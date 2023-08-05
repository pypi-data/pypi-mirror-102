"""Tests for the demultiplex flowcell class"""
from pathlib import Path

import pytest
from cg.models.demultiplex.flowcell import Flowcell


def test_get_run_parameters_when_non_existing(fixtures_dir: Path):
    # GIVEN a flowcell object with a directory without run parameters
    flowcell = Flowcell(flowcell_path=fixtures_dir)
    assert flowcell.run_parameters_path.exists() is False

    # WHEN fetching the run parameters object
    with pytest.raises(FileNotFoundError):
        # THEN assert that a FileNotFound error is raised
        flowcell.run_parameters_object
