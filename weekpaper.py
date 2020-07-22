import requests
import json
import time
import datetime
time.strftime('%Y-%m-%d')
url = 'https://oapi.dingtalk.com/robot/send?access_token=d896f1b9d79c5ea9e56fa8a3f3e848c95b005bc53634457c0b38dfc0c278aad1'
now_time=datetime.datetime.now()
seven_time=now_time+datetime.timedelta(days=-6)
obj = dict(msgtype="text", text=dict(content='@所有人'+
                                             '\麻烦各位实战同学提交以下信息：'+
                                             '\实战日报链接：'+
                                             '\nhttps://yida.alibaba-inc.com/s/ACdaily'+
                                             '\n产品bug及优化建议链接：'+
                                             '\nhttps://yida.alibaba-inc.com/s/PRactualcombat'
                                             '\n感谢各位！'
                                     ))
requests.post(url,
    headers={'Content-Type': 'application/json'},
    data=json.dumps(obj)
)
