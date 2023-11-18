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
from PyQt6.QtCore import Qt as constant_e
from PyQt6.QtCore import pyqtBoundSignal

# from pyvispr.installer.installer import node_description_wgt_t


class node_help_container_wgt_t(wg.QWidget):
    def __init__(self, parent, close_help_fct):
        """"""
        super().__init__(parent)

        layout = wg.QVBoxLayout(self)
        layout.setAlignment(constant_e.AlignmentFlag.AlignTop)
        layout.setContentsMargins(12, 0, 12, 0)

        # self.setLayout(layout)

        # self.help_wgt = node_description_wgt_t(read_only=True)
        # self.help_wgt.layout().setContentsMargins(0, 0, 0, 0)

        close_btn = wg.QPushButton("Close Help")
        cast(pyqtBoundSignal, close_btn.clicked).connect(close_help_fct)

        # layout.addWidget(self.help_wgt)
        layout.addWidget(close_btn)
