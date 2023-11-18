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

from PyQt6.QtCore import QPointF
from PyQt6.QtCore import Qt as constant_e
from PyQt6.QtGui import QColor, QPainterPath, QPen
from PyQt6.QtWidgets import QGraphicsPathItem, QMenu

from pyvispr.flow.visual.node.main import button_width_c
from pyvispr.widget.general.info_box import info_box_manager_t

horizontal_shift_c = 3 * button_width_c

pen_for_empty_c = QPen(QColor(255, 0, 0), 2, constant_e.PenStyle.SolidLine)
pen_for_full_c = QPen(QColor(0, 255, 0), 2, constant_e.PenStyle.SolidLine)


class visual_link_t(QGraphicsPathItem):
    should_show_info_boxes = True

    # --- VISUAL LINK INSTANTIATION

    def __init__(
        self,
        parent_graph,
        visual_node_o,
        origin: QPointF,
        visual_node_d,
        destination: QPointF,
        is_already_full=False,
    ):
        """"""
        super().__init__()

        self.parent_graph = parent_graph

        self.visual_node_o = visual_node_o
        self.visual_node_d = visual_node_d

        self.origin = None  # in terms of (x,y)-coordinates, not node
        self.destination = None  # same as above

        self.SetPath(origin, destination)
        if is_already_full:
            self.setPen(pen_for_full_c)
        else:
            self.setPen(pen_for_empty_c)

        self.setAcceptHoverEvents(True)
        self.info_box_manager = None

    # --- VISUAL LINK PROPERTIES

    @property
    def underlying_links(self) -> list:
        """"""
        node_1 = self.visual_node_o.node
        node_2 = self.visual_node_d.node
        idx_1 = self.parent_graph.nodes.index(node_1)

        underlying_links = []
        for output_name, links_per_out in self.parent_graph.links[idx_1].items():
            if node_2 in links_per_out:
                idc_2 = [idx for idx, elm in enumerate(links_per_out) if elm is node_2]
                for link_idx in idc_2:
                    underlying_links.append([output_name, links_per_out[link_idx + 1]])

        return underlying_links

    @property
    def info_text(self):
        """"""
        text = ""
        for link in self.underlying_links:
            text += link[0] + "->" + link[1] + "\n"

        return text[:-1]

    # --- VISUAL LINK MODIFICATIONS

    def SetPath(self, origin: QPointF, destination: QPointF) -> None:
        """"""
        self.origin = origin  # type: QPointF
        self.destination = destination  # type: QPointF

        direction = self.destination - self.origin  # type: QPointF

        dir_1 = 0.4 * direction  # type: QPointF
        dir_2 = 0.4 * direction  # type: QPointF

        dir_1.setY(0)
        if dir_1.x() < 0:
            dir_1.setX(-dir_1.x())
        if dir_1.x() < horizontal_shift_c:
            dir_1.setX(horizontal_shift_c)

        dir_2.setY(0)
        if dir_2.x() < 0:
            dir_2.setX(-dir_2.x())
        if dir_2.x() < horizontal_shift_c:
            dir_2.setX(horizontal_shift_c)

        path = QPainterPath(self.origin)
        path.cubicTo(self.origin + dir_1, self.destination - dir_2, self.destination)
        self.setPath(path)

    def ChangeAppearanceToFull(self, state_is_full):
        """"""
        if state_is_full:
            self.setPen(pen_for_full_c)
        else:
            self.setPen(pen_for_empty_c)

    # --- VISUAL LINK EVENT HANDLERS

    def hoverEnterEvent(self, event):
        """
        Note: The value of visual_link_t.should_show_info_boxes could be used in __init__ to activate or not
        enter and leave events. However, this would require to write a method to toggle the boolean
        and activate/deactivate these events. Maybe one day...
        """
        if visual_link_t.should_show_info_boxes:
            self.info_box_manager = info_box_manager_t(
                self,
                event.scenePos() - QPointF(event.screenPos()),
                self.parent_graph.visual_manager,
            )

    def hoverLeaveEvent(self, event):
        """
        See note in hoverEnterEvent.

        Do not know if a leave event can be generated w/o prior enter event.
        In theory, no, but in practice...
        """
        if visual_link_t.should_show_info_boxes and (self.info_box_manager is not None):
            self.info_box_manager.should_still_display_box = False

    def mousePressEvent(self, event):
        """
        /!\ strange behavior (Qt bug): sometimes a mouse press on a different link (or even in the background)
        calls the mousePressEvent callback of the previously pressed link; and this repeats several times,
        until clicking far away from any link!!!
        """
        menu = QMenu()
        cancel_act = menu.addAction("Close Menu")
        no_act = menu.addAction("or Remove Link(s):")
        no_act.setEnabled(False)

        underlying_links = self.underlying_links

        menu_actions = len(underlying_links) * [None]
        for link_idx, link in enumerate(underlying_links):
            menu_actions[link_idx] = menu.addAction(link[0] + "->" + link[1])
        if len(underlying_links) > 1:
            menu_actions.append(menu.addAction("Remove All"))

        selected_act = menu.exec(event.screenPos())
        if not ((selected_act is None) or (selected_act is cancel_act)):
            if selected_act is menu_actions[-1]:
                self.parent_graph.RemoveVisualLink(self, None, True)
            else:
                self.parent_graph.RemoveVisualLink(
                    self,
                    underlying_links[menu_actions.index(selected_act)],
                    len(underlying_links) == 1,
                )
