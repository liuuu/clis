import os


BASE_PATH = os.getenv("BASE_PATH") or os.path.dirname(__file__)
OUT_PATH = os.path.join(BASE_PATH, "out.txt")


def processFile(file_path):
  print(11, file_path)
  abs_file_path = os.path.realpath(os.path.join(BASE_PATH, file_path))
  with open(abs_file_path, 'r') as in_file, open(OUT_PATH, 'w') as out_file:
    for line in iter(in_file.readline, ''):
      out_file.write(line.upper())


def processFileStream(stream):
  with open(OUT_PATH, 'w') as out_file:
    for line in iter(stream):
      out_file.write(line.upper())
      print("successfully converted to uppercase")
