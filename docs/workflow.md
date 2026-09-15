# Computational Workflow

## Overview

This project follows a computational workflow designed to keep molecular
model preparation, electronic-structure calculations, validation, and
automated analysis clearly separated.

The current workflow is:

```text
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
