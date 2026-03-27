"""
ALPHA-8 Torsion Efficiency Comparison
V1 (bilateral), V2 (cylindrical), V3 (tetrahedral)
"""
import numpy as np

MU0   = 4 * np.pi * 1e-7
KAPPA = 8 * np.pi * 6.674e-11 / (2.998e8)**4
TETRA = np.arccos(-1/3)  # 109.4712...°

def B0(I, R):
    return MU0 * I / (2 * R)

def S_bilateral(I, R, omega):
    b = B0(I, R)
    return KAPPA * b**2 / (MU0 * omega) * 0.05   # 95% cancels

def S_cylindrical(I, R, omega):
    b = B0(I, R)
    return KAPPA * b**2 / (MU0 * omega) * 0.27

def S_tetrahedral(I, R, omega):
    b = B0(I, R)
    sigma = b**2 / (MU0 * omega)
    S_ec   = KAPPA * 4 * sigma
    S_iso  = (4/3) * S_ec
    return S_iso * (6/16) * (1/np.sqrt(3))

if __name__ == "__main__":
    I, R, omega = 200, 0.20, 628.3
    print(f"V1 bilateral:   S = {S_bilateral(I,R,omega):.3e} m⁻¹  eff=5%")
    print(f"V2 cylindrical: S = {S_cylindrical(I,R,omega):.3e} m⁻¹  eff=27%")
    print(f"V3 tetrahedral: S = {S_tetrahedral(I,R,omega):.3e} m⁻¹  eff=28.9%")
    print(f"Tetrahedral angle: {np.degrees(TETRA):.7f}°")
    
