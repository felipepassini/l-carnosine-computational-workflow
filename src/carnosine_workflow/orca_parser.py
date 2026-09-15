import re
from pathlib import Path

OPTIMIZATION_CONVERGED_MESSAGE = "THE OPTIMIZATION HAS CONVERGED"

NORMAL_TERMINATION_MESSAGE = "ORCA TERMINATED NORMALLY"

FINAL_ENERGY_PATTERN = re.compile(
    r"FINAL SINGLE POINT ENERGY\s+"
    r"([-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][+-]?\d+)?)"
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
    """
    Extract the final electronic energy from an ORCA output.

    If multiple FINAL SINGLE POINT ENERGY entries are present,
    the last one is returned.

    Returns None when no energy entry is found.
    """
    text = read_output(output_file)

    matches = FINAL_ENERGY_PATTERN.findall(text)

    if not matches:
        return None

    return float(matches[-1])


def optimization_converged(output_file: str | Path) -> bool:
    """Check whether an ORCA geometry optimization converged."""
    text = read_output(output_file)

    return OPTIMIZATION_CONVERGED_MESSAGE in text
