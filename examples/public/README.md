# Public Examples

This directory contains public demonstration material used to document
and test the computational workflow without exposing unpublished
L-carnosine research data.

## Water Example

The water example contains:

```text
examples/public/
├── inputs/
│   └── water_opt_freq.inp
├── structures/
│   └── water.xyz
└── outputs/
    └── water_demo.out

Structure

structures/water.xyz contains a simple water geometry used only as a
public demonstration structure.

ORCA Input

inputs/water_opt_freq.inp demonstrates the general structure of an ORCA
geometry optimization followed by a vibrational frequency calculation.

The input is intended as a workflow example, not as a universal
recommended computational method.

Demonstration Output

outputs/water_demo.out is a synthetic ORCA-style file.

It was created specifically to demonstrate the parser and command-line
interface and should not be interpreted as the numerical result of
running water_opt_freq.inp.

Its numerical values are illustrative.

Using the CLI

With the project installed in the active Python environment:

orca-summary examples/public/outputs/water_demo.out

The command reports:

normal termination status;
geometry optimization convergence;
final electronic energy;
number of optimization cycles;
number of imaginary frequencies;
strongest IR bands.

Example:

ORCA Calculation Summary
------------------------
Normal termination:       True
Optimization converged:   True
Final energy (Eh):        -75.975
Optimization cycles:      3
Imaginary frequencies:    0

Top 3 IR bands
------------------------
Mode    6 |    1600.00 cm^-1 |      70.00 km/mol
Mode    8 |    3750.00 cm^-1 |      40.00 km/mol
Mode    7 |    3650.00 cm^-1 |      25.00 km/mol
Research Data Policy

No active L-carnosine calculation is included in this example.

Research-specific geometries, ORCA outputs, vibrational results, spectra,
and scientific conclusions remain outside the public example directory
unless explicitly approved for release.