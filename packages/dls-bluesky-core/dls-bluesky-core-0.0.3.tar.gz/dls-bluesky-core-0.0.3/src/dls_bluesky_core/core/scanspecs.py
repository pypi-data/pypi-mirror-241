from typing import List, Optional

import numpy as np
from scanspec.core import Frames
from scanspec.specs import DURATION


def get_constant_duration(frames: List[Frames]) -> Optional[float]:
    """
    Returns the duration of a number of ScanSpec frames, if known and consistent.

    Args:
        frames (List[Frames]): A number of Frame objects

    Returns:
        duration (float): if all frames have a consistent duration
        None: otherwise

    """
    duration_frame = [
        f for f in frames if DURATION in f.axes() and len(f.midpoints[DURATION])
    ]
    if len(duration_frame) != 1:
        # Either no frame has DURATION axis,
        #   the frame with a DURATION axis has 0 points,
        #   or multiple frames have DURATION axis
        return None
    durations = duration_frame[0].midpoints[DURATION]
    first_duration = durations[0]
    if np.any(durations != first_duration):
        # Not all durations are the same
        return None
    return first_duration
