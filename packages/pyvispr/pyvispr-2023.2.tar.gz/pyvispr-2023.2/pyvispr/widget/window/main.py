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

from os.path import dirname as ExtractPathPart
from os.path import expanduser as ExpandTildeBasePath
from typing import cast

import PyQt6.QtWidgets as wg
from PyQt6.QtCore import Qt as constant_e

from pyvispr.flow.visual.link import visual_link_t
from pyvispr.flow.visual.node.main import visual_node_t
from pyvispr.widget.flow.graph_container import graph_container_wgt_t
from pyvispr.widget.general.menu import AddEntryToMenu
from pyvispr.widget.window.node_help import node_help_container_wgt_t
from pyvispr.widget.window.node_iio import iio_stacking_wgt_t
from pyvispr.widget.window.node_list import node_list_wgt_t


class pyflow_wdw_t(wg.QMainWindow):
    workflow_extension = "pyvispr"

    def __init__(self) -> None:
        """"""
        super().__init__()

        home_folder = ExpandTildeBasePath("~")
        self.last_install_from_location = home_folder
        self.last_save_location = home_folder
        self.last_load_location = home_folder
        self.last_save_as_script_location = home_folder

        self.setWindowTitle("pyVispr")

        main_container = wg.QWidget(self)
        main_layout = wg.QHBoxLayout()
        node_list_lyt = wg.QVBoxLayout()
        gh_stacking_wgt_lyt = wg.QVBoxLayout()
        iio_stacking_wgt_lyt = wg.QVBoxLayout()

        node_list_lyt.setAlignment(constant_e.AlignmentFlag.AlignTop)
        gh_stacking_wgt_lyt.setAlignment(constant_e.AlignmentFlag.AlignTop)
        iio_stacking_wgt_lyt.setAlignment(constant_e.AlignmentFlag.AlignTop)

        self.node_help_container_wgt = node_help_container_wgt_t(
            main_container, self.CloseNodeHelp
        )
        self.iio_stacking_wgt = iio_stacking_wgt_t(main_container)
        self.graph_container_wgt = graph_container_wgt_t(
            main_container, self.iio_stacking_wgt
        )
        self.node_list_wgt = node_list_wgt_t(
            None,  # self.node_help_container_wgt.help_wgt,
            self.ShowNodeHelp,
            self.graph_container_wgt.AddVisualNodesToGraph,
        )

        self.gh_stacking_wgt = pyflow_wdw_t.__CreateGraphHelpStackingWidget__(
            main_container, self.graph_container_wgt, self.node_help_container_wgt
        )

        node_list_lyt.addWidget(self.node_list_wgt)
        node_list_lyt.addWidget(self.node_list_wgt.filter_wgt)
        gh_stacking_wgt_lyt.addWidget(self.gh_stacking_wgt)
        iio_stacking_wgt_lyt.addWidget(self.iio_stacking_wgt)

        main_layout.addLayout(node_list_lyt)
        main_layout.addLayout(gh_stacking_wgt_lyt, 3)
        main_layout.addLayout(iio_stacking_wgt_lyt, 1)

        main_container.setLayout(main_layout)
        self.setCentralWidget(main_container)

        # self.statusBar()
        self.__AddMenuBar__(self.graph_container_wgt.visual_graph)

    @staticmethod
    def __CreateGraphHelpStackingWidget__(
        main_container, graph_container_wgt, help_wgt
    ):
        """"""
        gh_stacking_wgt = wg.QStackedWidget(main_container)
        gh_stacking_wgt.addWidget(graph_container_wgt)
        gh_stacking_wgt.addWidget(help_wgt)

        return gh_stacking_wgt

    def __AddMenuBar__(self, visual_graph):
        """"""
        menu_bar = self.menuBar()

        menu = menu_bar.addMenu("py&Flow")
        AddEntryToMenu(menu, self, "Get Info", self.OpenAboutDialog)
        AddEntryToMenu(menu, self, "Configure", self.OpenConfiguration)
        menu.addSeparator()
        AddEntryToMenu(
            menu, self, "&Quit", lambda checked_u: self.close(), shortcut="Ctrl+Q"
        )

        menu = menu_bar.addMenu("&Workflow")
        AddEntryToMenu(
            menu,
            self,
            "&Run",
            lambda _: visual_graph.RunInteractively(),
            shortcut="Ctrl+R",
        )
        menu.addSeparator()
        AddEntryToMenu(menu, self, "&Save", self.SaveWorkflowToFile, shortcut="Ctrl+S")
        AddEntryToMenu(
            menu, self, "L&oad", self.LoadWorkflowFromFile, shortcut="Ctrl+O"
        )
        menu.addSeparator()
        AddEntryToMenu(menu, self, "Save As Script", self.SaveWorkflowAsScript)
        menu.addSeparator()
        submenu = menu.addMenu("Reset...")
        AddEntryToMenu(
            submenu, self, "Now", lambda checked_u: visual_graph.InvalidateAllNodes()
        )
        submenu = menu.addMenu("Clear...")
        AddEntryToMenu(submenu, self, "Now", lambda checked_u: visual_graph.Clear())

        menu = menu_bar.addMenu("&View")
        submenu = menu.addMenu("Show Info Boxes...")
        AddEntryToMenu(
            submenu,
            self,
            "For Nodes (toggle)",
            pyflow_wdw_t.ToggleShowInfoBoxesForNodes,
            checkable=True,
            checked=visual_node_t.should_show_info_boxes,
        )
        AddEntryToMenu(
            submenu,
            self,
            "For Links (toggle)",
            pyflow_wdw_t.ToggleShowInfoBoxesForLinks,
            checkable=True,
            checked=visual_link_t.should_show_info_boxes,
        )
        AddEntryToMenu(
            menu,
            self,
            "Merged Ins/Outs (toggle)",
            self.ToggleMergedInsOutsPresentation,
            checkable=True,
        )

        menu = menu_bar.addMenu("&Catalog")
        AddEntryToMenu(
            menu,
            self,
            "Refresh",
            lambda checked_u: self.node_list_wgt.Reload(),
        )
        # menu.addSeparator()
        # AddEntryToMenu(menu, self, "Install Node:", None, disabled=True)
        # AddEntryToMenu(
        #     menu,
        #     self,
        #     "  From User Code",
        #     lambda checked_u: self.OpenNodeInstaller(False),
        # )
        # AddEntryToMenu(
        #     menu,
        #     self,
        #     "  From System Code",
        #     lambda checked_u: self.OpenNodeInstaller(True),
        # )

    @staticmethod
    def ToggleShowInfoBoxesForNodes(checked: bool) -> None:
        visual_node_t.should_show_info_boxes = checked

    @staticmethod
    def ToggleShowInfoBoxesForLinks(checked: bool) -> None:
        visual_link_t.should_show_info_boxes = checked

    def ToggleMergedInsOutsPresentation(self, checked: bool):
        """"""
        if checked:
            wg.QMessageBox.about(
                cast(wg.QWidget, self), "Merged Ins/Outs", "Merged Ins/Outs: YES\n"
            )
        else:
            wg.QMessageBox.about(
                cast(wg.QWidget, self), "Merged Ins/Outs", "Merged Ins/Outs: NO\n"
            )

    def ShowNodeHelp(self) -> None:
        self.gh_stacking_wgt.setCurrentWidget(self.node_help_container_wgt)

    def CloseNodeHelp(self, _: bool, /) -> None:
        self.gh_stacking_wgt.setCurrentWidget(self.graph_container_wgt)

    def SaveWorkflowToFile(self, _: bool, /):
        """"""
        filename = wg.QFileDialog.getSaveFileName(
            cast(wg.QWidget, self),
            "Save Workflow",
            self.last_save_location,
            "pyVispr Workflows (*." + pyflow_wdw_t.workflow_extension + ")",
        )
        if (filename is None) or (len(filename[0]) == 0):
            return
        filename = filename[0]

        self.last_save_location = ExtractPathPart(filename)
        self.last_load_location = self.last_save_location

        self.graph_container_wgt.visual_graph.SaveToFile(filename)

    def LoadWorkflowFromFile(self, _: bool, /):
        """"""
        filename = wg.QFileDialog.getOpenFileName(
            cast(wg.QWidget, self),
            "Load Workflow",
            self.last_load_location,
            "pyVispr Workflows (*." + pyflow_wdw_t.workflow_extension + ")",
        )
        if (filename is None) or (len(filename[0]) == 0):
            return
        filename = filename[0]

        self.last_load_location = ExtractPathPart(filename)

        n_nodes = len(self.graph_container_wgt.visual_graph.nodes)
        if n_nodes > 0:
            loading_question_wdw = wg.QMessageBox(self)
            loading_question_wdw.setWindowTitle("Loading Options")
            loading_question_wdw.setText(
                "About to load a workflow while the current workflow is not empty\nLoading options are:"
            )
            # merge_option_btn_u = loading_question_wdw.addButton(
            #     "Merge Workflows", wg.QMessageBox.YesRole
            # )
            # del merge_option_btn_u # /!\ why deleting the button? seen in a forum answer???
            replace_option_btn = loading_question_wdw.addButton(
                "Replace Workflow", wg.QMessageBox.ButtonRole.NoRole
            )

            loading_question_wdw.exec()

            if loading_question_wdw.clickedButton() == replace_option_btn:
                node_idx_offset = 0
                self.graph_container_wgt.visual_graph.Clear()
            else:
                node_idx_offset = n_nodes
        else:
            node_idx_offset = 0

        self.graph_container_wgt.visual_graph.LoadFromFile(filename, node_idx_offset)

    def SaveWorkflowAsScript(self, _: bool, /):
        """"""
        filename = wg.QFileDialog.getSaveFileName(
            cast(wg.QWidget, self),
            "Save Workflow as Script",
            self.last_save_as_script_location,
            "Python Scripts (*.py)",
        )
        if (filename is None) or (len(filename[0]) == 0):
            return
        filename = filename[0]

        self.last_save_as_script_location = ExtractPathPart(filename)

        self.graph_container_wgt.visual_graph.SaveAsScript(filename)

    def OpenAboutDialog(self, _: bool, /) -> None:
        """"""
        wg.QMessageBox.about(cast(wg.QWidget, self), "About pyVispr", "pyVispr 2016a\n")

    def OpenConfiguration(self, _: bool, /) -> None:
        """"""
        wg.QMessageBox.about(
            cast(wg.QWidget, self),
            "pyVispr Configuration",
            "No configuration options yet\n",
        )

    # def OpenNodeInstaller(self, module_is_system: bool, /) -> None:
    #     """"""
    #     pass
    # if module_is_system:
    #     module_source = None
    # else:
    #     module_source = wg.QFileDialog.getOpenFileName(
    #         cast(wg.QWidget, self),
    #         "Install Node",
    #         self.last_install_from_location,
    #         "Python Scripts (*.py)",
    #     )
    #     if (module_source is None) or (len(module_source[0]) == 0):
    #         return
    #     module_source = module_source[0]
    #     #
    #     self.last_install_from_location = ExtractPathPart(module_source)
    #
    # wdw = installer_wdw_t(
    #     cast(wg.QWidget, self),
    #     module_source,
    #     self.node_list_wgt.node_names,
    #     catalog_t.catalog_folder,
    # )
    #
    # if wdw.exec() == wg.QDialog.DialogCode.Accepted:
    #     self.node_list_wgt.UpdateFromSource(wdw.dst_filename)
