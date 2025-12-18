import numpy as np

def compute_distances(x, y):
    diff = x - y
    return np.sqrt(np.sum(diff * diff, axis=1))


if __name__ == "__main__":
    n = 5_000_000
    x = np.random.rand(n, 2)
    y = np.random.rand(n, 2)

    result = compute_distances(x, y)
    print(result[:5])
