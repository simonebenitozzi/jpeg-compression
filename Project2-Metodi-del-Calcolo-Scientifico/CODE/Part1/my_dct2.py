def my_dct2(f_mat):
    N = len(f_mat)      #number of rows and columns
    D = compute_D(N)
    c_mat = f_mat

    # DCT1 for columns
    for j in range(N):
        c_mat[:,j] = np.dot(D, c_mat[:,j])

    # DCT1 for rows
    for j in range(N):
        c_mat[j,:] = np.transpose(np.dot(D, np.transpose(c_mat[j,:])))

    return c_mat