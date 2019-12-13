import os


BASE_PATH = os.getenv("BASE_PATH") or os.path.dirname(__file__)
OUT_PATH = os.path.join(BASE_PATH, "out.txt")


def processFileStream(obj):
  with open(OUT_PATH, 'w') as out_file:
    # docs, if second argument present, the first must be callable
    iter_obj = iter(obj) if not callable(obj) else iter(obj, "")
    for line in iter_obj:
      out_file.write(line.upper())

  print("successfully converted to uppercase")
