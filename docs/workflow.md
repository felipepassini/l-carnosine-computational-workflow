# Computational Workflow

## Overview

This project follows a computational workflow designed to keep molecular
model preparation, electronic-structure calculations, validation, and
automated analysis clearly separated.

The current workflow is:

Molecular structure
        ↓
Avogadro 2
        ↓
Initial geometry preparation
        ↓
ORCA 6 input
        ↓
DFT calculation
        ↓
Geometry optimization
        ↓
Frequency calculation
        ↓
Numerical validation
        ↓
Structural inspection
        ↓
Vibrational analysis
        ↓
Python-based automated analysis

```

## 1. Molecular Structure Preparation

Initial molecular structures may be created, imported, or inspected using
Avogadro 2.

Before running an electronic-structure calculation, the structure should
be checked for:

- expected molecular composition;
- total charge;
- spin multiplicity;
- molecular connectivity;
- intended protonation state;
- obviously incorrect atom positions.

A preliminary molecular-mechanics optimization may be used to generate a
reasonable starting geometry.

The resulting structure is not considered a final quantum-mechanical
geometry.

## 2. ORCA Input Preparation

A typical geometry optimization and vibrational calculation may use an
input similar to:

```text
! B3LYP def2-SVP Opt Freq TightSCF

%geom
  MaxIter 200
end

* xyzfile 0 1 molecule.xyz
```

The exact computational method used for scientific calculations must be
documented for each calculation.

Relevant parameters include:

- density functional;
- basis set;
- optimization settings;
- SCF settings;
- molecular charge;
- spin multiplicity;
- solvent model, when applicable;
- ORCA version.

Templates included in this repository should be treated as examples, not
as universal recommended settings.

## 3. Electronic-Structure Calculation

ORCA performs the requested electronic-structure calculation.

For an optimization followed by a frequency calculation, relevant stages
may include:

```text
SCF calculation
      ↓
Geometry optimization cycle
      ↓
Updated molecular geometry
      ↓
Repeated until convergence
      ↓
Frequency calculation
```

Generated ORCA files may contain both intermediate data and scientific
results.

Most generated research files are therefore excluded from Git by default.

## 4. Numerical Validation

After calculation completion, the workflow should check objective
numerical information such as:

- normal ORCA termination;
- SCF convergence;
- geometry optimization convergence;
- number of optimization cycles;
- final electronic energy;
- successful completion of the frequency calculation;
- number of imaginary frequencies.

Several of these checks are already automated by the Python tools in this
repository.

## 5. Structural Validation

The optimized geometry should then be inspected independently of the
numerical convergence status.

Current visualization tools include:

- Avogadro 2;
- UCSF ChimeraX;
- SEQCROW.

Inspection may include:

- molecular integrity;
- connectivity;
- unexpected atom displacement;
- proton positions;
- bond formation or cleavage;
- relevant bond lengths and angles;
- structural rearrangements during optimization.

This step is essential because a numerically converged calculation may
still produce a structure different from the intended chemical species.

## 6. Vibrational Analysis

When a frequency calculation is available, the workflow may analyze:

- vibrational frequencies;
- imaginary frequencies;
- IR intensities;
- strongest calculated IR bands;
- normal-mode displacement vectors;
- atomic participation in selected modes.

Normal-mode assignments should be treated as scientific interpretations
and should not be automatically considered definitive.

## 7. Python Analysis

Python tools developed in this repository automate repetitive and
objective parts of the workflow.

The current analysis pipeline is:

```text
ORCA output
     ↓
Parser
     ↓
Structured Python data
     ↓
Validation summary
     ↓
Command-line interface
     ↓
Future CSV / tables / plots
```

The current toolkit can extract or determine:

- termination status;
- optimization convergence;
- final electronic energy;
- optimization cycle count;
- vibrational frequencies;
- number of imaginary frequencies;
- IR frequencies and intensities;
- strongest IR bands.

A command-line interface is available through:

```bash
orca-summary calculation.out
```

## 8. Data Separation

Unpublished research calculations are stored outside the Git repository.

The Git repository should contain primarily:

- source code;
- documentation;
- generic templates;
- sanitized examples;
- automated tests;
- approved demonstration material.

Scientific results should only be added after explicit review.

## Current Methodological Direction

The current objective is not to reproduce previous theoretical calculations
numerically using identical computational settings.

Instead, the project aims to update the computational methodology and
evaluate how the resulting predictions compare with previously reported
reference data.

For the zwitterionic form of L-carnosine, the current computational
direction includes the use of an implicit aqueous environment through
CPCM(Water).

The general comparison strategy is therefore:

```text
Reference experimental/theoretical data
              ↓
Updated computational methodology
              ↓
Geometry optimization
              ↓
Vibrational calculation
              ↓
Validation
              ↓
Comparison with reference data

Differences between previous and current calculations should not
automatically be interpreted as errors. They may result from changes in
the computational model, solvent treatment, molecular structure, or other
methodological choices.

Specific numerical results and scientific conclusions from these
comparisons are not included in this repository unless approved for
public release.

## Guiding Principle

The purpose of the workflow is not only to obtain a numerical result.

The objective is to understand, validate, document, and reproduce how
that result was obtained.
