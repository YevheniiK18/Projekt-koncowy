def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Input file path')
    parser.add_argument('output_file', help='Output file path')
    return parser.parse_args()
