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

from types import ModuleType as module_t


class ii_manager_t:  # ii: interactive input
    constructor_name_c = "CreateIIWidget"
    getter_name_c = "GetIIValue"
    setter_name_c = "SetIIValue"

    def __init__(self, module: module_t, /) -> None:
        """"""
        self.RunConstructor = None
        self.RunGetter = None
        self.RunSetter = None

        try:
            self.RunConstructor = getattr(module, ii_manager_t.constructor_name_c)
            self.RunGetter = getattr(module, ii_manager_t.getter_name_c)
            self.RunSetter = getattr(module, ii_manager_t.setter_name_c)
        except:
            if any([self.RunConstructor, self.RunGetter, self.RunSetter]):
                print(
                    "Unsuccessful module import(s) in ii_manager_t instanciation",
                    module,
                    self.RunConstructor,
                    self.RunGetter,
                    self.RunSetter,
                )
                self.RunConstructor = None
                self.RunGetter = None
                self.RunSetter = None
