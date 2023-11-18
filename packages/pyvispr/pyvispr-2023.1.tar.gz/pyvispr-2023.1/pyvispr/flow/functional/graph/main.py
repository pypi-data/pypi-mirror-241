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

import dataclasses as dtcl

from pyvispr.flow.functional.graph.observer import dummy_observer_t, observer_p
from pyvispr.flow.functional.link import outbound_links_t
from pyvispr.flow.functional.node.main import node_t


@dtcl.dataclass(repr=False, eq=False)
class graph_t:
    """
    links[idx]: Outbound links of node of index idx in list "nodes":
        - None if node has no outbound links.
        - If not None, dictionary with:
            - key=name of output and...
            - value=list of alternating target nodes and name of target inputs.
    """

    nodes: list[node_t] = dtcl.field(init=False, default_factory=list)
    links: list[outbound_links_t | None] = dtcl.field(init=False, default_factory=list)
    observer: observer_p = dtcl.field(default_factory=dummy_observer_t)

    def AddNode(self, node: node_t, /) -> None:
        """"""
        self.nodes.append(node)
        self.links.append(None)

    def AddLink(
        self, node_src: node_t, output_name: str, node_dst: node_t, input_name: str, /
    ) -> tuple[bool, bool]:
        """"""
        node_src_idx = self.nodes.index(node_src)
        outbound_links = self.links[node_src_idx]

        if outbound_links is None:
            self.links[node_src_idx] = outbound_links_t.NewForLink(
                output_name, node_dst, input_name
            )
            not_already_present = True
        else:
            not_already_present = outbound_links.AddLink(
                output_name, node_dst, input_name
            )

        out_value = node_src.output_states[output_name].value
        is_already_full = out_value is not None

        if not_already_present:
            node_src.SetOutputLinkingState(output_name, True)
            node_dst.SetInputLinkingState(input_name, True)

            if is_already_full:
                node_dst.SetInputValue(input_name, out_value)

            self.InvalidateNodesInCascadeFromNode(node_dst)

        return not_already_present, is_already_full

    def RemoveNode(self, node: node_t, /) -> None:
        """"""
        self.InvalidateNodesInCascadeFromNode(node)

        for node_src in self._PredecessorsOfNode(node):
            node_src_idx = self.nodes.index(node_src)
            outbound_links = self.links[node_src_idx]  # Cannot be None.

            for output_name in outbound_links.names:
                links_state = outbound_links.RemoveLinkIfExists(output_name, node, None)

                if links_state is outbound_links_t.state_e.empty:
                    node_src.SetOutputLinkingState(output_name, False)
                    self.links[node_src_idx] = None
                    break

                if links_state is outbound_links_t.state_e.empty_for_out:
                    node_src.SetOutputLinkingState(output_name, False)

        node_idx = self.nodes.index(node)

        if self.links[node_idx] is not None:
            for links_per_out in self.links[node_idx].values():
                for link_idx in range(0, len(links_per_out), 2):
                    links_per_out[link_idx].SetInputLinkingState(
                        links_per_out[link_idx + 1], False
                    )

        del self.nodes[node_idx]
        del self.links[node_idx]

    def RemoveLink(
        self,
        node_src: node_t,
        output_name: str | None,
        node_dst: node_t,
        input_name: str | None,
        /,
    ) -> None:
        """
        Removes one or several links assuming that the link(s) exist(s).
        """
        self.InvalidateNodesInCascadeFromNode(node_dst)

        # Do not place at end since it will not be called if encountering return below.
        node_dst.SetInputLinkingState(input_name, False)

        node_src_idx = self.nodes.index(node_src)
        outbound_links = self.links[node_src_idx]

        if output_name is None:
            output_names = outbound_links.names
        else:
            output_names = (output_name,)

        for name in output_names:
            links_state = outbound_links.RemoveLinkIfExists(name, node_dst, input_name)

            if links_state is outbound_links_t.state_e.empty:
                node_src.SetOutputLinkingState(name, False)
                self.links[node_src_idx] = None
                return

            if links_state is outbound_links_t.state_e.empty_for_out:
                node_src.SetOutputLinkingState(name, False)

    def ContainsLinkTo(self, node_dst: node_t, input_name: str, /) -> bool:
        """"""
        for links_per_node in self.links:
            if links_per_node is None:
                continue

            if (node_dst, input_name) in links_per_node:
                return True

        return False

    def _SuccessorsOfNode(self, node_src: node_t, /) -> tuple[node_t, ...]:
        """"""
        outbound_links = self.links[self.nodes.index(node_src)]

        if outbound_links is None:
            return ()
        else:
            return outbound_links.successor_nodes

    def _PredecessorsOfNode(
        self, node_dst: node_t, /, *, input_name: str | None = None
    ) -> tuple[node_t, ...]:
        """"""
        output = set()

        for node_src_idx, links_per_node in enumerate(self.links):
            if links_per_node is None:
                continue

            if input_name is None:
                if node_dst in links_per_node:
                    output.add(self.nodes[node_src_idx])
            elif (node_dst, input_name) in links_per_node:
                return (self.nodes[node_src_idx],)

        if input_name is None:
            return tuple(output)

        return ()

    def InvalidateNodesInCascadeFromNode(
        self, origin_node: node_t, /, *, barrier_node: node_t = None
    ) -> None:
        """
        Reasons for invalidating from origin_node:
            - origin_node is about to be deleted
            - some input links have been added or deleted
            - some inputs have been modified
        """
        nodes_to_be_invalidated = [origin_node]
        # Useful only in presence of cycles.
        node_was_invalidated = len(self.nodes) * [False]

        while len(nodes_to_be_invalidated) > 0:
            successors = []
            node_idc = map(
                lambda node_l: self.nodes.index(node_l), nodes_to_be_invalidated
            )

            for node_idx, node in zip(node_idc, nodes_to_be_invalidated):
                if (barrier_node is not None) and (node is barrier_node):
                    continue

                node.InvalidateOutputs(observer=self.observer)
                node_was_invalidated[node_idx] = True

                if self.links[node_idx] is not None:
                    for links_per_out in self.links[node_idx].values():
                        for link_idx in range(0, len(links_per_out), 2):
                            links_per_out[link_idx].InvalidateInputs(
                                name=links_per_out[link_idx + 1]
                            )

                successors.extend(
                    [
                        successor
                        for successor in self._SuccessorsOfNode(node)
                        if (successor not in successors)
                        and (not node_was_invalidated[self.nodes.index(successor)])
                    ]
                )

            nodes_to_be_invalidated = successors

    def InvalidateAllNodes(self) -> None:
        """"""
        for node in self.nodes:
            if not node.needs_running:
                self.InvalidateNodesInCascadeFromNode(node)

            if all(_nde.needs_running for _nde in self.nodes):
                break

    def Run(self, /, *, script_accessor=None) -> None:
        """"""
        unrun_nodes = [node for node in self.nodes if node.needs_running]

        while len(unrun_nodes) > 0:
            runnable_nodes = [node for node in unrun_nodes if node.can_run]
            if len(runnable_nodes) == 0:
                break

            run_again_nodes = []

            for node in runnable_nodes:
                output_names = node.output_names

                if (script_accessor is not None) and (len(output_names) > 0):
                    if len(output_names) > 1:
                        for idx in range(len(output_names) - 1):
                            script_accessor.write(
                                node.UniqueNameWithPostfix(output_names[idx]) + ", "
                            )
                    script_accessor.write(
                        node.UniqueNameWithPostfix(output_names[-1]) + " = "
                    )

                self.observer.AckNodeAboutToRun(node)
                output_values = node.Run(script_accessor=script_accessor)
                self.observer.AckNodeDoneRunning(node)

                if len(output_names) > 1:
                    for idx, name in enumerate(output_names):
                        node.SetOutputValue(
                            name, output_values[idx], observer=self.observer
                        )
                elif len(output_names) > 0:
                    node.SetOutputValue(
                        output_names[0], output_values, observer=self.observer
                    )

                all_out_links = self.links[self.nodes.index(node)]
                if all_out_links is not None:
                    for output_name, per_out_links in all_out_links.items():
                        output_value = node.output_states[output_name].value

                        for idx in range(0, len(per_out_links), 2):
                            next_node = per_out_links[idx]
                            next_in_name = per_out_links[idx + 1]
                            next_node.SetInputValue(next_in_name, output_value)

            unrun_nodes = [node for node in unrun_nodes if node not in runnable_nodes]
            unrun_nodes.extend(run_again_nodes)
