import argparse

parser = argparse.ArgumentParser(description='File Converter')
parser.add_argument('input_file', help='Input file path')
parser.add_argument('output_file', help='Output file path')
args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file
