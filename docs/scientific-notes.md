# Scientific and Technical Notes

## Purpose

This document records general scientific and computational lessons learned
during development of the workflow.

It should not contain unpublished numerical research results, confidential
structures, or conclusions that have not been approved for public release.

## Numerical Convergence and Chemical Validity

One of the first important lessons from the project was that numerical
convergence does not necessarily imply chemical validity.

A geometry optimization can satisfy the numerical convergence criteria
while producing a molecular structure different from the chemical species
that was originally intended.

For this reason, computational validation should combine:

- numerical convergence checks;
- molecular visualization;
- structural inspection;
- vibrational analysis;
- physical and chemical reasoning.

## Automated Analysis vs Scientific Interpretation

Automation is most reliable when applied to objective quantities.

Examples include:

- whether ORCA terminated normally;
- whether the optimizer reported convergence;
- final electronic energy;
- number of optimization cycles;
- vibrational frequencies;
- IR intensities;
- number of imaginary frequencies.

Higher-level conclusions should not be inferred automatically without
additional scientific analysis.

For example, a script should not independently declare that a structure is
the correct protonation state, biologically relevant configuration, or
experimentally observed species.

## Reproducibility

A useful computational result should eventually be accompanied by enough
information to understand how it was obtained.

Relevant metadata may include:

- software version;
- density functional;
- basis set;
- charge;
- multiplicity;
- solvent treatment;
- optimization settings;
- initial geometry;
- convergence criteria.

Future versions of the toolkit may automate the extraction of part of this
metadata.

## Testing Scientific Software

The parser is developed using synthetic ORCA outputs rather than active
research calculations.

This allows parser behavior to be tested reproducibly without publishing
unreleased scientific data.

Automated tests also provide protection against accidentally breaking
previously working analysis functions as the code evolves.

## Methodological Update vs Numerical Reproduction

An important distinction in the current research direction is that the
goal is not necessarily to reproduce older theoretical calculations
numerically.

The purpose of revisiting previous calculations is to apply an updated
computational methodology and compare the resulting predictions with
reference data.

For the zwitterionic form currently under investigation, the methodology
includes implicit aqueous solvation using CPCM(Water).

Consequently, differences between older and newer calculations are not,
by themselves, evidence of an incorrect calculation.

They must be interpreted in light of methodological differences such as:

- solvation treatment;
- initial molecular geometry;
- protonation state;
- density functional;
- basis set;
- optimization procedure;
- other computational settings.

The relevant scientific question is therefore not simply whether two
calculations produce identical numerical values, but whether the updated
model provides a physically meaningful description and how its predictions
compare with the available reference data.
