from pathlib import Path


NORMAL_TERMINATION_MESSAGE = "ORCA TERMINATED NORMALLY"


def terminated_normally(output_file: str | Path) -> bool:
    """
    Check whether an ORCA output file reports normal termination.

    Parameters
    ----------
    output_file
        Path to an ORCA output file.

    Returns
    -------
    bool
        True if ORCA reports normal termination, otherwise False.
    """
    output_path = Path(output_file)

    text = output_path.read_text(
        encoding="utf-8",
        errors="replace",
    )

    return NORMAL_TERMINATION_MESSAGE in text
