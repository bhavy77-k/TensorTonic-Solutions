import math

def sobel_edges(image):
    """
    Apply Sobel operator to detect edges.
    Zero-padding is used.
    """
    H = len(image)
    W = len(image[0])

    # Sobel kernels (standard definition)
    Kx = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]

    Ky = [
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ]

    # Pad image with zeros
    padded = [[0]*(W+2) for _ in range(H+2)]
    for i in range(H):
        for j in range(W):
            padded[i+1][j+1] = image[i][j]

    # Output edges
    edges = [[0 for _ in range(W)] for _ in range(H)]

    # Convolve
    for i in range(H):
        for j in range(W):
            gx = 0
            gy = 0
            for m in range(3):
                for n in range(3):
                    px = padded[i+m][j+n]
                    gx += px * Kx[m][n]
                    gy += px * Ky[m][n]
            edges[i][j] = math.sqrt(gx**2 + gy**2)

    return edges
