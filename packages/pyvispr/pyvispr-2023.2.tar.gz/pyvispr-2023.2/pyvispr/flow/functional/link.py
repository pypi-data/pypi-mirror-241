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

from __future__ import annotations

import dataclasses as dtcl
from enum import Enum as enum_t

from pyvispr.flow.functional.node.main import node_t


@dtcl.dataclass(repr=False, eq=False)
class outbound_links_t(dict[str, list[node_t | None | str]]):
    """
    Per node outbound links.
    """

    class state_e(enum_t):
        non_empty = 0
        empty_for_out = 1
        empty = 2
        as_is = 3

    @classmethod
    def NewForLink(
        cls, output_name: str, node_dst: node_t | None, input_name: str, /
    ) -> outbound_links_t:
        """"""
        output = cls()
        output[output_name] = [node_dst, input_name]
        return output

    @classmethod
    def NewForDict(
        cls, dictionary: dict[str, list[node_t | None | str]], /
    ) -> outbound_links_t:
        """"""
        output = cls()
        output.update(dictionary)
        return output

    @property
    def names(self) -> tuple[str, ...]:
        """"""
        return tuple(self.keys())

    @property
    def successor_nodes(self) -> tuple[node_t, ...]:
        """"""
        output = set()

        for links_per_out in self.values():
            output.update(links_per_out[::2])

        return tuple(output)

    def AddLink(self, output_name: str, node_dst: node_t, input_name: str, /) -> bool:
        """"""
        not_already_present = True

        if output_name in self:
            links_per_out = self[output_name]

            if (node_dst in links_per_out) and (input_name in links_per_out):
                for idx, elm in enumerate(links_per_out):
                    if (elm is node_dst) and (links_per_out[idx + 1] == input_name):
                        not_already_present = False
                        break

            if not_already_present:
                links_per_out.extend([node_dst, input_name])
        else:
            self[output_name] = [node_dst, input_name]

        return not_already_present

    def RemoveLinkIfExists(
        self, output_name: str, node_dst: node_t, input_name: str | None, /
    ) -> outbound_links_t.state_e:
        """"""
        links_per_out = self[output_name]
        links_dst_idc = [
            _idx for _idx, _elm in enumerate(links_per_out) if _elm is node_dst
        ]
        if len(links_dst_idc) == 0:
            return outbound_links_t.state_e.as_is

        if input_name is None:
            for links_dst_idx in reversed(links_dst_idc):
                del links_per_out[links_dst_idx : (links_dst_idx + 2)]
        else:
            for links_dst_idx in links_dst_idc:
                if links_per_out[links_dst_idx + 1] == input_name:
                    del links_per_out[links_dst_idx : (links_dst_idx + 2)]
                    break

        if len(links_per_out) > 0:
            return outbound_links_t.state_e.non_empty

        del self[output_name]
        if len(self) > 0:
            return outbound_links_t.state_e.empty_for_out

        return outbound_links_t.state_e.empty

    def __contains__(self, item: str | node_t | tuple[node_t, str]) -> bool:
        """"""
        if isinstance(item, str):
            return super().__contains__(item)

        if isinstance(item, node_t):
            return any(item in _elm for _elm in self.values())

        node_dst, input_name = item
        for links_per_out in self.values():
            if node_dst in links_per_out:
                link_dst_idc = [
                    _idx for _idx, _elm in enumerate(links_per_out) if _elm is node_dst
                ]
                for l_idx in link_dst_idc:
                    if links_per_out[l_idx + 1] == input_name:
                        return True

        return False

    # --- LINKS SERIALIZATION

    # def CreateIndexedForm(self, nodes: list) -> dict:
    #     """"""
    #     indexed_form = {}
    #
    #     for output_name, links_per_out in self.items():
    #         indexed_links = links_per_out[:]
    #         for idx in range(0, len(indexed_links), 2):
    #             indexed_links[idx] = nodes.index(indexed_links[idx])
    #
    #         indexed_form[output_name] = indexed_links
    #
    #     return indexed_form
    #
    # def ConvertBackFromIndexedForm(self, nodes: list, node_idx_offset=0) -> None:
    #     """"""
    #     for output_name, links_per_out in self.items():
    #         for idx in range(0, len(links_per_out), 2):
    #             links_per_out[idx] = nodes[links_per_out[idx] + node_idx_offset]
