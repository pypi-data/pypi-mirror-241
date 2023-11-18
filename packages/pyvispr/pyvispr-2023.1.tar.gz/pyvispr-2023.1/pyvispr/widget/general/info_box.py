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

from PyQt6.QtCore import QPointF, QRectF, QTimer, pyqtBoundSignal
from PyQt6.QtGui import QBrush, QColor, QCursor
from PyQt6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem


class info_box_manager_t:
    delay_before_display_c = 500
    delay_before_unplay_c = 1000

    info_box_background_c = QBrush(QColor(255, 255, 153, 192))
    info_box_font_color_c = QColor(0, 0, 0, 192)

    def __init__(self, source_obj, shift, visual_items_manager):
        """"""
        self.source_obj = source_obj
        self.shift = shift
        self.visual_items_manager = visual_items_manager
        self.should_still_display_box = True

        self.timer_u = __CreateAndLaunchSingleShotTimer__(
            info_box_manager_t.delay_before_display_c, self.__ShowInfoBoxIfAppropriate__
        )

    def __ShowInfoBoxIfAppropriate__(self):
        """"""
        if self.should_still_display_box:
            info_box = info_box_wgt_t(self, self.source_obj.info_text, self.shift)
            self.visual_items_manager.AddItem(info_box)

    def AckNotNeededAnymore(self, child):
        self.visual_items_manager.RemoveItem(child)


class info_box_wgt_t(QGraphicsRectItem):
    def __init__(self, manager, text: str, shift) -> None:
        """"""
        super().__init__()

        self.setBrush(info_box_manager_t.info_box_background_c)

        self.manager = manager

        label = QGraphicsTextItem(text, self)
        label.setDefaultTextColor(info_box_manager_t.info_box_font_color_c)

        label_size = label.boundingRect().size()
        self.setRect(QRectF(0, 0, label_size.width(), label_size.height()))
        self.setPos(
            QCursor.pos()
            + shift
            - QPointF(label_size.width() / 2, label_size.height() / 2)
        )

        self.timer_u = __CreateAndLaunchSingleShotTimer__(
            info_box_manager_t.delay_before_unplay_c, self.__AckTimerTimeOut__
        )

    def __AckTimerTimeOut__(self):
        """"""
        if self.isUnderMouse():
            self.timer_u = __CreateAndLaunchSingleShotTimer__(
                info_box_manager_t.delay_before_unplay_c, self.__AckTimerTimeOut__
            )
        else:
            self.manager.AckNotNeededAnymore(self)


def __CreateAndLaunchSingleShotTimer__(delay, timeout_function):
    #
    timer = QTimer()
    timer.setSingleShot(True)
    cast(pyqtBoundSignal, timer.timeout).connect(timeout_function)
    timer.start(delay)

    return timer
