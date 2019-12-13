import sys
import os
import argparse
from process_file import processFileStream

parser = argparse.ArgumentParser(
    description='Process some input source', epilog="UPPERCASE YOUR HEAD 😇  😇",
    prefix_chars='-+'
)

group = parser.add_mutually_exclusive_group()
group.add_argument("--file", help="process the file to uppercase")
group.add_argument("--input", "-", default=True,
                   help="process stdin", type=bool)
args = parser.parse_args()


BASE_PATH = os.getenv("BASE_PATH") or os.path.dirname(__file__)

if(args.file):
  abs_file_path = os.path.realpath(os.path.join(BASE_PATH, args.file))
  with open(abs_file_path, 'r') as in_file:
    processFileStream(in_file.readline)
elif (args.input):
  processFileStream(sys.stdin)
