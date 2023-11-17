"""Tests for basic plugin functionality.
Here we test that fsleyes loads without error when the plugin is present.
We also test that it loads with the default mrs layout.
"""

from pathlib import Path
from subprocess import check_call

# Data paths
test_data_path = Path(__file__).parent / 'test_data'
t1 = test_data_path / 'T1.nii.gz'
svs = test_data_path / 'metab.nii.gz'


def test_load(tmp_path):
    assert not check_call(['render',
                           '-of', tmp_path / 'test.png',
                           str(t1),
                           str(svs)])


def test_load_mrs_layout(tmp_path):
    assert not check_call(['render',
                           '-of', tmp_path / 'test.png',
                           '-smrs',
                           str(t1),
                           str(svs)])
