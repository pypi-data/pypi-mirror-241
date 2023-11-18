# Copyright CNRS/Inria/UniCA
# Contributor(s): Eric Debreuve (since 2017)
#
# eric.debreuve@cnrs.fr
#
# This software is governed by the CeCILL  license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

from __future__ import annotations

import ast
import ast as prsr
import dataclasses as dtcl
import importlib as mprt
from enum import Enum as enum_t
from pathlib import Path as path_t
from types import ModuleType as module_t
from typing import Any, Callable, ClassVar
from typing import NamedTuple as named_tuple_t

from pyvispr.python.module import ModuleForPath

# EDUCATED_NAME: Node name as it will appear in interface.
# ACTUAL_SOURCE: Where is the node implemented? See node_t.path and node_t.source_e.
# FUNCTION_NAME: Node function.
# MISSING_IN_INDICATORS: Sequence of booleans indicating the presence of *args and **kwargs arguments.
# MISSING_IN_HINTS: Sequence of arguments with missing type hint.
# MISSING_OUT_HINT_INDICATOR: Boolean indicating the presence of output type hint.
#
# DEFAULT_MAIN_FUNCTION: Default node function name.
# MISSING_IN_NAME_PREFIX: With integer postfix, replaces *args and **kwargs in argument list.
# HINT_PLACEHOLDER: Replaces missing type hints.
EDUCATED_NAME = "_name"
ACTUAL_SOURCE = "_actual"
FUNCTION_NAME = "_function_name"
MISSING_IN_INDICATORS = "_missing_in"
MISSING_IN_HINTS = "_missing_in_hint"
MISSING_OUT_HINT_INDICATOR = "_missing_out_hint"
#
DEFAULT_MAIN_FUNCTION = "Main"
MISSING_IN_NAME_PREFIX = "_missing_"
HINT_PLACEHOLDER = "no_hint"


