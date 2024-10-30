from fastapi import File, UploadFile,APIRouter
from config.fastapi_config import app
from fastapi.responses import JSONResponse
import shutil,os

class fileService:
    '''文件服务'''
    @staticmethod
    async def upload_file_service(file: UploadFile = File(...),upload_folder = "uploaded_files"):
        '''上传文件'''
        try:
            # 检查上传文件夹是否存在，如果不存在则创建
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)

            # 将文件保存到本地
            file_location = os.path.join(upload_folder, file.filename)
            with open(file_location, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            return JSONResponse(status_code=200, content={"message": "File uploaded successfully", "file_path": file_location})
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": "Failed to upload file", "error": str(e)})