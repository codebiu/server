# self

from config.log import console
from config.fastapi_config import app
from service.index import TableService
from config.path import path_html
# lib
import os
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import APIRouter, status
from fastapi.openapi.docs import get_swagger_ui_html


html_file = open(os.path.join(path_html, "index.html"), 'r').read()
# 配置前端静态文件服务
app.mount("/assets", StaticFiles(directory=os.path.join(path_html, "assets"), html=True), name="assets")
# 首页 app非router挂载
@app.get("/", response_class=HTMLResponse)
async def server():
    console.log('初始首页html') 
    return html_file




# 自定义 Swagger 文档路由，指向本地的 Swagger UI 文件
@app.get("/docs_self", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="/assets/swagger-ui/swagger-ui-bundle.js",
        swagger_css_url="/assets/swagger-ui/swagger-ui.css"
    )


# 基础db
router = APIRouter()

# 测试
@router.get("/create",status_code=status.HTTP_201_CREATED)
async def create():
    '''创建未创建的表'''
    result=await TableService.create()
    return result

app.include_router(router,prefix="/db",tags=['db'])
console.log('...controller index')
