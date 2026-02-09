import math

def rotate_image(image, angle_degrees):
    """
    Rotate the image counterclockwise by the given angle
    using nearest neighbor interpolation.
    """
    H = len(image)
    W = len(image[0])

    # Output image initialized with zeros
    output = [[0 for _ in range(W)] for _ in range(H)]

    # Center of the image
    cy = (H - 1) / 2
    cx = (W - 1) / 2

    # Convert angle to radians
    theta = math.radians(angle_degrees)

    cos_t = math.cos(theta)
    sin_t = math.sin(theta)

    # For each output pixel
    for i in range(H):
        for j in range(W):
            # Offset from center
            dy = i - cy
            dx = j - cx

            # Inverse rotation
            src_y = cy + dy * cos_t + dx * sin_t
            src_x = cx - dy * sin_t + dx * cos_t

            # Nearest neighbor
            src_y = int(round(src_y))
            src_x = int(round(src_x))

            # Check bounds
            if 0 <= src_y < H and 0 <= src_x < W:
                output[i][j] = image[src_y][src_x]
            else:
                output[i][j] = 0

    return output
