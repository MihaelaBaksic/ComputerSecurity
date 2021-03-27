import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mp', required=True, type=str)
parser.add_argument('--adr', required=False, type=str)
parser.add_argument('--pwd', required=False, type=str);


args = parser.parse_args()




