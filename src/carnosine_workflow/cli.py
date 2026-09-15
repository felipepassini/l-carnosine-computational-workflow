import argparse
from pathlib import Path

from carnosine_workflow.orca_parser import (
    strongest_ir_bands,
    summarize_calculation,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="orca-summary",
        description="Summarize objective information from an ORCA output file.",
    )

    parser.add_argument(
        "output_file",
        type=Path,
        help="Path to an ORCA .out file.",
    )

    parser.add_argument(
        "--top-ir",
        type=int,
        default=5,
        help="Number of strongest IR bands to display.",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if not args.output_file.exists():
        parser.error(f"file not found: {args.output_file}")

    summary = summarize_calculation(args.output_file)

    print("ORCA Calculation Summary")
    print("------------------------")
    print(f"Normal termination:       {summary['terminated_normally']}")
    print(f"Optimization converged:   {summary['optimization_converged']}")
    print(f"Final energy (Eh):        {summary['final_energy_hartree']}")
    print(f"Optimization cycles:      {summary['optimization_cycles']}")
    print(f"Imaginary frequencies:    {summary['imaginary_frequencies']}")

    bands = strongest_ir_bands(
        args.output_file,
        top_n=args.top_ir,
    )

    if bands:
        print()
        print(f"Top {len(bands)} IR bands")
        print("------------------------")

        for band in bands:
            print(
                f"Mode {band['mode']:>4} | "
                f"{band['frequency_cm1']:>10.2f} cm^-1 | "
                f"{band['intensity_km_mol']:>10.2f} km/mol"
            )


if __name__ == "__main__":
    main()
