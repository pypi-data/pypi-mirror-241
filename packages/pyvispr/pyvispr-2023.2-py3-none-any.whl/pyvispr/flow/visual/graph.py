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

import typing as h

from pyvispr.flow.descriptive.node import node_t as node_description_t
from pyvispr.flow.functional.graph.main import graph_t
from pyvispr.flow.functional.node.main import node_t
from pyvispr.flow.functional.node.state import output_state_t
from pyvispr.flow.visual.link import visual_link_t
from pyvispr.flow.visual.node.main import next_run_brush_needs_c, visual_node_t
from pyvispr.python.object import ConvertObjectToStr, repr_long_format_c


class visual_graph_t(graph_t):
    def __init__(self, graph_manager: h.Any, /) -> None:
        """"""
        super().__init__(observer=self)

        self.visual_manager = graph_manager
        # Note: Visual_nodes are not explicitly remembered.
        # They can be accessed through the visual_nodes property.
        self.visual_links = []

    # --- VISUAL GRAPH PROPERTIES

    @property
    def visual_nodes(self) -> iter:
        return self.visual_manager.visual_nodes

    def visual_node_of_node(self, node: node_t) -> visual_node_t:
        """"""
        for visual_node in self.visual_nodes:
            if visual_node.node is node:
                return visual_node

        raise ValueError(
            repr(self) + ": no visual node corresponding to node: " + repr(node)
        )

    # --- VISUAL GRAPH MODIFICATIONS

    def AddVisualNode(self, visual_node) -> None:
        """"""
        self.AddNode(visual_node.node)

        visual_node.InstantiateIIOContainerWidget(parent_graph=self)

        self.visual_manager.AddIIContainer(visual_node.iio_container_wgt)
        self.visual_manager.AddItem(visual_node)

    def AddVisualLink(self, visual_node_1, output_name, visual_node_2, input_name):
        """"""
        (not_already_present, is_already_full) = self.AddLink(
            visual_node_1.node, output_name, visual_node_2.node, input_name
        )
        if not_already_present:
            for visual_link in self.visual_links:
                if (visual_link.visual_node_o is visual_node_1) and (
                    visual_link.visual_node_d is visual_node_2
                ):
                    return

            visual_link = visual_link_t(
                self,
                visual_node_1,
                visual_node_1.output_anchor_coordinates,
                visual_node_2,
                visual_node_2.input_anchor_coordinates,
                is_already_full=is_already_full,
            )
            self.visual_links.append(visual_link)
            self.visual_manager.AddItem(visual_link)

    def RemoveVisualNode(self, visual_node: visual_node_t) -> None:
        """"""
        self.RemoveNode(visual_node.node)

        adjacent_link_idc = []
        for idx, visual_link in enumerate(self.visual_links):
            if (visual_node is visual_link.visual_node_o) or (
                visual_node is visual_link.visual_node_d
            ):
                self.visual_manager.RemoveItem(visual_link)
                adjacent_link_idc.append(idx)

        for idx in reversed(adjacent_link_idc):
            del self.visual_links[idx]

        self.visual_manager.RemoveItem(visual_node)
        newly_selected = self.visual_manager.RemoveIIContainer(
            visual_node.iio_container_wgt
        )

        if newly_selected != 0:
            for visual_node_l in self.visual_nodes:
                if visual_node_l.iio_container_wgt == newly_selected:
                    visual_node_l.setSelected(True)
                    break

    def RemoveVisualLink(self, visual_link, links_out_in, no_links_will_remain):
        """"""
        if links_out_in is None:
            self.RemoveLink(
                visual_link.visual_node_o.node,
                None,
                visual_link.visual_node_d.node,
                None,
            )
        else:
            self.RemoveLink(
                visual_link.visual_node_o.node,
                links_out_in[0],
                visual_link.visual_node_d.node,
                links_out_in[1],
            )

        if no_links_will_remain:
            self.visual_links.remove(visual_link)
            self.visual_manager.RemoveItem(visual_link)

    def Clear(self):
        """"""
        for visual_node in self.visual_nodes:
            self.RemoveVisualNode(visual_node)

    # --- VISUAL GRAPH INTERACTIONS

    def RunInteractively(self, script_accessor=None):
        """"""
        if script_accessor is not None:
            # note: wait until all the nodes have a valid ID before setting feeding output names below
            for node_idx, node in enumerate(self.nodes):
                node.id = node_idx

            for node_idx, links_per_node in enumerate(self.links):
                back_node = self.nodes[node_idx]
                for output_name, links_per_out in links_per_node.items():
                    for link_idx in range(0, len(links_per_out), 2):
                        links_per_out[link_idx].SetInputSource(
                            links_per_out[link_idx + 1], back_node, output_name
                        )

        for visual_node in self.visual_nodes:
            node = visual_node.node

            for input_name in node.input_names:
                if (
                    node.inputs[input_name].assignment
                    is not node_description_t.assignment_e.link
                ) and not self.ContainsLinkTo(node, input_name):
                    value = visual_node.interactive_inputs[input_name].value

                    if value is not None:
                        node.SetInputValue(input_name, value)
                        if script_accessor is not None:
                            # Fake self-backlink (since is not linked).
                            node.SetInputSource(input_name, node, input_name)
                            script_accessor.write(
                                f"{node.SourceOutputOfInput(input_name)} = {value}\n"
                            )

        super().Run(script_accessor=script_accessor)

        for visual_node in self.visual_nodes:
            for idx, output_name in enumerate(visual_node.output_names):
                output_value = visual_node.node.output_states[output_name].value

                if output_value is not output_state_t.VALUE_NOT_SET:
                    visual_node.output_widgets[idx].setText(
                        ConvertObjectToStr(output_value, max_length=repr_long_format_c)
                    )

                    if script_accessor is not None:
                        variable_name = visual_node.UniqueNameWithPostfix(output_name)
                        script_accessor.write(
                            f"# print('{variable_name} =', {variable_name})\n"
                        )
                        # /!\ replace print with save for default python type

    def SaveToFile(self, filename: str):
        """"""
        pass

    def LoadFromFile(self, filename: str, node_idx_offset: int):
        """"""
        pass

    def SaveAsScript(self, filename: str):
        """"""
        pass

    # --- VISUAL GRAPH EVENT HANDLERS

    def AckOutputGotValue(self, node, output_name):
        """"""
        self._AckOutputValueChanged(node, output_name, True)

    def AckOutputLostValue(self, node, output_name):
        """"""
        self._AckOutputValueChanged(node, output_name, False)

    def _AckOutputValueChanged(self, node, output_name, value_is_now_set):
        """"""
        if not value_is_now_set:
            self.visual_node_of_node(node).next_run_btn.setBrush(next_run_brush_needs_c)

        if output_name is None:  # /!\ in which context does this happen?
            return

        node_idx = self.nodes.index(node)

        if (self.links[node_idx] is not None) and (output_name in self.links[node_idx]):
            destination_nodes = self.links[node_idx][output_name]
            destination_nodes = destination_nodes[::2]

            for visual_link in self.visual_links:
                if (visual_link.visual_node_o.node is node) and (
                    visual_link.visual_node_d.node in destination_nodes
                ):
                    visual_link.ChangeAppearanceToFull(value_is_now_set)

    def AckNodeAboutToRun(self, node) -> None:
        """"""
        self.visual_node_of_node(node).ChangeAppearanceToRunning(True)

    def AckNodeDoneRunning(self, node) -> None:
        """"""
        self.visual_node_of_node(node).ChangeAppearanceToRunning(False)
