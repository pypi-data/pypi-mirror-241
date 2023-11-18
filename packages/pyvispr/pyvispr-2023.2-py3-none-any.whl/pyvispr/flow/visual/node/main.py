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

import typing

import PyQt6.QtWidgets as wg
from PyQt6.QtCore import QPoint, QPointF, QRectF
from PyQt6.QtCore import Qt as constant_e
from PyQt6.QtGui import QBrush, QColor

from pyvispr.flow.descriptive.node import node_t as node_description_t
from pyvispr.flow.functional.node.main import node_t
from pyvispr.flow.visual.node.input import ii_manager_t
from pyvispr.widget.flow.node_input import interactive_input_t
from pyvispr.widget.general.info_box import info_box_manager_t

total_width_c = 120
total_height_c = 75
button_width_c = 15

resting_brush_c = QBrush(QColor(230, 230, 230))
selected_brush_c = QBrush(QColor(200, 200, 255))
running_brush_c = QBrush(QColor(0, 230, 0))
inactive_inout_brush_c = QBrush(QColor(80, 230, 230))
active_inout_brush_c = QBrush(QColor(0, 230, 80))
config_brush_c = QBrush(QColor(230, 0, 0))
next_run_brush_normal_c = QBrush(QColor(0, 0, 240))
next_run_brush_needs_c = QBrush(QColor(255, 230, 80))
next_run_brush_running_c = QBrush(QColor(0, 130, 240))


