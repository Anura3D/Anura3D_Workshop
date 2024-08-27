import numpy as np
import matplotlib.pyplot as plt

def terzaghi_settlement_solution(LayerDepth, TractionLoad, NondimensionalTime, YoungsModulus, PoissonRatio, tolerance=1e-10, max_iterations=30): 
    """
    Calculate the convergent values of UU with Fourier series until convergence is achieved.

    Parameters:
    - DataPoints: Number of points in the depth array.
    - LayerDepth: Depth of the layer.
    - TractionLoad: Traction load for normalization.
    - Compressibility: Compressibility value.
    - NondimensionalTime: Array of non-dimensional times.
    - tolerance: Convergence tolerance.
    - max_iterations: Maximum number of iterations for convergence.

    Returns:
    - UU: The convergent array of values.
    """


    OedometricModulus = YoungsModulus * (1 - PoissonRatio) / ((1 + PoissonRatio) * (1 - 2 * PoissonRatio)) # 1/YoungsModulus    
    Compressibility = 1 / OedometricModulus # m_v [=] m2/N

    # Initialize the array to store results
    UU = np.zeros(len(NondimensionalTime))  # An array of size NondimensionalTime with zeros
    
    # Loop until convergence for each value in NondimensionalTime
    for kk in range(len(NondimensionalTime)):
        converged = False
        iteration = 0
        while not converged and iteration < max_iterations:
            MM = np.pi * ((2 * iteration) + 1) * 0.5
            term = (2 / MM**2) * np.exp(-(MM**2) * NondimensionalTime[kk])
            previous_value = UU[kk]
            UU[kk] += term

            # Check convergence
            if np.abs(UU[kk] - previous_value) < tolerance:
                converged = True
            else:
                iteration += 1

        # Apply scaling factors
        UU[kk] = (1 - UU[kk]) * LayerDepth * TractionLoad * Compressibility

    return UU  # Return the calculated values
