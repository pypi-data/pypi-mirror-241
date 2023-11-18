# -*- coding: UTF-8 -*-
"""
  Author:  Jacek Kotlarski --<szumak@virthost.pl>
  Created: 01.09.2023

  Purpose: BData container base class.
"""

from inspect import currentframe
from typing import Dict, Optional

from jsktoolbox.attribtool import NoDynamicAttributes
from jsktoolbox.raisetool import Raise


class BClasses(NoDynamicAttributes):
    """Base class for projects."""

    @property
    def _c_name(self) -> str:
        """Return class name."""
        return self.__class__.__name__

    @property
    def _f_name(self) -> str:
        """Return current method name."""
        frame = currentframe().f_back
        method_name = frame.f_code.co_name
        return method_name


class BData(BClasses):
    """BData container class."""

    __data: Optional[Dict] = None

    @property
    def _data(self) -> Dict:
        """Return data dict."""
        if self.__data is None:
            self.__data = {}
        return self.__data

    @_data.setter
    def _data(self, value: Optional[Dict]) -> None:
        """Set data dict."""
        if value is None:
            self.__data = {}
            return
        if isinstance(value, Dict):
            for key in value.keys():
                self.__data[key] = value[key]
        else:
            raise Raise.error(
                f"Expected Dict type, received: '{type(value)}'.",
                AttributeError,
                self._c_name,
                currentframe(),
            )


# #[EOF]#######################################################################
