import sys
from config import *
from args_parser import ArgsParser
from csview_opener import CSViewOpener
from csviewer import CSViewer

#TODO file_path
if __name__ == "__main__":
  args = ArgsParser(sys.argv[1:])

  with CSViewOpener(file_path = args.path_to_file) as file:
    csviewer = CSViewer(file, args)
    csviewer.parse()
