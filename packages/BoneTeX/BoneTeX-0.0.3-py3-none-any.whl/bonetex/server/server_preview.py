#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/19 12:59
# @Author : 詹荣瑞
# @File : server.py
# @desc : 本代码未经授权禁止商用
import code
import json
import os

import requests
from fastapi import FastAPI, Path, Body
from pydantic import BaseModel, Field
from enum import Enum
from bonetex.parser import parse, parse_block, code_init, code_reset
from bonetex.parser import parse_tex

app = FastAPI()

target_dir = os.path.join(os.getcwd(), "../../resources")
target_name = os.path.join(os.getcwd(), "../../resources")
interpreter = code.InteractiveInterpreter()
interpreter.runcode(code_init)


class Template(str, Enum):
    bone = "bone"
    mustache = "mustache"


class ParseIn(BaseModel):
    template: Template = Field(
        "bone", title="LaTeX模版引擎", description="使用指定LaTeX模版引擎对源代码处理"
    )
    code: str = Field(
        ..., title="源代码"
    )

    class Config:
        schema_extra = {
            "example": {
                "template": "bone",
                "code": "",
            }
        }


class ParseOut(BaseModel):
    # block-python:str
    # block-tex:str
    # code-python:str
    # code-tex:str
    # code-safe-tex:str

    class Config:
        schema_extra = {
            "example": {
                "block-python": {},
                "block-tex": {},
                "code-python": code_init,
                "code-tex": "",
                "code-safe-tex": "",
            }
        }


class TestInSchema(BaseModel):
    key: str
    src: str


default_headers = {
    'app_id': 'rrzhan_stu_xidian_edu_cn_c820a4',
    'app_key': 'f457c19f7c81e894fa28',
    'Content-type': 'application/json'
}
num = 5


@app.post("/mathpix")
def test(req: TestInSchema):
    global num
    if num == 0:
        return {"error": "请求超过上限"}
    elif req.key == "MrAWmmWS%U&bY4NtPZqFtPZW6NjML$QpTOP":
        num -= 1
        res = requests.post(
            'https://api.mathpix.com/v3/text',
            data=json.dumps({
                "src": req.src,
                # "data_options": {
                #     "include_asciimath": True,
                #     "include_latex": True
                # }
            }), headers=default_headers)
        return res.json()
    else:
        return {"error": "密码错误"}


@app.get('/get_pid')
async def get_pid():
    return {
        "pid": os.getpid()
    }


@app.post('/parse')
async def parse_code(request: ParseIn):
    interpreter.runcode(code_reset)
    response = {
        "block-python": {},
        "block-tex": {},
        "code-python": code_init,
        "code-tex": "",
        "code-safe-tex": "",
    }
    # method = request.json["method"].split("/")
    #
    # if method[0] == "parse_block":
    #     response["code-python"] = parse_block(request.json["name"], method[1], request.json["code"])
    # elif method[0] == "parse_full":
    if request.template == "bone":
        interpreter.runcode("render = bone_template_render")
    elif request.template == "mustache":
        interpreter.runcode("render = mustache_render")
    for name, code_block in parse(request.code):
        response["block-python"][name] = code_block
        response["code-python"] += f"\r\n{code_block}\r\n"
        interpreter.runcode(code_block)
    response["code-tex"] = interpreter.locals["_doc"].latex()
    response["code-safe-tex"] = parse_tex(response["code-tex"])

    return response


@app.post('/open_file')
async def open_file(path: str = Body(...)):
    (filepath, filename_ex) = os.path.split(path)
    (filename, extension) = os.path.splitext(filename_ex)
    os.chdir(filepath)
    # print(os.path.join(filepath, filename))
    interpreter.runcode(
        f"_compiler = Compiler(_doc, r'{os.path.join(filepath, filename)}', "
        f"compilers='xelatex')"
    )
    return {
        "success": True
    }


@app.post('/save')
async def save(dir: str = Body(...), code: str = Body(...)):
    success = True
    try:
        with open(dir, mode="w", encoding="utf-8") as file:
            file.write(code.replace("\r\n", "\n"))
    except FileNotFoundError:
        success = False

    return {
        "success": success
    }


@app.post('/generate')
async def generate():
    interpreter.runcode(
        "_compiler.generate_pdf()"
    )
    _compiler = interpreter.locals["_compiler"]
    return {
        "curdir": _compiler.path,
        "name": _compiler.name
    }


if __name__ == '__main__':
    import uvicorn

    # 官方推荐是用命令后启动 uvicorn main:app --host=127.0.0.1 --port=8010 --reload
    uvicorn.run(
        app='bonetex.server.server_preview:app',
        host="127.0.0.1", port=6954, reload=True, debug=True
    )
