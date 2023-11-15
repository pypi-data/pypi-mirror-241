from typing import Any, Callable, Generator, Union

from bluesky import Msg
from ophyd_async.core import Device
from scanspec.specs import DURATION

#  'A true "plan", usually the output of a generator function'
MsgGenerator = Generator[Msg, Any, None]
#  'A function that generates a plan'
PlanGenerator = Callable[..., MsgGenerator]
ScannableAxis = Union[Device, DURATION]
