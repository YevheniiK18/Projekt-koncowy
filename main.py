import argparse

parser = argparse.ArgumentParser(description='Opis programu.')
parser.add_argument('--option1', help='Opis opcji 1')
parser.add_argument('--option2', help='Opis opcji 2')
args = parser.parse_args()

if args.option1:
    print(f'Opcja 1: {args.option1}')
if args.option2:
    print(f'Opcja 2: {args.option2}')
