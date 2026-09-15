# Computational Validation

## Purpose

Electronic-structure calculations should not be considered reliable
solely because the software reports numerical convergence.

This project follows a validation workflow that combines numerical,
structural, and physical inspection before a calculation is interpreted.

## Numerical Convergence

For an ORCA calculation, relevant numerical checks may include:

- normal program termination;
- SCF convergence;
- geometry optimization convergence;
- number of optimization cycles;
- convergence of energy and geometry criteria;
- successful completion of the requested frequency calculation.

These checks indicate whether the numerical procedure completed as
expected.

They do not, by themselves, establish that the final molecular structure
represents the intended chemical species.

## Geometry Validation

The optimized structure should also be inspected for chemical and
structural consistency.

Relevant checks may include:

- molecular connectivity;
- unexpected bond formation or cleavage;
- detached atoms or fragments;
- proton positions;
- relevant bond lengths;
- relevant bond angles;
- preservation or change of the intended protonation state;
- major structural rearrangements.

Visualization tools such as Avogadro, UCSF ChimeraX, and SEQCROW may be
used alongside numerical analysis.

## Vibrational Validation

For a geometry intended to represent a local minimum on the potential
energy surface, a frequency calculation provides an additional
validation step.

Relevant checks include:

- successful completion of the frequency calculation;
- number of imaginary frequencies;
- magnitude of any imaginary frequencies;
- visualization of suspicious normal modes when necessary.

A structure with no imaginary frequencies is consistent with a local
minimum within the computational model used.

This does not by itself prove that the structure corresponds to the
experimentally relevant species.

## Chemical Interpretation

Structural and vibrational information must be interpreted in the
context of the computational model.

Factors such as the following may affect the optimized structure:

- initial geometry;
- protonation state;
- total charge;
- spin multiplicity;
- density functional;
- basis set;
- gas-phase versus solvent treatment;
- intermolecular environment.

Scientific interpretation should therefore be separated from automated
validation whenever possible.

## Automation Philosophy

Python tools developed in this repository should primarily report
objective computational information.

For example:

```text
Geometry optimization converged: yes
Normal termination: yes
Imaginary frequencies: 0
Final energy: ...
Optimization cycles: ...
