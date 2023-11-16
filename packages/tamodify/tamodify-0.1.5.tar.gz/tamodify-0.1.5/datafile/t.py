#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tamodify as ta

def 生成索引():
    ta.createidx(22,"OFI","sed","rv","20231112")
    ta.widx("01",2)
    ta.widx("01")
    ta.closeidx()

def 生成数据文件():
    ta.createdatafile(22,"01","sed","rv","20231114")
    ta.set2("Address","abc12345")
    ta.writedata()
    ta.closedatafile()

def 修改文件():
    ta.open("OFD_sed_rv_20231114_01.TXT","t.txt")
    while ta.read() == 0:
        姓名=ta.get("InvestorName")
        ta.set("Address","abc")
        ta.write()
    ta.close()

def main():
    生成索引()
    生成数据文件()
    修改文件()
    
main()
