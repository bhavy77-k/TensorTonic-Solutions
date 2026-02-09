def conv2d(image, kernel, stride=1, padding=0):
    """
    Apply 2D convolution to a single-channel image.
    image: 2D list of size H x W
    kernel: 2D list of size kH x kW
    stride: int, default=1
    padding: int, default=0
    Returns: 2D list of convolved image
    """
    import copy

    H = len(image)
    W = len(image[0])
    kH = len(kernel)
    kW = len(kernel[0])

    # Pad the image
    if padding > 0:
        padded = [[0]*(W + 2*padding) for _ in range(H + 2*padding)]
        for i in range(H):
            for j in range(W):
                padded[i+padding][j+padding] = image[i][j]
    else:
        padded = copy.deepcopy(image)

    H_p, W_p = len(padded), len(padded[0])

    # Output dimensions
    out_h = (H_p - kH)//stride + 1
    out_w = (W_p - kW)//stride + 1

    output = [[0 for _ in range(out_w)] for _ in range(out_h)]

    # Perform convolution
    for i in range(out_h):
        for j in range(out_w):
            conv_sum = 0
            for m in range(kH):
                for n in range(kW):
                    conv_sum += padded[i*stride + m][j*stride + n] * kernel[m][n]
            output[i][j] = conv_sum

    return output
