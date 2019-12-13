import sys
import argparse
from process_file import processFile, processFileStream

parser = argparse.ArgumentParser(
    description='Process some input source', epilog="UPPERCASE YOUR HEAD 😇  😇",
    prefix_chars='-+'
)

group = parser.add_mutually_exclusive_group()
group.add_argument("--file", help="process the file to uppercase")
group.add_argument("--input", "-", default=True,
                   help="process stdin", type=bool)
args = parser.parse_args()


if(args.file):
  processFile(args.file)
elif (args.input):
  processFileStream(sys.stdin)
