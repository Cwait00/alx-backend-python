#!/usr/bin/env python3

from typing import Mapping, Any, Optional

def safely_get_value(dct: Mapping, key: Any, default: Optional[Any] = None) -> Any:
    if key in dct:
        return dct[key]
    else:
        return default
