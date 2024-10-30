from fastapi import File, UploadFile,APIRouter
from config.fastapi_config import app
from service.fileService import fileService
router = APIRouter()
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    '''上传文件'''
    return await fileService.upload_file_service(file)

app.include_router(router,prefix="/utils",tags=['utils'])
