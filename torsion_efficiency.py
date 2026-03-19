import numpy as np

def tetrahedral_vectors():
    s = 1.0 / np.sqrt(3)
    return [
        np.array([1, 1, 1]) * s,
        np.array([1, -1, -1]) * s,
        np.array([-1, 1, -1]) * s,
        np.array([-1, -1, 1]) * s
    ]

def torsion_scalar(B, omega, geometry='tetra'):
    kappa = 8 * np.pi * 6.6743e-11 / (3e8)**4
    mu0 = 4 * np.pi * 1e-7
    if geometry == 'tetra':
        factor = (4/3) * (3/8) * (1/np.sqrt(3))
        return kappa * (B**2 / (mu0 * omega)) * factor * 4
    elif geometry == 'bilateral':
        return kappa * (B**2 / (mu0 * omega)) * 0.05
    else:
        return kappa * (B**2 / (mu0 * omega)) * 0.27

if __name__ == "__main__":
    B = 6.283e-4
    omega = 628
    print("Tetrahedral S_net:", torsion_scalar(B, omega, 'tetra'))
    print("Bilateral S_net:", torsion_scalar(B, omega, 'bilateral'))
    print("Efficiency ratio:", torsion_scalar(B, omega, 'tetra') / torsion_scalar(B, omega, 'bilateral'))
