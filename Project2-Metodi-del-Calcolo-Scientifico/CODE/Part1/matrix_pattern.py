for j in range(1, N+1):
    for ell in range(1, N+1):    
        x_val = (2*j-1) / (2*N)
        y_val = (2*ell-1) / (2*N)
        f_mat[j-1, ell-1] = f(x_val, y_val)