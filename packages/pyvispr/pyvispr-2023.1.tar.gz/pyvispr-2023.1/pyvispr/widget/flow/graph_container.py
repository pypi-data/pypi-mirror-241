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

from typing import cast

import PyQt6.QtWidgets as wg
from PyQt6.QtCore import pyqtBoundSignal
from PyQt6.QtGui import QPainter as painter_t

from pyvispr.flow.visual.graph import visual_graph_t
from pyvispr.flow.visual.node.main import visual_node_t


class graph_container_wgt_t(wg.QGraphicsView):
    zoom_factor_c = 1.25

    def __init__(self, parent_wgt, iio_manager):
        """"""
        super().__init__(parent_wgt)

        self.iio_manager = iio_manager

        self.setRenderHint(painter_t.RenderHint.Antialiasing)
        self.setMinimumSize(640, 480)
        self.setSizePolicy(
            wg.QSizePolicy.Policy.MinimumExpanding,
            wg.QSizePolicy.Policy.MinimumExpanding,
        )
        # self.setDragMode(wg.QGraphicsView.ScrollHandDrag) # does not work in conjunction with selectable RectItems
        # self.setAcceptDrops(True)

        self.visual_manager = wg.QGraphicsScene(self)  # type: wg.QGraphicsScene
        cast(pyqtBoundSignal, self.visual_manager.selectionChanged).connect(
            self.AckSelectionChanged
        )

        self.setScene(self.visual_manager)
        self.visual_graph = visual_graph_t(self)

    @property
    def visual_nodes(self) -> iter:
        return iter(
            [
                elm
                for elm in self.visual_manager.items()
                if isinstance(elm, visual_node_t)
            ]
        )

    def AddVisualNodesToGraph(self, visual_nodes: list[visual_node_t], /) -> None:
        """"""
        for visual_node in visual_nodes:
            self.visual_graph.AddVisualNode(visual_node)

    def AddIIContainer(self, iio_container_wgt: wg.QWidget):
        """"""
        self.iio_manager.AddIIContainer(iio_container_wgt)
        # next line is useless since automatically done through
        # setSelected>selectionChanged>AckSelection>ShowInteractiveInputWidgets in __init__
        # self.iio_selector.setCurrentWidget(self.iio_container_wgt)

    def RemoveIIContainer(self, iio_container_wgt: wg.QWidget) -> wg.QWidget:
        """"""
        return self.iio_manager.RemoveIIContainer(iio_container_wgt)

    def AddItem(self, item):
        """"""
        if isinstance(item, visual_node_t):
            self.visual_manager.clearSelection()  # otherwise the newly created visual node replaces the selection
            self.visual_manager.addItem(item)
            self.ensureVisible(item, xMargin=0, yMargin=0)
        else:  # item is a visual link
            self.visual_manager.addItem(item)

    def RemoveItem(self, item):
        self.visual_manager.removeItem(item)

    def AckSelectionChanged(self):
        """"""
        selected_items = self.scene().selectedItems()

        if len(selected_items) == 1:
            self.iio_manager.SwitchToIIContainer(selected_items[0].iio_container_wgt)
        else:
            self.iio_manager.SwitchToIIContainer()

    def wheelEvent(self, event):
        """"""
        original_pos = self.mapToScene(event.pos())

        scale_factor = (
            1 / graph_container_wgt_t.zoom_factor_c
            if event.angleDelta().y() > 0
            else graph_container_wgt_t.zoom_factor_c
        )
        self.scale(scale_factor, scale_factor)

        shift = self.mapToScene(event.pos()) - original_pos
        self.translate(shift.x(), shift.y())