@dtcl.dataclass(repr=False, eq=False)
class node_t:
    class not_set_t:
        pass

    DEFAULT_NOT_SET: ClassVar[not_set_t] = not_set_t()

    class source_e(enum_t):
        not_set = 0
        local = 1
        referenced = 2
        system = 3

    class assignment_e(enum_t):
        """
        full: link + interactive, user input.
        """

        link = 0
        full = 1

    class input_t(named_tuple_t):
        type: str
        assignment: node_t.assignment_e
        default_value: Any

        @property
        def has_default(self) -> bool:
            """"""
            return self.default_value is not node_t.DEFAULT_NOT_SET

    path: str | path_t
    name: str = ""
    keywords: str = ""
    short_description: str = ""
    long_description: str = ""
    source: node_t.source_e = source_e.not_set
    function_name: str | None = None
    missing_in_indicators: tuple[bool, ...] | None = None
    missing_in_hints: tuple[str, ...] | None = None
    missing_out_hint_indicator: bool | None = None
    inputs: dict[str, input_t] | None = None
    outputs: dict[str, str] | None = None
    #
    module: module_t | None = None
    Function: Callable[..., Any] | None = None

    def __post_init__(self) -> None:
        """"""
        if self.name.__len__() > 0:
            return

        if isinstance(self.path, str):
            self.path = path_t(self.path)
        self.path = self.path.expanduser()
        with open(self.path) as accessor:
            tree = prsr.parse(accessor.read())
        for node in prsr.walk(tree):
            if not isinstance(node, prsr.FunctionDef):
                continue

            documentation = prsr.get_docstring(node, clean=False)

            (
                self.name,
                actual,
                self.function_name,
                self.missing_in_indicators,
                missing_in_hints,
                missing_out_hint_indicator,
                assignments,
            ) = _N_A_F_A(documentation)
            if actual is None:
                self.source = node_t.source_e.local
            elif actual.endswith(".py"):
                self.source = node_t.source_e.referenced
                self.path = path_t(actual)
            else:
                self.source = node_t.source_e.system
                self.path = actual

            if self.missing_in_indicators is None:
                inputs = {}
                arguments_sets = node.args
                for arguments, defaults in (
                    (
                        arguments_sets.posonlyargs,
                        arguments_sets.posonlyargs.__len__()
                        * (node_t.DEFAULT_NOT_SET,),
                    ),
                    (arguments_sets.args, arguments_sets.defaults),
                    (arguments_sets.kwonlyargs, arguments_sets.kw_defaults),
                ):
                    for argument, default in zip(arguments, defaults):
                        stripe = argument.annotation
                        if isinstance(stripe, prsr.Name):
                            stripe = stripe.id
                        elif isinstance(stripe, prsr.Constant):
                            stripe = stripe.value

                        assignment = assignments.get(argument.arg, "link")
                        assignment = node_t.assignment_e[assignment]

                        if default is node_t.DEFAULT_NOT_SET:
                            default_value = node_t.DEFAULT_NOT_SET
                        elif isinstance(default, ast.Constant):
                            default_value = default.value
                        elif isinstance(default, ast.Name):
                            default_value = default.id
                        else:
                            try:
                                default_value = ast.literal_eval(default)
                            except (
                                ValueError,
                                TypeError,
                                SyntaxError,
                                MemoryError,
                                RecursionError,
                            ):
                                function_name = (
                                    actual if actual is not None else self.function_name
                                )
                                raise ValueError(
                                    f"Unhandled default specification: {default}, with type: {type(default).__name__}, "
                                    f'dumped as: {ast.dump(default)}, for input: {argument.arg}:{stripe} of function "{function_name}" of node "{self.name}".'
                                )

                        inputs[argument.arg] = self.__class__.input_t(
                            type=stripe,
                            assignment=assignment,
                            default_value=default_value,
                        )
                self.inputs = inputs

            if missing_in_hints is not None:
                self.missing_in_hints = _SplitAndStriped(missing_in_hints, ",")

            if missing_out_hint_indicator is None:
                self.missing_out_hint_indicator = False

                outputs = node.returns.value
                if outputs is None:
                    outputs = ()
                elif isinstance(outputs, str):
                    if "," in outputs:
                        outputs = outputs.split(",")
                    else:
                        outputs = (outputs,)
                else:
                    raise ValueError
                self.outputs = dict(_SplitAndStriped(_out, ":") for _out in outputs)
            else:
                self.missing_out_hint_indicator = True

    @property
    def misses_hints(self) -> bool:
        """"""
        return (self.missing_in_hints is not None) or self.missing_out_hint_indicator

    @property
    def needs_specification(self) -> bool:
        """"""
        return (self.inputs is None) or (self.outputs is None)

    @property
    def n_inputs(self) -> int:
        """"""
        return self.inputs.__len__()

    @property
    def input_names(self) -> tuple[str, ...]:
        """"""
        return tuple(self.inputs.keys())

    @property
    def input_types(self) -> tuple[str, ...]:
        """"""
        return tuple(_elm.type for _elm in self.inputs.values())

    @property
    def input_default_values(self) -> tuple[Any | node_t.DEFAULT_NOT_SET, ...]:
        """"""
        return tuple(_elm.default_value for _elm in self.inputs.values())

    @property
    def n_outputs(self) -> int:
        """"""
        return self.outputs.__len__()

    @property
    def output_names(self) -> tuple[str, ...]:
        """"""
        return tuple(self.outputs.keys())

    @property
    def output_types(self) -> tuple[str, ...]:
        """"""
        return tuple(self.outputs.values())

    def AsDict(self) -> dict[str, Any]:
        """"""
        return {_key.name: getattr(self, _key.name) for _key in dtcl.fields(self)}

    def Activate(self) -> None:
        """"""
        if self.module is None:
            if self.source is self.__class__.source_e.referenced:
                self.module, self.Function = _M_F_FromPathAndName(
                    self.path, self.function_name
                )
            else:  # self.__class__.source_e.system
                self.module, self.Function = _M_F_FromPyPath(self.path)


def _N_A_F_A(
    documentation: str, /
) -> tuple[
    str, str | None, str | None, str | None, str | None, str | None, dict[str, str]
]:
    """"""
    description = documentation.strip().splitlines()
    description = dict(_SplitAndStriped(_lne, ":") for _lne in description)

    if (actual := description.get(ACTUAL_SOURCE)) is None:
        function_name = DEFAULT_MAIN_FUNCTION
    else:
        function_name = description.get(FUNCTION_NAME)

    # Returned "description" on last position will be interpreted as assignment types of the inputs.
    return (
        description[EDUCATED_NAME],
        actual,
        function_name,
        description.get(MISSING_IN_INDICATORS),
        description.get(MISSING_IN_HINTS),
        description.get(MISSING_OUT_HINT_INDICATOR),
        description,
    )


def _M_F_FromPathAndName(path: str, function_name: str, /) -> tuple[module_t, Callable]:
    """"""
    # TODO: Add error management.
    module = ModuleForPath(path_t(path))
    Function = getattr(module, function_name)

    return module, Function


def _M_F_FromPyPath(py_path: str, /) -> tuple[module_t, Callable]:
    """"""
    # TODO: Add error management.
    last_dot_idx = py_path.rfind(".")
    module = mprt.import_module(py_path[:last_dot_idx])
    Function = getattr(module, py_path[(last_dot_idx + 1) :])

    return module, Function


def _SplitAndStriped(text: str, separator: str, /) -> tuple[str, str] | tuple[str, ...]:
    """"""
    return tuple(_elm.strip() for _elm in text.split(sep=separator))


# from inspect import getdoc as GetFunctionDoc
# from inspect import signature as GetFunctionSignature
# signature = GetFunctionSignature(function)
# documentation = GetFunctionDoc(function)
