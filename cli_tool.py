import argparse
import matplotlib.pyplot as plt
import numpy as np

class TorsionEfficiency:
    def __init__(self, length, angle, material):
        self.length = length
        self.angle = angle
        self.material = material

    def calculate_efficiency(self):
        # Simplistic calculation for demonstration
        efficiency = (self.length * np.cos(np.radians(self.angle))) / self.material_strength(self.material)
        return efficiency

    def material_strength(self, material):
        # Placeholder for material strength calculation
        strengths = {'steel': 200, 'aluminum': 100, 'plastic': 50}
        return strengths.get(material, 1)

    def visualize(self, efficiency):
        plt.bar(['Efficiency'], [efficiency])
        plt.title('Torsion Efficiency')
        plt.ylabel('Efficiency Value')
        plt.show()

def main():
    parser = argparse.ArgumentParser(description='Torsion Efficiency Calculator')
    parser.add_argument('--length', type=float, required=True, help='Length of the object')
    parser.add_argument('--angle', type=float, required=True, help='Angle of torsion')
    parser.add_argument('--material', type=str, required=True, choices=['steel', 'aluminum', 'plastic'], help='Material type')

    args = parser.parse_args()
    torsion = TorsionEfficiency(args.length, args.angle, args.material)
    efficiency = torsion.calculate_efficiency()
    print(f'Torsion Efficiency: {efficiency}')
    torsion.visualize(efficiency)

if __name__ == '__main__':
    main()