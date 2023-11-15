dls-bluesky-core
===========================

|code_ci| |docs_ci| |coverage| |pypi_version| |license|

This module stores Bluesky functionality that is common to multiple techniques or groups within the Diamond Light Source
organisation, such that it can be imported by instances of BlueAPI, or built upon within more focussed plan
repositories to reduce duplication.

The 'plans' package contains functions that describe a full operation which performs an experiment and captures data,
and may wish to be available to instances of BlueAPI to allow common experiment types to be maintained centrally.
The 'stubs' package contains modular partial instructions that may act as a building block for constructing plans, for
which the implementation is common: e.g. querying APIs, standard handling of metadata
The 'tasks' package contains instructions that are not sufficient to run a full experiment but are useful utilities for
providing functionality to instances of BlueAPI: e.g. moving a motor.

============== ==============================================================
PyPI           ``pip install dls-bluesky-core``
Source code    https://github.com/DiamondLightSource/dls-bluesky-core
Documentation  https://DiamondLightSource.github.io/dls-bluesky-core
Releases       https://github.com/DiamondLightSource/dls-bluesky-core/releases
============== ==============================================================

The module built from this repository is intended to either act directly as a source of plans for an instance of
BlueAPI by being a planFunctions source in the config of an instance:

.. code-block:: yaml

    worker:
      env:
        sources:
          - kind: planFunctions
            module: dls_bluesky_core.plans
          - kind: planFunctions
            module: dls_bluesky_core.tasks

Or else contributing functionality that may be common with other plan repositories within Diamond.

.. code-block:: python

    import dls_bluesky_core.stubs  as cps

    def technique_specific_plan(*args, **kwargs):
        yield from cps.common_diamond_setup()

.. |code_ci| image:: https://github.com/DiamondLightSource/dls-bluesky-core/actions/workflows/code.yml/badge.svg?branch=main
    :target: https://github.com/DiamondLightSource/dls-bluesky-core/actions/workflows/code.yml
    :alt: Code CI

.. |docs_ci| image:: https://github.com/DiamondLightSource/dls-bluesky-core/actions/workflows/docs.yml/badge.svg?branch=main
    :target: https://github.com/DiamondLightSource/dls-bluesky-core/actions/workflows/docs.yml
    :alt: Docs CI

.. |coverage| image:: https://codecov.io/gh/DiamondLightSource/dls-bluesky-core/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/DiamondLightSource/dls-bluesky-core
    :alt: Test Coverage

.. |pypi_version| image:: https://img.shields.io/pypi/v/dls-bluesky-core.svg
    :target: https://pypi.org/project/dls-bluesky-core
    :alt: Latest PyPI version

.. |license| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: Apache License

..
    Anything below this line is used when viewing README.rst and will be replaced
    when included in index.rst

See https://DiamondLightSource.github.io/dls-bluesky-core for more detailed documentation.
