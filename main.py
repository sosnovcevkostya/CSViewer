import sys
from config import *
from delimiter_determinant import delimiterDeterminant
from csview_opener import CSViewOpener
from csviewer import CSViewer

#TODO file_path
if __name__ == "__main__":
  with CSViewOpener() as file:
    csviewer = CSViewer(file, sys.argv[1:])
    csviewer.parse()
