from controllers.BaseController import BaseController
from fastapi import FastAPI,APIRouter,Depends,UploadFile
from models import ResponseEnums
from .ProjectController import ProjectController
import os


class DataController(BaseController):
    
    def __init__(self):
        super().__init__() 
        self.size_scale = 1048576


    def validate_uploaded_file(self,file:UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False,ResponseEnums.FILE_TYPE_NOT_SUPPORTED.value    

        if file.size is not None and file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False,ResponseEnums.FILE_SIZE_EXCEEDED.value


        return True ,ResponseEnums.FILE_UPLOAD_SUCCESS.value


    def generate_unique_path(self, origin_file_name: str,project_id: str):
            random_filename_key = self.generate_unique_name_filename(origin_file_name)     
            project_path = ProjectController().get_project_path(project_id=project_id)
            new_file_path= os.path.join(
                project_path,
                random_filename_key
             )
            while os.path.exists(new_file_path):
                       random_filename_key = self.generate_unique_name_filename(origin_file_name)  
                       new_file_path= os.path.join(
                                        project_path,
                                        random_filename_key
                                    )
            return   new_file_path , random_filename_key                