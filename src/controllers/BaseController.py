from helpers.config import get_settings, Settings
import os
from uuid import uuid4
from pathlib import Path






class BaseController:
    def __init__(self):
        self.app_settings = get_settings()


        self.base_dir= os.path.dirname(os.path.dirname(__file__))
        self.file_dir= os.path.join(
            self.base_dir,
            "assets/files"
        )
       # self.file_dir= self.base_dir + "/" + "assets/files"

       # random name for file upload
      

    

    def generate_unique_name_filename(self,filename: str) -> str:
        ext = Path(filename).suffix.lower()
        return f"{uuid4().hex}{ext}"