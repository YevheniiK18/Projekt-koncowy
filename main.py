import argparse

parser = argparse.ArgumentParser(description='Konwerter danych')
parser.add_argument('input_file', help='Ścieżka do pliku wejściowego')
parser.add_argument('output_file', help='Ścieżka do pliku wyjściowego')
args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file
