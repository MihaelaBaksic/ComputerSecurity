import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mp', required=True, type=str)
parser.add_argument('--adr', type=str)
parser.add_argument('--pwd', type=str);

args = parser.parse_args()

