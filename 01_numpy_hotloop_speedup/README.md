## Problem
The original script was slow due to Python for-loops operating over NumPy arrays,
resulting in high interpreter overhead for large inputs.

## Approach
- Profiled the script to identify the primary hot loop
- Removed Python loops and replaced them with vectorized array operations
- Reduced unnecessary intermediate array creation
- Ensured output remained identical to the original implementation

## Validation
- Outputs match the original implementation
- Verified correctness on both small and large inputs

## Results
- Before: 6.83 seconds
- After:  0.41 seconds
- Speedup: 16.6×
