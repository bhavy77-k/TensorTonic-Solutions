def gaussian_kernel(size, sigma):
    """
    Generate a normalized 2D Gaussian blur kernel.
    """
    # Write code here
    center = size//2
    kernel = [[0 for _ in range(size)]for _ in range(size)]
    total = 0.0 
    for i in range(size):
        for j in range(size):
            x = j-center 
            y = i-center
            value = math.exp(-(x**2 + y**2)/(2*sigma**2))
            kernel[i][j] = value 
            total += value 
    for i in range (size):
        for j in range(size):
            kernel[i][j]/=total 
    return kernel 
