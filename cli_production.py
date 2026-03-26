import argparse
import matplotlib.pyplot as plt
from torsion_efficiency import calculate_efficiency, visualize_comparison


def main():
    parser = argparse.ArgumentParser(description='CLI for Torsion Efficiency Calculation')
    parser.add_argument('--mode', choices=['single', 'sweep'], required=True, 
                        help='Select calculation mode: single for single calculation, sweep for parameter sweep')
    parser.add_argument('--parameter', type=float, help='Specify the parameter for single calculation')
    parser.add_argument('--param_range', nargs=2, type=float, help='Range for parameter sweep (start end)')
    parser.add_argument('--steps', type=int, help='Number of steps for parameter sweep')

    args = parser.parse_args()

    if args.mode == 'single':
        if args.parameter is None:
            parser.error('--parameter is required for single mode')
        efficiency = calculate_efficiency(args.parameter)
        print(f'Calculated Efficiency: {efficiency}')

    elif args.mode == 'sweep':
        if args.param_range is None or args.steps is None:
            parser.error('--param_range and --steps are required for sweep mode')
        start, end = args.param_range
        step_size = (end - start) / args.steps
        parameters = [start + i * step_size for i in range(args.steps + 1)]
        efficiencies = [calculate_efficiency(p) for p in parameters]
        visualize_comparison(parameters, efficiencies)


if __name__ == '__main__':
    main()