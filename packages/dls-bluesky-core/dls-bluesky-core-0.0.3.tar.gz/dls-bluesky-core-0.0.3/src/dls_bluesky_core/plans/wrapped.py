from typing import Any, List, Mapping, Optional, Union

import bluesky.plans as bp
from bluesky.protocols import Readable

from dls_bluesky_core.core import MsgGenerator

"""
Wrappers for Bluesky built-in plans with type hinting and renamed metadata
"""


def count(
    detectors: List[Readable],
    num: int = 1,
    delay: Optional[Union[float, List[float]]] = None,
    metadata: Optional[Mapping[str, Any]] = None,
) -> MsgGenerator:
    """
    Take `n` readings from a device

    Args:
        detectors (List[Readable]): Readable devices to read
        num (int, optional): Number of readings to take. Defaults to 1.
        delay (Optional[Union[float, List[float]]], optional): Delay between readings.
                                                               Defaults to None.
        metadata (Optional[Mapping[str, Any]], optional): Key-value metadata to include
                                                          in exported data.
                                                          Defaults to None.

    Returns:
        MsgGenerator: _description_

    Yields:
        Iterator[MsgGenerator]: _description_
    """
    plan_args = (
        {  # If bp.count added delay to plan_args, we could remove all md handling
            "detectors": list(map(repr, detectors)),
            "num": num,
            "delay": delay,
        }
    )

    _md = {
        "plan_args": plan_args,
        **(metadata or {}),
    }

    yield from bp.count(detectors, num, delay=delay, md=_md)
