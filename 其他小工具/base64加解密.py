# coding=utf-8
import base64

####################——————tak制作  vol.605——————####################
####################——————tak制作移植 2.X版——————####################

while True:
    type = input("\033[30m \n 请选择：\n 1：base64加密\n 2：base64解密\n ")
    if type == "1":
        note1 = input("\033[30m 请输入需要加密的内容\返回请输入:0 \033[0m \n")
        if note1 == "0":  # 返回请输入:0
            continue
        else:
            A = base64.b64encode(note1)  # base64解密
            print(A)

    if type == "2":
        note2 = input("\033[30m 请输入需要解密的内容\返回请输入:0 \033[0m \n")
        if note2 == "0":  # 返回请输入:0
            continue
        else:
            B = base64.b64decode(note2)  # base64解密
            print(B)

####################——————tak制作  vol.605——————####################
####################——————tak制作移植 2.X版——————####################
"""
Code producer：aotak
Mobile：+86 18817762560
E-Mail：hujunyi@021.com 
"""
