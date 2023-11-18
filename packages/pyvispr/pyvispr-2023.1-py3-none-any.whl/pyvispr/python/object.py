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

repr_short_format_c = 12
repr_medium_format_c = 24
repr_long_format_c = 45
repr_full_format_c = 0


def GetObjectAddress(obj: object) -> str:
    #
    representation = object.__repr__(obj)
    at_position = representation.index(" at 0x")

    return representation[at_position + 4 : -1]


def ConvertObjectToStr(obj: object, max_length: int = repr_short_format_c) -> str:
    #
    if isinstance(obj, str):
        representation = obj  # type: str
    else:  # which includes None
        representation = str(obj)  # type: str

    if len(representation) > max_length:
        representation = representation[:max_length] + "..."  # type: str

    return representation
