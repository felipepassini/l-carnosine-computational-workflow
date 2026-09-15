from pathlib import Path

from carnosine_workflow.orca_parser import terminated_normally


FIXTURES = Path(__file__).parent / "fixtures" / "sanitized"


def test_detects_normal_termination():
    output_file = FIXTURES / "normal_termination.out"

    assert terminated_normally(output_file) is True


def test_detects_abnormal_termination():
    output_file = FIXTURES / "abnormal_termination.out"

    assert terminated_normally(output_file) is False
