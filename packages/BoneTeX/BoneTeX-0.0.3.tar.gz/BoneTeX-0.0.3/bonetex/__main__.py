#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/17 14:13
# @Author : 詹荣瑞
# @File : __main__.py
# @desc : 本代码未经授权禁止商用
from bonetex.server.server import app
from bonetex.parser import parser_bone
from bonetex.parser.parser_bone import code_init
import typer

main = typer.Typer(help="BoneTeX命令行程序")


@main.command(help="开启一个解析服务器。")
def server(port: int = typer.Option(6954, min=0, max=65535, help="指定服务器端口")):
    app.run(port=port)


@main.command(help="解析目标文件。")
def parse(path: str = typer.Argument(..., help="指定源文件")):
    try:
        with open(path + ".btex", mode='r', encoding="utf-8") as file:
            out = parser_bone.parse(file.read())
        with open(path + ".py", mode='w', encoding="utf-8") as file:
            file.write(code_init + "".join(code for name, code in out))
    except FileNotFoundError:
        print(f"未找到<{path}>文件")


main()
