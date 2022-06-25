def compute_D(N):
    alpha_vect = np.zeros((N, 1))
    D = np.zeros((N, N))

    alpha_vect[0] = N**(-0.5)
    alpha_vect[1:] = N**(-0.5) * math.sqrt(2)

    for k in range(1, N+1):
        for i in range(1, N+1):
            D[k-1, i-1] = alpha_vect[k-1] * math.cos((k-1) * math.pi * (2*i-1) / (2*N))
            
    return D