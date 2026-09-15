import re
from pathlib import Path


NORMAL_TERMINATION_MESSAGE = "ORCA TERMINATED NORMALLY"
OPTIMIZATION_CONVERGED_MESSAGE = "THE OPTIMIZATION HAS CONVERGED"

FINAL_ENERGY_PATTERN = re.compile(
    r"FINAL SINGLE POINT ENERGY\s+"
    r"([-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][+-]?\d+)?)"
)

OPTIMIZATION_CYCLE_PATTERN = re.compile(
    r"GEOMETRY OPTIMIZATION CYCLE\s+(\d+)"
)

VIBRATIONAL_FREQUENCY_PATTERN = re.compile(
    r"^\s*\d+:\s+"
    r"([-+]?(?:\d+(?:\.\d*)?|\.\d+))\s+cm\*\*-1",
    re.MULTILINE,
)

IR_LINE_PATTERN = re.compile(
    r"^\s*(\d+):\s+"
    r"([-+]?(?:\d+(?:\.\d*)?|\.\d+))\s+"
    r"([-+]?(?:\d+(?:\.\d*)?|\.\d+))\s+"
    r"([-+]?(?:\d+(?:\.\d*)?|\.\d+))",
    re.MULTILINE,
)


def read_output(output_file: str | Path) -> str:
    """Read an ORCA output file."""
    output_path = Path(output_file)

    return output_path.read_text(
        encoding="utf-8",
        errors="replace",
    )


def terminated_normally(output_file: str | Path) -> bool:
    """Check whether an ORCA output reports normal termination."""
    text = read_output(output_file)

    return NORMAL_TERMINATION_MESSAGE in text


def extract_final_energy(output_file: str | Path) -> float | None:
    """Extract the last FINAL SINGLE POINT ENERGY from an ORCA output."""
    text = read_output(output_file)

    matches = FINAL_ENERGY_PATTERN.findall(text)

    if not matches:
        return None

    return float(matches[-1])


def optimization_converged(output_file: str | Path) -> bool:
    """Check whether an ORCA geometry optimization converged."""
    text = read_output(output_file)

    return OPTIMIZATION_CONVERGED_MESSAGE in text


def extract_optimization_cycles(output_file: str | Path) -> int | None:
    """Extract the number of geometry optimization cycles."""
    text = read_output(output_file)

    cycles = OPTIMIZATION_CYCLE_PATTERN.findall(text)

    if not cycles:
        return None

    return max(int(cycle) for cycle in cycles)


def extract_vibrational_frequencies(
    output_file: str | Path,
) -> list[float]:
    """Extract vibrational frequencies in cm^-1."""
    text = read_output(output_file)

    return [
        float(value)
        for value in VIBRATIONAL_FREQUENCY_PATTERN.findall(text)
    ]


def count_imaginary_frequencies(output_file: str | Path) -> int:
    """Count negative vibrational frequencies."""
    frequencies = extract_vibrational_frequencies(output_file)

    return sum(frequency < 0 for frequency in frequencies)


def extract_ir_spectrum(output_file: str | Path) -> list[dict]:
    """
    Extract mode number, frequency and IR intensity.

    IR intensity is reported by ORCA in km/mol.
    """
    text = read_output(output_file)

    marker = "IR SPECTRUM"

    if marker not in text:
        return []

    ir_section = text.split(marker, 1)[1]

    bands = []

    for mode, frequency, _eps, intensity in IR_LINE_PATTERN.findall(
        ir_section
    ):
        bands.append(
            {
                "mode": int(mode),
                "frequency_cm1": float(frequency),
                "intensity_km_mol": float(intensity),
            }
        )

    return bands


def strongest_ir_bands(
    output_file: str | Path,
    top_n: int = 5,
) -> list[dict]:
    """Return the strongest calculated IR bands."""
    bands = extract_ir_spectrum(output_file)

    return sorted(
        bands,
        key=lambda band: band["intensity_km_mol"],
        reverse=True,
    )[:top_n]


def summarize_calculation(output_file: str | Path) -> dict:
    """Return a compact objective summary of an ORCA calculation."""
    return {
        "terminated_normally": terminated_normally(output_file),
        "optimization_converged": optimization_converged(output_file),
        "final_energy_hartree": extract_final_energy(output_file),
        "optimization_cycles": extract_optimization_cycles(output_file),
        "imaginary_frequencies": count_imaginary_frequencies(output_file),
    }

