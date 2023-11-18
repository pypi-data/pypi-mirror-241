"""Helper functions for testing.
"""
import torch
import re
import plenoptic as po
import pyrtools as pt
import numpy as np
from test_models import TestPortillaSimoncelli, get_portilla_simoncelli_synthesize_filename
from test_metric import osf_download
from conftest import DEVICE


def update_ps_synthesis_test_file():
    """Create new test file for test_models.test_ps_synthesis().

    We cannot guarantee perfect reproducibility across pytorch versions, but we
    can guarantee it within versions. Therefore, we need to periodically create
    new files to test our synthesis outputs against. This helper function does
    that, but note that you NEED to examine the resulting metamer manually to
    ensure it still looks good.

    After generating this file and checking it looks good, upload it to the OSF
    plenoptic-files project: https://osf.io/ts37w/files/osfstorage

    Returns
    -------
    met : po.synth.Metamer
        Metamer object for inspection

    """
    # for now, we want to compare against the one that worked for pytorch version 1.11
    ps_synth_file = osf_download(get_portilla_simoncelli_synthesize_filename('1.11'))
    print(f'Loading from {ps_synth_file}')

    with np.load(ps_synth_file) as f:
        im = f['im']
        im_init = f['im_init']
        im_synth = f['im_synth']
        rep_synth = f['rep_synth']

    met = TestPortillaSimoncelli().test_ps_synthesis(ps_synth_file, False)

    torch_v = torch.__version__.split('+')[0]
    file_name_parts = re.findall('(.*portilla_simoncelli_synthesize)(_gpu)?(_torch_v)?([0-9.]*).npz',
                                 ps_synth_file)[0]
    output_file_name = ''.join(file_name_parts[:2]) + f'_torch_v{torch_v}.npz'
    output = po.to_numpy(met.synthesized_signal).squeeze()
    rep = po.to_numpy(met.model(met.synthesized_signal)).squeeze()
    try:
        np.testing.assert_allclose(output, im_synth.squeeze(), rtol=1e-4, atol=1e-4)
        np.testing.assert_allclose(rep, rep_synth.squeeze(), rtol=1e-4, atol=1e-4)
        print("Current synthesis same as saved version, so not saving current synthesis.")
    # only do all this if the tests would've failed
    except AssertionError:
        print(f"Saving at {output_file_name}")
        np.savez(output_file_name, im=im, im_init=im_init, im_synth=output,
                 rep_synth=rep)
        fig = pt.imshow([output, im_synth.squeeze()],
                        title=[f'New metamer (torch {torch_v})',
                               'Old metamer'])
        fig.savefig(output_file_name.replace('.npz', '.png'))
    return met
