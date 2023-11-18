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

import PyQt6.QtWidgets as wg


class iio_stacking_wgt_t(wg.QStackedWidget):
    def __init__(self, parent):
        """"""
        super().__init__(parent)

        self.empty_iio_wgt = wg.QLabel(
            "Empty Workflow or\nNo Node Selected or\nSeveral Nodes Selected"
        )
        self.addWidget(self.empty_iio_wgt)

        # self.iio_stacking_wgt.setSizePolicy(wg.QSizePolicy.Maximum, wg.QSizePolicy.MinimumExpanding)

    def AddIIContainer(self, iio_container_wgt: wg.QWidget) -> None:
        """"""
        self.addWidget(iio_container_wgt)

    def RemoveIIContainer(self, iio_container_wgt: wg.QWidget) -> wg.QWidget:
        """"""
        self.removeWidget(iio_container_wgt)
        return self.currentWidget()

    def SwitchToIIContainer(self, iio_container_wgt=None):
        """"""
        if iio_container_wgt is None:
            self.setCurrentWidget(self.empty_iio_wgt)
        elif self.currentWidget() is not iio_container_wgt:
            self.setCurrentWidget(iio_container_wgt)
