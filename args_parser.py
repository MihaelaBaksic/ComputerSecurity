import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mp', required=True, type=str)
parser.add_argument('--adr', required=True, type=str)
parser.add_argument('--pass', type=str);

args = parser.parse_args()

