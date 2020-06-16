# coding=utf-8
import requests




type = input("\n 请输入数字：\n 1：输入accid\n ")              #输入accid

type1 = input("\n 请输入数字：\n 2：输入想要跳转的lv\n")      #输入要跳转到的关卡


urls = "http://test-tc.happyxiaoxiucai.com/games/add/set_level?accid="+type+"&" + "level="+type1   #拼接url
print(urls)
re = requests.get(urls)          #请求接口
print(re.text)                      #查询当前关卡


####################——————ctf——————####################
