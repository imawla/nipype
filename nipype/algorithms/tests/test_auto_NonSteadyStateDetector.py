# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..confounds import NonSteadyStateDetector


def test_NonSteadyStateDetector_inputs():
    input_map = dict(
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(mandatory=True, ),
    )
    inputs = NonSteadyStateDetector.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_NonSteadyStateDetector_outputs():
    output_map = dict(n_volumes_to_discard=dict(), )
    outputs = NonSteadyStateDetector.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
