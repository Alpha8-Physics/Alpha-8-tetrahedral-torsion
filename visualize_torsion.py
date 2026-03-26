def plot_torsion_efficiency(data):
    import matplotlib.pyplot as plt
    
    # Extracting the necessary information from data
    angles = [d['angle'] for d in data]
    efficiencies = [d['efficiency'] for d in data]
    
    # Creating the plot
    plt.figure(figsize=(10, 5))
    plt.plot(angles, efficiencies, marker='o')
    plt.title('Torsion Efficiency vs Angle')
    plt.xlabel('Angle (degrees)')
    plt.ylabel('Torsion Efficiency')
    plt.grid(True)
    plt.show()

def save_torsion_efficiency_plot(data, filename):
    import matplotlib.pyplot as plt
    
    # Extracting the necessary information from data
    angles = [d['angle'] for d in data]
    efficiencies = [d['efficiency'] for d in data]
    
    # Creating the plot
    plt.figure(figsize=(10, 5))
    plt.plot(angles, efficiencies, marker='o')
    plt.title('Torsion Efficiency vs Angle')
    plt.xlabel('Angle (degrees)')
    plt.ylabel('Torsion Efficiency')
    plt.grid(True)
    
    # Saving the plot as a file
    plt.savefig(filename)
    plt.close()