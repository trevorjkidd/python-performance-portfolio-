## Problem
The original script was slow due to Python for-loops operating over NumPy arrays,
resulting in high interpreter overhead for large inputs.

## Approach
- Profiled the script to identify the primary hot loop
- Removed Python loops and replaced them with vectorized array operations
- Reduced unnecessary intermediate array creation
- Ensured output remained identical to the original implementation

## Results
- Before: ~XX.X seconds
- After:  ~X.X seconds
- Speedup: ~X× (input-size dependent)

## Validation
- Outputs match the original implementation
- Verified correctness on both small and large inputs
