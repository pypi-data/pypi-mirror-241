import os
from pathlib import Path

import nonebot
from fastapi import FastAPI
from fastapi.responses import FileResponse
from nonebot import get_driver

DRIVER = get_driver()
dir_path = Path(__file__).parent
img_path = dir_path / 'image_cache'

app: FastAPI = nonebot.get_app()


@DRIVER.on_startup
def app_run():
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    print('启动成功')

    @app.get('/uploads/<filename>')
    async def get_file(filename):
        return FileResponse(img_path / filename)
