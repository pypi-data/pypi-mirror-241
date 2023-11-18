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

import dataclasses as dtcl
import typing

from pyvispr.flow.descriptive.node import node_t as base_t
from pyvispr.flow.functional.node.state import input_state_t, output_state_t


@dtcl.dataclass(repr=False, eq=False)
class node_t(base_t):
    input_states: dict[str, input_state_t] | None = None
    output_states: dict[str, output_state_t] | None = None
    is_disabled: bool = False
    is_running: bool = False
    # Used only for script output (no need to save, or expose).
    id: int = -1

    @classmethod
    def NewForDescription(cls, description: base_t, /) -> node_t:
        """"""
        # TODO: Store the (activated) description as an attribute to avoid redundant storage among the functional nodes.
        description.Activate()
        as_dict = description.AsDict()

        input_states = {_nme: input_state_t() for _nme in description.input_names}
        output_states = {_nme: output_state_t() for _nme in description.output_names}
        as_dict["input_states"] = input_states
        as_dict["output_states"] = output_states

        return cls(**as_dict)

    def UniqueNameWithPostfix(self, postfix: str, /) -> str:
        """"""
        return self.name + "_" + str(self.id) + "_" + postfix

    def SetInputSource(
        self, input_name: str, src_node: node_t, output_name: str
    ) -> None:
        """
        Method name suggests parameter order: ...Input...: first input name, ...BackLink: then source of link as
        src_node, output_name
        """
        self.input_states[
            input_name
        ].source_output_name = src_node.UniqueNameWithPostfix(output_name)

    def SetInputLinkingState(self, name: str, is_linked: bool, /):
        """"""
        if name is None:
            for input_state in self.input_states.values():
                input_state.is_linked = is_linked
        else:
            self.input_states[name].is_linked = is_linked

    def SetOutputLinkingState(self, name: str, is_linked: bool):
        """"""
        self.output_states[name].is_linked = is_linked

    def SourceOutputOfInput(self, name: str, /) -> str:
        """"""
        if name in self.inputs:
            return self.input_states[name].source_output_name

        return "non-existing back-link"

    @property
    def needs_running(self) -> bool:
        """
        Note: the decision is based on whether the outputs are valid for use downward in the workflow,
        not on whether the inputs have changed since the last run.
        """
        if self.is_disabled:
            return False

        if self.n_outputs == 0:
            return True

        if any(
            _stt.is_linked and (not _stt.has_value)
            for _stt in self.output_states.values()
        ):
            return True

        return False

    @property
    def can_run(self) -> bool:
        """
        This method is meant to be called from functional.graph.Run,
        i.e., after visual.graph.RunInteractively has read the ii_values
        to set the corresponding node input values if appropriate.
        Appropriate means: the corresponding inputs have mode "full" (actually,
        not "link") and they are not linked to outputs.
        """
        return (self.n_inputs == 0) or all(
            self.input_states[_nme].has_value or self.inputs[_nme].has_default
            for _nme in self.inputs
        )

    def InvalidateInputs(self, /, *, name: str = None) -> None:
        """"""
        if name is None:
            for state in self.input_states.values():
                state.Invalidate()
        else:
            self.input_states[name].Invalidate()

    def InvalidateOutputs(self, /, *, observer=None) -> None:
        """"""
        if self.n_outputs > 0:
            for name in self.outputs:
                self.output_states[name].Invalidate()

                if observer is not None:
                    observer.AckOutputLostValue(self, name)
        else:
            if observer is not None:
                observer.AckOutputLostValue(self, None)

    def Run(self, script_accessor=None):
        """"""

        def _FakeOutputs(n_outputs: int, fake_value: object) -> object | tuple:
            """"""
            return n_outputs * (fake_value,) if n_outputs > 1 else fake_value

        self.is_running = True

        try:
            if self.n_inputs > 0:
                anonymous_args = []
                named_args = {}
                anonymous_args_as_str = []
                named_args_as_str = []

                for name, description in self.inputs.items():
                    if self.input_states[name].has_value:
                        value = self.input_states[name].value
                        if description.has_default:
                            named_args[name] = value
                            if script_accessor is not None:
                                named_args_as_str.append(
                                    f"{name}={self.input_states[name].source_output_name}"
                                )
                        else:
                            anonymous_args.append(value)
                            if script_accessor is not None:
                                anonymous_args_as_str.append(
                                    self.input_states[name].source_output_name
                                )
                    elif description.has_default:
                        named_args[name] = description.default_value
                        # TODO: Check old code to see how default values are handled.
                        if script_accessor is not None:
                            named_args_as_str.append(
                                f"{name}={description.default_value}"
                            )
                    else:
                        raise ValueError("Should not have happened, I think...")

                if script_accessor is None:
                    output_values = self.Function(*anonymous_args, **named_args)
                else:
                    arguments = ", ".join(anonymous_args_as_str + named_args_as_str)
                    script_accessor.write(f"{self.Function.__name__}({arguments})\n")
                    output_values = _FakeOutputs(self.n_outputs, "Done")
            #
            elif script_accessor is None:
                output_values = self.Function()
            else:
                script_accessor.write(f"{self.Function.__name__}()\n")
                output_values = _FakeOutputs(self.n_outputs, "Done")
        except Exception as exception:
            output_values = _FakeOutputs(self.n_outputs, None)
            print(f"Exception while running {self.name}:", exception)

        self.is_running = False

        return output_values

    def SetInputValue(self, name: str, value: typing.Any, /) -> None:
        """"""
        self.input_states[name].value = value

    def SetOutputValue(self, name: str, value: typing.Any, /, *, observer=None) -> None:
        """"""
        self.output_states[name].value = value
        if not ((value is output_state_t.VALUE_NOT_SET) or (observer is None)):
            observer.AckOutputGotValue(self, name)
