import bluesky.plan_stubs as bps
from bluesky.protocols import Flyable

from dls_bluesky_core.core import MsgGenerator, group_uuid


def fly_and_collect(
    flyer: Flyable,
    flush_period: float = 0.5,
    checkpoint_every_collect: bool = False,
    stream_name: str = "primary",
) -> MsgGenerator:
    """Fly and collect a flyer, waiting for collect to finish with a period.

    flyer.kickoff and complete are called, which starts the fly scanning process.
    bps.wait is called, which finishes after each flush period and then repeats, until
    complete finishes. At this point, bps.collect is called to gather the documents
    produced.

    For some flyers, this plan will need to be called in succession in order to, for
    example, set up a flyer to send triggers multiple times and collect data. For such
    a use case, this plan can be setup to checkpoint for each collect.

    Note: this plan must be wrapped with calls to open and close run, and the flyer
    must implement the Collectable protocol. See tests/stubs/test_flyables for an
    example.

    Args:
        flyer (Flyable, Collectable): ophyd-async device which implements Flyable and
                                      Collectable.
        flush_period (float): How often to check if flyer.complete has finished.
                              Defaults to 0.5
        checkpoint_every_collect (bool): whether or not to checkpoint after
                                         flyer.collect has been called. Defaults to
                                         False.
        stream_name (str): name of the stream to collect from. Defaults to "primary".


    Returns:
        MsgGenerator: Plan

    Yields:
        Iterator[MsgGenerator]: Bluesky messages
    """
    yield from bps.kickoff(flyer)
    complete_group = group_uuid("complete")
    yield from bps.complete(flyer, group=complete_group)
    done = False
    while not done:
        try:
            yield from bps.wait(group=complete_group, timeout=flush_period)
        except TimeoutError:
            pass
        else:
            done = True
        yield from bps.collect(
            flyer, stream=True, return_payload=False, name=stream_name
        )
        if checkpoint_every_collect:
            yield from bps.checkpoint()
