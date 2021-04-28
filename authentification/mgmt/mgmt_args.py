import argparse

parser = argparse.ArgumentParser()
parser.add_argument('action', type=str)
parser.add_argument('username', type=str)

args = parser.parse_args()
