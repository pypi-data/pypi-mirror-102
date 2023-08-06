#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/10 16:04
# @Author : 詹荣瑞
# @File : server_socket.py
# @desc : 本代码未经授权禁止商用
import code
import os
from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, types
from bonetex.parser import parse, parse_block, code_init, code_reset
from bonetex.parser import parse_tex


app = FastAPI()
interpreters = {}


class ConnectionManager:
    def __init__(self):
        # 存放激活的ws连接对象
        self.active_connections: List[WebSocket] = []

    async def connect(self, ws: WebSocket):
        # 等待连接
        await ws.accept()
        # 存储ws连接对象
        self.active_connections.append(ws)

    def disconnect(self, ws: WebSocket):
        # 关闭时 移除ws对象
        self.active_connections.remove(ws)

    @staticmethod
    async def send_json(message: dict, ws: WebSocket):
        await ws.send_json(message)

    @staticmethod
    async def send_personal_message(message: str, ws: WebSocket):
        # 发送个人消息
        await ws.send_text(message)

    async def broadcast(self, message: str):
        # 广播消息
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.websocket("/{user}")
async def websocket_endpoint(websocket: WebSocket, user: str):
    await manager.connect(websocket)
    await manager.send_json({
        "jsonrpc": "2.0",
        "result": os.getpid()
    }, websocket)

    interpreters[user] = code.InteractiveInterpreter()
    interpreter = interpreters[user]
    interpreter.runcode(code_init)

    try:
        while True:
            data = await websocket.receive_json()
            print(data)
            await manager.send_personal_message(f"你说了: {data}", websocket)
            await manager.broadcast(f"用户:{user} 说: {data}")

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"用户-{user}-离开")


if __name__ == "__main__":
    import uvicorn

    # 官方推荐是用命令后启动 uvicorn main:app --host=127.0.0.1 --port=8010 --reload
    uvicorn.run(
        app='bonetex.server.socket_server:app',
        host="127.0.0.1", port=6954, reload=True, debug=True
    )
