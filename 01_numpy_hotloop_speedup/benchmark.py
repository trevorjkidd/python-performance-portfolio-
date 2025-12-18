import time
import numpy as np
from original import compute_distances as slow
from optimized import compute_distances as fast

n = 5_000_000
x = np.random.rand(n, 2)
y = np.random.rand(n, 2)

# Warmup
slow(x[:1000], y[:1000])
fast(x[:1000], y[:1000])

start = time.perf_counter()
slow(x, y)
t1 = time.perf_counter() - start

start = time.perf_counter()
fast(x, y)
t2 = time.perf_counter() - start

print(f"Original:  {t1:.2f}s")
print(f"Optimized: {t2:.2f}s")
print(f"Speedup:   {t1 / t2:.1f}x")
