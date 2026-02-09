def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    # Write code here
    H = len(X)
    W = len(X[0])
    # calculate output dimension
    output_height = (H-pool_size)//stride +1
    output_width = (W-pool_size)//stride +1

    output = [[0 for _ in range (output_width)]for _ in range (output_height)]

    # Perform max pooling 
    for i in range(output_height):
        for j in range(output_width):
            start_i = i*stride 
            start_j = j*stride 
            
            window = []
            for x in range(pool_size):
                for y in range(pool_size):
                    window.append(X[start_i+x][start_j+y])

            output[i][j]=max(window)

    return output 
