import sys
from config import *
from delimiter_determinant import DelimeterDeterminant
from csview_opener import CSViewOpener
from csviewer import CSViewer

if __name__ == "__main__":
  with CSViewOpener() as file:
    csviewer = CSViewer(file, sys.argv[1:])
    print(csviewer.get_head_rows(3))
    determinant = DelimeterDeterminant(csviewer.get_head_rows())
    d = determinant.detect()
