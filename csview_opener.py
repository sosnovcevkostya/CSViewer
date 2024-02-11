import os
import re

class CSViewOpener:
    DATA_DIR = "./data"

    def __init__(self, **kwargs):
        self._show_service_info(**kwargs)
        file_path = kwargs['file_path'] if 'file_path' in kwargs.keys() else None

        if file_path:
          self.file_path = file_path
        else:
          for file in os.listdir(self.DATA_DIR):
            if re.match(r".*\.csv", file):
               self.file_path = '/'.join([self.DATA_DIR, file])
               break
          if not self.file_path:
             raise RuntimeError('There is no csv file to show')

    def __enter__(self):
        self.file_obj = open(self.file_path, mode="r")
        return self.file_obj

    def __exit__(self, exc_type, exc_value, traceback):
        if not all(value is None for value in [exc_type, exc_value, traceback]):
           print(f"""CSViewOpener is interrupted with 
                 exc_type: {{{exc_type}}}, 
                 exc_value: {{{exc_value}}}, 
                 traceback: {{{traceback}}}""")
        
        if self.file_obj:
            self.file_obj.close()
    
    @staticmethod
    def _show_service_info(**kwargs):
      print(f'CSViewOpener is invoked with params { {key: value for key, value in kwargs.items()}}')      
