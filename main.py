from config import *
from delimiter_determinant import DelimeterDeterminant
from csview_opener import CSViewOpener
from csviewer import CSViewer

with CSViewOpener() as file:
  csviewer = CSViewer(file)
  print(csviewer.get_head_rows(3))
  determinant = DelimeterDeterminant(csviewer.get_head_rows())
  d = determinant.detect()
