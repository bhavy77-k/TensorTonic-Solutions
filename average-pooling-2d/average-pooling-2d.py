def average_pooling_2d(X, pool_size):
    """
    Apply 2D average pooling with non-overlapping windows.
    X: 2D list (H x W)
    pool_size: int, size of the pooling window
    Returns: 2D list of pooled output
    """
    H = len(X)
    W = len(X[0])
    stride = pool_size

    out_h = H // pool_size
    out_w = W // pool_size

    output = [[0 for _ in range(out_w)] for _ in range(out_h)]

    for i in range(out_h):
        for j in range(out_w):
            # Compute the sum of the current pooling window
            window_sum = 0
            for m in range(pool_size):
                for n in range(pool_size):
                    window_sum += X[i*stride + m][j*stride + n]
            # Compute average
            output[i][j] = window_sum / (pool_size * pool_size)

    return output
