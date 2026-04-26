# Data Processing & Scripts

This directory contains the backend logic for data acquisition and profiling.

## Task 2: Data Approach
### 1. Data Profiling
- **Audit:** Checking for temporal completeness from Jan 2015 - March 2026.
- **Identify:** Spotting NASA's `-999` sentinel values across Ethiopia, Kenya, Sudan, Tanzania, and Nigeria.

### 2. Cleaning Strategy
- **Null Handling:** Converting `-999` to `NaN` for accurate mean/median analysis.
- **Normalization:** Ensuring all five countries use consistent units for $T2M_{MAX}$.
- **Feature Engineering:** Creating month/year columns to isolate seasonal patterns for the COP32 report.