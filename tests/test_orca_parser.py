from pathlib import Path

from carnosine_workflow.orca_parser import (
    count_imaginary_frequencies,
    extract_final_energy,
    extract_ir_spectrum,
    extract_optimization_cycles,
    extract_vibrational_frequencies,
    optimization_converged,
    strongest_ir_bands,
    summarize_calculation,
    terminated_normally,
)


FIXTURES = Path(__file__).parent / "fixtures" / "sanitized"


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


def test_extracts_optimization_cycle_count():
    output_file = FIXTURES / "normal_termination.out"

    assert extract_optimization_cycles(output_file) == 3


def test_returns_none_when_no_optimization_cycles_are_found():
    output_file = FIXTURES / "abnormal_termination.out"

    assert extract_optimization_cycles(output_file) is None


def test_extracts_vibrational_frequencies():
    output_file = FIXTURES / "normal_termination.out"

    frequencies = extract_vibrational_frequencies(output_file)

    assert -83.22 in frequencies
    assert 435.79 in frequencies
    assert 544.50 in frequencies


def test_counts_imaginary_frequencies():
    output_file = FIXTURES / "normal_termination.out"

    assert count_imaginary_frequencies(output_file) == 1


def test_extracts_ir_spectrum():
    output_file = FIXTURES / "normal_termination.out"

    bands = extract_ir_spectrum(output_file)

    assert bands[-1] == {
        "mode": 8,
        "frequency_cm1": 544.50,
        "intensity_km_mol": 25.75,
    }


def test_ranks_strongest_ir_bands():
    output_file = FIXTURES / "normal_termination.out"

    bands = strongest_ir_bands(output_file, top_n=2)

    assert bands[0]["mode"] == 8
    assert bands[1]["mode"] == 7


def test_summarizes_calculation():
    output_file = FIXTURES / "normal_termination.out"

    summary = summarize_calculation(output_file)

    assert summary["terminated_normally"] is True
    assert summary["optimization_converged"] is True
    assert summary["final_energy_hartree"] == -123.456789
    assert summary["optimization_cycles"] == 3
    assert summary["imaginary_frequencies"] == 1

