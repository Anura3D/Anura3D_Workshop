import numpy as np
import matplotlib.pyplot as plt

def terzaghi_pressure_solution(
    DataPoints,
    LayerDepth,
    IntrinsicPermeability,
    Porosity,
    Viscosity,
    YoungsModulus,
    PoissonRatio,
    LiquidDensity,
    DimensionalTimeInput,
    EndTime,  
    target_times,
    plot_results
):

    GravitationalAcceleration = 9.81 #m/s2

    # error tolerance and iternation parameters
    tolerance=1e-10
    max_iterations=30
    
    # Calculate Cv
    DrainagePath = LayerDepth # single drainage
    Permeability = IntrinsicPermeability * (LiquidDensity * GravitationalAcceleration) / Viscosity # m/s
    print(Permeability)
    OedometricModulus = YoungsModulus * (1 - PoissonRatio) / ((1 + PoissonRatio) * (1 - 2 * PoissonRatio)) # 1/YoungsModulus
    Compressibility = 1 / OedometricModulus # m_v [=] m2/N
    Cv = Permeability / (Compressibility * LiquidDensity * GravitationalAcceleration) # Cv [=] m2/s input parameter #1.474e-6
    
    # Generate depth array
    DepthArray = np.linspace(0, LayerDepth, DataPoints) # generating a series of depths z
    
    # Generate time arrays
    if DimensionalTimeInput: 
        # prescribed time 
        # if you want to input the dimensional time yourself
        StartTime = 0
        DimensionalTime = np.linspace(StartTime, EndTime, DataPoints)
        NondimensionalTime = Cv * DimensionalTime / (DrainagePath ** 2) # calculate non-dimensional time based on selected time range
    else: 
        # non dimensional time  
        # if you want to want to 
        NondimensionalTime = target_times
        DimensionalTime = [t * (DrainagePath ** 2) / Cv for t in target_times]
    
    # Initialize the u_z array
    u_z = np.zeros((DataPoints, len(NondimensionalTime)))
    
    # Compute u_z with convergence check
    for kk in range(len(NondimensionalTime)):
        for jj in range(DataPoints):
            converged = False
            iteration = 0
            
            while not converged and iteration < max_iterations:
                previous_value = u_z[jj, kk]
                MM = np.pi * ((2 * iteration) + 1) * 0.5
                term = (2 / MM) * ((-1) ** iteration) * np.cos((MM * DepthArray[jj]) / DrainagePath) * np.exp(-(MM ** 2) * NondimensionalTime[kk])
                u_z[jj, kk] += term
                
                if np.abs(u_z[jj, kk] - previous_value) < tolerance:
                    converged = True
                else:
                    iteration += 1

    # Plotting
    if plot_results:
       plt.figure(figsize=(10, 6))
       for kk in range(len(NondimensionalTime)):
           plt.plot(
                u_z[:, kk],
                DepthArray,
                linestyle='-', 
                marker='o', 
                markersize=3,
                markerfacecolor='none',
                color='black',
                label=f'NonDimTime= {NondimensionalTime[kk]}'
            )
        

    plt.ylabel('Depth (meters)')  # X-axis label
    plt.xlabel('u_z')  # Y-axis label
    plt.grid(True)  # Add gridlines for better visualization
    plt.legend()  # Display the legend
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()  # Show the plot
    
    
    return u_z, DimensionalTime, NondimensionalTime, DepthArray