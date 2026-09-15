from pathlib import Path

import matplotlib.pyplot as plt

from carnosine_workflow.orca_parser import extract_ir_spectrum


OUTPUT_FILE = Path("examples/public/outputs/water_demo.out")
FIGURE_FILE = Path("figures/demo/water_ir_demo.png")


def main() -> None:
    bands = extract_ir_spectrum(OUTPUT_FILE)

    frequencies = [band["frequency_cm1"] for band in bands]
    intensities = [band["intensity_km_mol"] for band in bands]

    plt.figure(figsize=(10, 4))

    for frequency, intensity in zip(frequencies, intensities):
        plt.vlines(frequency, 0, intensity)
        plt.text(
            frequency,
            intensity + 1,
            f"{frequency:.0f}",
            ha="center",
            va="bottom",
            fontsize=8,
        )

    plt.xlabel("Wavenumber (cm$^{-1}$)")
    plt.ylabel("Intensity (km/mol)")
    plt.title("Synthetic IR Spectrum Demo: Water Example")

    plt.ylim(0, max(intensities) + 10)

    plt.tight_layout()
    plt.savefig(FIGURE_FILE, dpi=200)
    plt.close()

    print(f"Saved figure to: {FIGURE_FILE}")


if __name__ == "__main__":
    main()