class visual_node_t(wg.QGraphicsRectItem):
    active_src_node = None
    active_src_out_name = None
    active_src_out_types = None

    active_dst_node = None
    active_dst_in_name = None
    active_dst_in_types = None

    should_show_info_boxes = False

    # --- VISUAL NODE INSTANTIATION

    def __init__(self, node: node_t, /, *, pos=None):
        """
        ii: interactive input
        """
        super().__init__(QRectF(0, 0, total_width_c, total_height_c))

        self.parent_graph = None
        self.node = node

        self.in_btn = None
        self.out_btn = None
        self.config_btn = None
        self.next_run_btn = None

        self.ii_manager = ii_manager_t(node.module)
        if self.ii_manager.RunConstructor is None:
            self.ii_manager = None

        self.iio_container_wgt = None
        self.interactive_inputs = {}
        self.output_widgets = []

        self.SetupAndCreateElements(pos)

        self.setSelected(True)

        self.setAcceptHoverEvents(True)
        self.info_box_manager = None

    def __getattr__(self, attribute: str, /) -> typing.Any:
        """"""
        try:
            output = self.__getattribute__(attribute)
        except AttributeError:
            output = self.node.__getattribute__(attribute)
        return output

    def SetupAndCreateElements(self, pos):
        """"""
        if pos is None:
            self.setPos(0, 0)
        else:
            self.setPos(pos)

        self.setFlag(wg.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(wg.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(wg.QGraphicsItem.GraphicsItemFlag.ItemClipsChildrenToShape)
        self.setFlag(wg.QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges)
        self.setBrush(resting_brush_c)

        label = wg.QGraphicsTextItem(self)
        label.setHtml(self.name)
        label.setPos(button_width_c, 0)
        label.setTextWidth(total_width_c - 2 * button_width_c)
        # label.setTextInteractionFlags(constant_e.TextSelectableByMouse)

        if self.n_inputs > 0:
            self.in_btn = wg.QGraphicsRectItem(
                QRectF(0, 0, button_width_c, total_height_c),
                self,
            )
            self.in_btn.setBrush(inactive_inout_brush_c)
        else:
            self.in_btn = None

        if self.n_outputs > 0:
            self.out_btn = wg.QGraphicsRectItem(
                QRectF(
                    total_width_c - button_width_c,
                    0,
                    button_width_c,
                    total_height_c,
                ),
                self,
            )
            self.out_btn.setBrush(inactive_inout_brush_c)
        else:
            self.out_btn = None

        config_btn_width = int((total_width_c - 2 * button_width_c) / 2.5)
        self.config_btn = wg.QGraphicsRectItem(
            QRectF(
                button_width_c,
                total_height_c - button_width_c,
                config_btn_width,
                button_width_c,
            ),
            self,
        )
        self.config_btn.setBrush(config_brush_c)

        self.next_run_btn = wg.QGraphicsRectItem(
            QRectF(
                button_width_c + config_btn_width,
                total_height_c - button_width_c,
                total_width_c - 2 * button_width_c - config_btn_width,
                button_width_c,
            ),
            self,
        )
        self.next_run_btn.setBrush(next_run_brush_needs_c)

    def InstantiateIIOContainerWidget(self, parent_graph) -> None:
        """"""
        self.parent_graph = parent_graph

        self.iio_container_wgt = wg.QWidget()
        iio_container_lyt = wg.QVBoxLayout()
        iio_container_lyt.setAlignment(constant_e.AlignmentFlag.AlignTop)
        self.iio_container_wgt.setLayout(iio_container_lyt)

        iio_container_lyt.addWidget(
            wg.QLabel("<b><font color='#0000ff'>" + self.name + "</font></b>")
        )

        # center_btn = wg.QPushButton('Show on View')
        # cast(pyqtBoundSignal, center_btn.clicked).connect(self.ShowOnView)
        # iio_container_lyt.addWidget(center_btn)

        iio_container_lyt.addWidget(
            wg.QLabel(
                "<font color='#0000ff'><b>INPUT(S)</b> (excluding link-only)</font>"
            )
        )

        for name in self.inputs:
            if self.inputs[name].assignment != node_description_t.assignment_e.link:
                self.interactive_inputs[name] = interactive_input_t(
                    self.ii_manager,
                    name,
                    self.inputs[name].type,
                    self.inputs[name].default_value,
                    self.__InvalidateNodesInCascadeFromSelf__,
                    iio_container_lyt,
                )

        if self.n_outputs > 0:
            iio_container_lyt.addWidget(
                wg.QLabel("<b><font color='#0000ff'>OUTPUT(S)</font></b>")
            )

            for name in self.outputs:
                self.CreateOutputWidgets(name, self.outputs[name])
        else:
            iio_container_lyt.addWidget(
                wg.QLabel("<b><font color='#0000ff'>NO OUTPUTS</font></b>")
            )

    def CreateOutputWidgets(self, name, stripe):
        """"""
        layout = self.iio_container_wgt.layout()

        layout.addWidget(wg.QLabel(f"{name}:{stripe}"))

        output_widget = wg.QLabel("...")
        self.output_widgets.append(output_widget)
        layout.addWidget(output_widget)

    # --- VISUAL NODE PROPERTIES

    @property
    def input_anchor_coordinates(self) -> QPointF:
        return self.__in_out_anchor_coordinates__(endpoint_is_input=True)

    @property
    def output_anchor_coordinates(self) -> QPointF:
        return self.__in_out_anchor_coordinates__(endpoint_is_input=False)

    @staticmethod
    def TranslateEventPositionOnChild(event, child) -> QPoint:
        """"""
        return (
            event.screenPos() - event.pos().toPoint() + child.rect().topLeft().toPoint()
        )

    @property
    def info_text(self):
        """"""
        text = "Function: " + self.function_name + "\n"

        if self.needs_running:
            text += "Needs Running: True\n"
            if self.can_run:
                text += "Can Run: True\n"
            else:
                text += "Can Run: False\n"
        else:
            text += "Needs Running: False\n"

        if self.n_inputs > 0:
            text += "Input(s):\n"

            for name in self.inputs:
                text += f"    {name}:{self.inputs[name].type} = {self.inputs[name].default_value}\n"
        else:
            text += "No Inputs\n"

        if self.n_outputs > 0:
            text += "Output(s):\n"

            for name in self.outputs:
                text += f"    {name}:{self.outputs[name]}\n"
        else:
            text += "No Outputs\n"

        return text[:-1]

    # --- VISUAL NODE MODIFICATIONS

    def paint(self, painter, options, widget):
        """"""
        super().paint(painter, options, widget)

        # /!\ certainly a very bad way to paint (multiple calls of paint()???)
        if self.is_running:
            self.setBrush(running_brush_c)
        elif self.isSelected():
            self.setBrush(selected_brush_c)
        else:
            self.setBrush(resting_brush_c)

    def ChangeAppearanceToRunning(self, state_is_running):
        """"""
        if state_is_running:
            self.setBrush(running_brush_c)
            self.next_run_btn.setBrush(next_run_brush_running_c)
        else:
            self.setBrush(resting_brush_c)
            self.next_run_btn.setBrush(next_run_brush_normal_c)

    # --- VISUAL NODE INTERACTIONS

    def SelectNodeForLinkCreation(self, event, endpoint_is_input: bool) -> None:
        """"""
        if endpoint_is_input:
            if visual_node_t.active_dst_node is self:  # excludes the None case
                visual_node_t.DeselectSrcOrDstForLinkCreation(should_deselect_src=False)
                return

            if visual_node_t.active_src_node is self:  # excludes the None case
                return

            possible_names = self.input_names
            if visual_node_t.active_src_out_types is None:
                possible_names = tuple(
                    name
                    for name in possible_names
                    if not self.input_states[name].is_linked
                )
            else:  # "visual_node_t.active_src_node is not None" is implicit
                possible_names = tuple(
                    name
                    for name in possible_names
                    if (not self.input_states[name].is_linked)
                    and self.inputs[name].type == visual_node_t.active_src_out_types
                )

            if len(possible_names) == 0:
                return

            if visual_node_t.active_dst_node is not None:
                visual_node_t.DeselectSrcOrDstForLinkCreation(should_deselect_src=False)

            visual_node_t.active_dst_node = self
            self.in_btn.setBrush(active_inout_brush_c)
        #
        else:  # this else could be merged with the following if, but kept as is for aesthetics
            if visual_node_t.active_src_node is self:  # excludes the None case
                visual_node_t.DeselectSrcOrDstForLinkCreation(should_deselect_src=True)
                return

            if visual_node_t.active_dst_node is self:  # excludes the None case
                return

            possible_names = self.output_names
            if visual_node_t.active_dst_in_types is not None:
                # "visual_node_t.active_dst_node is not None" is implicit
                possible_names = tuple(
                    name
                    for name in possible_names
                    if self.outputs[name] == visual_node_t.active_dst_in_types
                )
                #
                if len(possible_names) == 0:
                    return

            if visual_node_t.active_src_node is not None:
                visual_node_t.DeselectSrcOrDstForLinkCreation(should_deselect_src=True)

            visual_node_t.active_src_node = self
            self.out_btn.setBrush(active_inout_brush_c)

        if (
            len(possible_names) > 1
        ):  # or node_control_t.NameIsAContextName(possible_names[0]):
            menu = wg.QMenu()

            if endpoint_is_input and (visual_node_t.active_src_node is not None):
                no_act = menu.addAction(visual_node_t.active_src_out_name + " ->")
                no_act.setEnabled(False)
            #
            elif (not endpoint_is_input) and (
                visual_node_t.active_dst_node is not None
            ):
                no_act = menu.addAction("-> " + visual_node_t.active_dst_in_name)
                no_act.setEnabled(False)

            menu_actions = len(possible_names) * [None]
            for name_idx, name in enumerate(possible_names):
                menu_actions[name_idx] = menu.addAction(name)

            if endpoint_is_input:
                selected_act = menu.exec(
                    visual_node_t.TranslateEventPositionOnChild(event, self.in_btn)
                )
            else:
                selected_act = menu.exec(
                    visual_node_t.TranslateEventPositionOnChild(event, self.out_btn)
                )
            if selected_act is None:
                visual_node_t.DeselectSrcOrDstForLinkCreation(should_deselect_src=True)
                visual_node_t.DeselectSrcOrDstForLinkCreation(should_deselect_src=False)
            else:
                self.SelectInOrOutForLinkCreation(
                    possible_names[menu_actions.index(selected_act)], endpoint_is_input
                )
        else:
            self.SelectInOrOutForLinkCreation(possible_names[0], endpoint_is_input)

    def SelectInOrOutForLinkCreation(self, name, name_is_input) -> None:
        """"""
        if name_is_input:
            visual_node_t.active_dst_in_name = name
            visual_node_t.active_dst_in_types = visual_node_t.active_dst_node.inputs[
                name
            ].type
        else:
            visual_node_t.active_src_out_name = name
            visual_node_t.active_src_out_types = visual_node_t.active_src_node.outputs[
                name
            ]

        if not (
            (visual_node_t.active_src_node is None)
            or (visual_node_t.active_dst_node is None)
        ):
            self.parent_graph.AddVisualLink(
                visual_node_t.active_src_node,
                visual_node_t.active_src_out_name,
                visual_node_t.active_dst_node,
                visual_node_t.active_dst_in_name,
            )

            visual_node_t.DeselectSrcOrDstForLinkCreation(should_deselect_src=True)
            visual_node_t.DeselectSrcOrDstForLinkCreation(should_deselect_src=False)

    @staticmethod
    def DeselectSrcOrDstForLinkCreation(should_deselect_src: bool) -> None:
        """"""
        if should_deselect_src:
            if visual_node_t.active_src_node is not None:
                visual_node_t.active_src_node.out_btn.setBrush(inactive_inout_brush_c)
                visual_node_t.active_src_node = None
                visual_node_t.active_src_out_name = None
                visual_node_t.active_src_out_types = None
        elif visual_node_t.active_dst_node is not None:
            visual_node_t.active_dst_node.in_btn.setBrush(inactive_inout_brush_c)
            visual_node_t.active_dst_node = None
            visual_node_t.active_dst_in_name = None
            visual_node_t.active_dst_in_types = None

    # --- VISUAL NODE EVENT HANDLERS

    def hoverEnterEvent(self, event):
        """
        Note: The value of visual_link_t.should_show_info_boxes could be used in __init__ to activate or not
        enter and leave events. However, this would require to write a method to toggle the boolean
        and activate/deactivate these events. Maybe one day...
        """
        if visual_node_t.should_show_info_boxes:
            self.info_box_manager = info_box_manager_t(
                self,
                event.scenePos() - event.screenPos(),
                self.parent_graph.visual_manager,
            )  # QCursor.pos()

    def hoverLeaveEvent(self, event):
        """
        See note in hoverEnterEvent.

        Do not know if a leave event can be generated w/o prior enter event.
        Supposedly no, but...
        """
        if visual_node_t.should_show_info_boxes and (self.info_box_manager is not None):
            self.info_box_manager.should_still_display_box = False

    def mousePressEvent(self, event):
        """"""
        if visual_node_t.should_show_info_boxes and (self.info_box_manager is not None):
            self.info_box_manager.should_still_display_box = False

        if event.buttons() == constant_e.MouseButton.LeftButton:
            if (self.in_btn is not None) and self.in_btn.contains(event.pos()):
                self.SelectNodeForLinkCreation(event, endpoint_is_input=True)
            elif (self.out_btn is not None) and self.out_btn.contains(event.pos()):
                self.SelectNodeForLinkCreation(event, endpoint_is_input=False)
            elif self.config_btn.contains(event.pos()):
                menu = wg.QMenu()
                # cancel_act_u = menu.addAction("Close Menu")  # type: wg.QAction
                no_act = menu.addAction("or")
                no_act.setEnabled(False)
                remove_act = menu.addAction("Remove Node")
                selected_act = menu.exec(
                    visual_node_t.TranslateEventPositionOnChild(event, self.config_btn)
                )
                if selected_act is remove_act:
                    visual_graph = self.parent_graph
                    visual_graph.RemoveVisualNode(self)
            elif self.next_run_btn.contains(event.pos()):
                pass

    def itemChange(self, change, data):
        """"""
        if change == wg.QGraphicsItem.GraphicsItemChange.ItemPositionChange:
            for visual_link in self.parent_graph.visual_links:
                if self is visual_link.visual_node_o:
                    visual_link.SetPath(
                        visual_link.visual_node_o.output_anchor_coordinates,
                        visual_link.destination,
                    )
                elif self is visual_link.visual_node_d:
                    visual_link.SetPath(
                        visual_link.origin,
                        visual_link.visual_node_d.input_anchor_coordinates,
                    )

        return super().itemChange(change, data)

    # --- VISUAL NODE PRIVATE FUNCTIONS

    # --- --- properties

    def __in_out_anchor_coordinates__(self, endpoint_is_input) -> QPointF:
        """"""
        endpoint_pos = self.scenePos()
        endpoint_pos.setY(endpoint_pos.y() + int(0.5 * self.boundingRect().height()))

        if not endpoint_is_input:
            endpoint_pos.setX(endpoint_pos.x() + self.boundingRect().width())

        return endpoint_pos

    # --- --- modifications

    def __InvalidateNodesInCascadeFromSelf__(self, _: str = "", /) -> None:
        """
        used in instantiation
        """
        self.parent_graph.InvalidateNodesInCascadeFromNode(self.node)
