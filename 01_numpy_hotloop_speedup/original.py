import numpy as np

def compute_distances(x, y):
    n = len(x)
    out = np.empty(n, dtype=np.float64)

    for i in range(n):
        dx = x[i, 0] - y[i, 0]
        dy = x[i, 1] - y[i, 1]
        out[i] = np.sqrt(dx * dx + dy * dy)

    return out


if __name__ == "__main__":
    n = 5_000_000
    x = np.random.rand(n, 2)
    y = np.random.rand(n, 2)

    result = compute_distances(x, y)
    print(result[:5])
