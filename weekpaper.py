import requests
import json
import time
import datetime
time.strftime('%Y-%m-%d')
url = 'https://oapi.dingtalk.com/robot/send?access_token=53a5a9db50790c5c9468170930262d6b79c8669583b996da40dae5df2b4400e3'
now_time=datetime.datetime.now()
seven_time=now_time+datetime.timedelta(days=-6)
obj = dict(msgtype="text", text=dict(content='@所有人'+
                                             '\n数字警务室今天下班之前提交实战周报！！！[猫咪][猫咪][猫咪]'+
                                             '\n1)本次报告数据统计时间为：'+
                                             '\n'+seven_time.strftime('%Y-%m-%d')+
                                             '  到  '+now_time.strftime('%Y-%m-%d')+
                                             '\n2)研判案件数等数据均是”新增“的数量，不是历史累积，也不含“更新”案件。'+
                                             '\n3)点开下列链接填写各自负责的“局点”数据（下拉菜单可选择局点，若无相关局点，可自行添加或通知我添加，格式“战区-省-市-局点”）。'+
                                             '\n4)请点击以下链接填写:'+
                                             '\n阿里的实战同学：'+
                                             '\nhttps://yida.alibaba-inc.com/alibaba/web/APP_VH4COUW73O5IGNTCV01G/inst/formSubmit.html?formUuid=FORM-VFYJGRMVB98BKZZL1LEP56J2MUS532HJBPZ3KBB'+
                                             '\n非阿里的实战同学：'+
                                             '\nhttps://yida.alibaba-inc.com/o/szwb'
                                             '\nhttp://vcs.gts.terminus.io/project/user-arrangement'+
                                             '\n5)@董伟@张泽南@张杰峰@谢艺鹏，请在周四下班前检查宇视周报提交情况；若有局点已撤离，或本周无实战人员，请董伟汇总后通知@余柳，多谢！'
                                     ))
requests.post(url,
    headers={'Content-Type': 'application/json'},
    data=json.dumps(obj)
)
