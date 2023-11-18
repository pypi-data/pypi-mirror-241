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

from copy import copy as MakeACopy
from typing import cast

import PyQt6.QtWidgets as wg
from numpy import array as array_t
from PyQt6.QtCore import pyqtBoundSignal

from pyvispr.flow.descriptive.node import node_t


class interactive_input_t:  # ii: interactive input
    placeholder_text = "Hover for example(s)"

    def __init__(
        self,
        external_manager,
        name,
        stripe,
        default_value,
        invalidating_nodes_fct,
        layout,
    ) -> None:
        """"""
        self.external_manager = external_manager
        self.type = stripe
        self.selected_type_wgt = None
        self.typed_input_wgts = [None]
        self.hover_info_texts = [None]

        if default_value is node_t.DEFAULT_NOT_SET:
            label_txt = name
        else:
            label_txt = name + "=" + default_value
        layout.addWidget(wg.QLabel(label_txt))

        universal_widget = None

        # TODO: Switch to proper type management with conf-ini-g.
        input_idx = 0
        input_type = stripe
        raw_input_type = input_type

        if self.selected_type_wgt is not None:
            self.selected_type_wgt.addItem(raw_input_type)

        if self.external_manager is None:
            widget = None

            if input_type == bool.__name__:
                widget = wg.QComboBox()
                widget.addItem("True")
                widget.addItem("False")
                cast(pyqtBoundSignal, widget.currentIndexChanged).connect(
                    invalidating_nodes_fct
                )
            #
            elif input_type == int.__name__:
                self.hover_info_texts[input_idx] = "int"
            #
            elif input_type == float.__name__:
                self.hover_info_texts[input_idx] = "float"
            #
            elif input_type == complex.__name__:
                self.hover_info_texts[input_idx] = "complex: e.g., 1+2j"
            #
            elif (
                (input_type == "numpy.ndarray")
                or (input_type == list.__name__)
                or (input_type == tuple.__name__)
                or (input_type == set.__name__)
            ):
                self.hover_info_texts[input_idx] = input_type + ": e.g., 1, 2, 3"
            #
            elif input_type == range.__name__:
                self.hover_info_texts[input_idx] = (
                    input_type + ": e.g., 1..3 for 1, 2, 3, or 1..2..6 for 1, 3, 5"
                )
            #
            elif input_type == dict.__name__:
                self.hover_info_texts[input_idx] = (
                    input_type + ": key_1: value_1, key_2: value_2..."
                )
            #
            elif input_type == str.__name__:
                self.hover_info_texts[input_idx] = input_type
            #
            else:
                self.hover_info_texts[input_idx] = raw_input_type
        #
        else:
            widget = self.external_manager.RunConstructor(
                raw_input_type, invalidating_nodes_fct
            )

        if widget is None:
            if universal_widget is None:
                universal_widget = wg.QLineEdit()
                cast(pyqtBoundSignal, universal_widget.textChanged).connect(
                    invalidating_nodes_fct
                )
                universal_widget.setPlaceholderText(
                    interactive_input_t.placeholder_text
                )
                if self.hover_info_texts[input_idx] is not None:
                    universal_widget.setToolTip(self.hover_info_texts[input_idx])
                layout.addWidget(universal_widget)
            #
            self.typed_input_wgts[input_idx] = universal_widget
        #
        else:
            self.typed_input_wgts[input_idx] = widget
            layout.addWidget(widget)

        if self.selected_type_wgt is not None:
            cast(pyqtBoundSignal, self.selected_type_wgt.currentIndexChanged).connect(
                self.__AckNewSelectedType__
            )
            cast(pyqtBoundSignal, self.selected_type_wgt.currentIndexChanged).connect(
                invalidating_nodes_fct
            )

    @property
    def value(self) -> object:
        """"""
        if self.selected_type_wgt is None:
            input_type = self.type
            input_wgt = self.typed_input_wgts[0]
        else:
            input_type = self.selected_type_wgt.currentText()
            input_wgt = self.typed_input_wgts[self.selected_type_wgt.currentIndex()]

        if self.external_manager is None:
            try:
                if input_type == bool.__name__:
                    value_l = input_wgt.currentText() == str(True)
                elif (
                    input_type == int.__name__
                ):  # /!\ eventually, validators and such will be used; for now, only 'int' has a workaround for invalid entries
                    value_l = int(eval(input_wgt.text()))
                elif input_type == float.__name__:
                    value_l = eval(input_wgt.text())
                elif input_type == complex.__name__:
                    value_l = eval(input_wgt.text().replace(" ", ""))
                elif input_type == "numpy.ndarray":
                    value_l = array_t(eval("[" + input_wgt.text() + "]"))
                    if len(value_l) == 0:
                        value_l = None
                elif input_type == list.__name__:
                    value_l = eval("[" + input_wgt.text() + "]")
                    if len(value_l) == 0:
                        value_l = None
                elif input_type == tuple.__name__:
                    value_l = eval("(" + input_wgt.text() + ")")
                    if len(value_l) == 0:
                        value_l = None
                elif input_type == set.__name__:
                    value_l = eval("{" + input_wgt.text() + "}")
                    if len(value_l) == 0:
                        value_l = None
                elif input_type == range.__name__:
                    text = input_wgt.text()
                    if len(text) > 0:
                        bounds_in_list = text.split("..")
                        if len(bounds_in_list) < 3:
                            value_l = range(
                                eval(bounds_in_list[0]), eval(bounds_in_list[1]) + 1
                            )
                        else:
                            value_l = range(
                                eval(bounds_in_list[0]),
                                eval(bounds_in_list[2]) + 1,
                                eval(bounds_in_list[1]),
                            )
                    else:
                        value_l = None
                elif input_type == dict.__name__:
                    text = input_wgt.text()
                    if len(text) > 0:
                        dictionary = dict(
                            tuple(
                                [elm.strip() for elm in key_value.split(":")]
                                for key_value in text.split(",")
                            )
                        )
                        for key, value in dictionary.items():
                            dictionary[key] = eval(value)
                        value_l = dictionary
                    else:
                        value_l = None
                elif input_type == str.__name__:
                    value_l = MakeACopy(input_wgt.text())
                    if len(value_l) == 0:
                        value_l = None
                else:
                    value_l = MakeACopy(input_wgt.text())
            except:
                value_l = None

            return value_l
        else:
            return self.external_manager.RunGetter(input_wgt)

    def SetValue(self, ii_value: object) -> None:
        """
        method name suggests parameter order: ...Value...: first value, ...OfWidget...: then widget
        :param ii_value:
        """
        if self.selected_type_wgt is None:
            input_type = self.type
            input_wgt = self.typed_input_wgts[0]
        else:
            input_type = self.selected_type_wgt.currentText()
            input_wgt = self.typed_input_wgts[self.selected_type_wgt.currentIndex()]

        if self.external_manager is None:
            if input_type == bool.__name__:
                input_wgt.setCurrentText(ii_value)
            elif input_type == int.__name__:
                input_wgt.setText(str(ii_value))
            elif input_type == float.__name__:
                input_wgt.setText(str(ii_value))
            elif input_type == complex.__name__:
                input_wgt.setText(str(ii_value))
            elif input_type == "numpy.ndarray":
                input_wgt.setText(str(ii_value)[1:-1])
            elif input_type == list.__name__:
                input_wgt.setText(str(ii_value)[1:-1])
            elif input_type == tuple.__name__:
                input_wgt.setText(str(ii_value)[1:-1])
            elif input_type == set.__name__:
                input_wgt.setText(str(ii_value)[1:-1])
            elif input_type == range.__name__:
                if cast(range, ii_value).step == 1:
                    input_wgt.setText(
                        str(cast(range, ii_value).start)
                        + ".."
                        + str(cast(range, ii_value).stop - 1)
                    )
                else:
                    input_wgt.setText(
                        str(cast(range, ii_value).start)
                        + ".."
                        + str(cast(range, ii_value).step)
                        + ".."
                        + str(cast(range, ii_value).stop - 1)
                    )
            elif input_type == dict.__name__:
                dict_as_str = ""
                key_value_list = [
                    str(key) + ":" + str(key_value)
                    for key, key_value in sorted(cast(dict, ii_value).items())
                ]
                for key_value in key_value_list:
                    dict_as_str += key_value + ", "
                input_wgt.setText(dict_as_str[:-2])
            else:  # input_type is str or anything else (note: str() has no effect on a string)
                input_wgt.setText(str(ii_value))
        else:
            self.external_manager.RunSetter(input_wgt, ii_value)

    def __AckNewSelectedType__(self, new_idx_u: int) -> None:
        """"""
        if self.hover_info_texts[new_idx_u] is not None:
            self.typed_input_wgts[new_idx_u].setToolTip(
                self.hover_info_texts[new_idx_u]
            )
