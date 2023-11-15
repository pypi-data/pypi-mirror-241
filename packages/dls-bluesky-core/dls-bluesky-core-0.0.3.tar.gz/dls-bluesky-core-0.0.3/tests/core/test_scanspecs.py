import re

import pytest
from scanspec.specs import DURATION, Line, Static

from dls_bluesky_core.core.scanspecs import get_constant_duration


def test_single_frame_single_point():
    spec = Static.duration(0.1)
    assert get_constant_duration(spec.calculate()) == 0.1


def test_consistent_points():
    spec = Static.duration(0.1).concat(Static.duration(0.1))
    assert get_constant_duration(spec.calculate()) == 0.1


def test_inconsistent_points():
    spec = Static.duration(0.1).concat(Static.duration(0.2))
    assert get_constant_duration(spec.calculate()) is None


def test_frame_with_multiple_axes():
    spec = Static.duration(0.1).zip(Line.bounded("x", 0, 0, 1))
    frames = spec.calculate()
    assert len(frames) == 1
    assert get_constant_duration(frames) == 0.1


def test_inconsistent_frame_with_multiple_axes():
    spec = (
        Static.duration(0.1)
        .concat(Static.duration(0.2))
        .zip(Line.bounded("x", 0, 0, 2))
    )
    frames = spec.calculate()
    assert len(frames) == 1
    assert get_constant_duration(frames) is None


def test_non_static_spec_duration():
    spec = Line.bounded(DURATION, 0, 0, 3)
    frames = spec.calculate()
    assert len(frames) == 1
    assert get_constant_duration(frames) == 0


def test_multiple_duration_frames():
    spec = (
        Static.duration(0.1)
        .concat(Static.duration(0.2))
        .zip(Line.bounded(DURATION, 0, 0, 2))
    )
    with pytest.raises(
        AssertionError, match=re.escape("Zipping would overwrite axes ['DURATION']")
    ):
        spec.calculate()
    spec = (  # TODO: refactor when https://github.com/dls-controls/scanspec/issues/90
        Static.duration(0.1) * Line.bounded(DURATION, 0, 0, 2)
    )
    frames = spec.calculate()
    assert len(frames) == 2
    assert get_constant_duration(frames) is None
