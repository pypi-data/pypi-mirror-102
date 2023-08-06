#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/24 17:12
# @Author : 詹荣瑞
# @File : section.py
# @desc : 本代码未经授权禁止商用
from .command import Command
from .content import ContentBase, ContentList
from bonetex.generator.utils import command_label


class Section(ContentBase):

    def __init__(self, title, level: int = 0):
        if level > 2:
            level = 2
        elif level < 0:
            level = 0
        command_section = Command(level * "sub" + "section")
        self.title = title
        self.contents = ContentList(
            command_section(title),
            command_label(f"sec:{id(self)}"),
            separator="\n", end=""
        )
        self.dict = {
            "type": "section",
            "title": title,
            "children": self.contents
        }

    def to_dict(self):
        out_dict = self.dict
        out_dict["children"] = self.contents.to_dict()
        return out_dict

    def __getitem__(self, item):
        return self.contents[item]

    def latex(self, indent=""):
        out = self.contents.latex(indent)
        return out

    def latex3(self, indent=""):
        return self.latex(indent)

    def append(self, *contents):
        self.contents.append(*contents)
        return self
