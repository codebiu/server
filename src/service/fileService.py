from pathlib import Path
from fastapi import File, UploadFile, APIRouter
from config.fastapi_config import app
from fastapi.responses import JSONResponse
import shutil
from config.index import conf

files_path = str(conf["files_path"])


class fileService:
    """文件服务"""

    @staticmethod
    async def upload_file_service(
        file: UploadFile = File(...), upload_folder=files_path
    ):
        """上传文件"""
        try:
            upload_folder = Path(upload_folder)
            # 检查上传文件夹是否存在，如果不存在则创建
            if not upload_folder.exists():
                upload_folder.mkdir(parents=True, exist_ok=True)
            # 将文件保存到本地
            file_location = upload_folder/file.filename
            with open(file_location, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            return JSONResponse(
                status_code=200,
                content={
                    "message": "File uploaded successfully",
                    "file_path": str(file_location),
                },
            )
        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={"message": "Failed to upload file", "error": str(e)},
            )
