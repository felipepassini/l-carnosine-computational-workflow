from pathlib import Path

from carnosine_workflow.orca_parser import (
    extract_final_energy,	
    terminated_normally,
    extract_optimization_cycles,
    optimization_converged,
)


FIXTURES = Path(__file__).parent / "fixtures" / "sanitized"

def test_extracts_optimization_cycle_count():
    output_file = FIXTURES / "normal_termination.out"

    assert extract_optimization_cycles(output_file) == 3


def test_returns_none_when_no_optimization_cycles_are_found():
    output_file = FIXTURES / "abnormal_termination.out"

    assert extract_optimization_cycles(output_file) is None

def test_detects_normal_termination():
    output_file = FIXTURES / "normal_termination.out"

    assert terminated_normally(output_file) is True


def test_detects_abnormal_termination():
    output_file = FIXTURES / "abnormal_termination.out"

    assert terminated_normally(output_file) is False


def test_extracts_final_energy():
    output_file = FIXTURES / "normal_termination.out"

    assert extract_final_energy(output_file) == -123.456789


def test_returns_none_when_energy_is_missing():
    output_file = FIXTURES / "abnormal_termination.out"

    assert extract_final_energy(output_file) is None

def test_detects_converged_optimization():
    output_file = FIXTURES / "normal_termination.out"

    assert optimization_converged(output_file) is True


def test_detects_nonconverged_optimization():
    output_file = FIXTURES / "abnormal_termination.out"

    assert optimization_converged(output_file) is False


