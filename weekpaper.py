import requests
import json
import time
import datetime
time.strftime('%Y-%m-%d')
url = 'https://oapi.dingtalk.com/robot/send?access_token=a92543af7d62419352d16643a898bf249d5852284e772839d71dd8ec068fca89'
now_time=datetime.datetime.now()
seven_time=now_time+datetime.timedelta(days=-6)
obj = dict(msgtype="text", text=dict(content='@所有人'+
                                             '\n麻烦各位实战同学提交以下信息：'+
                                             '\n实战日报链接：'+
                                             '\nhttps://yida.alibaba-inc.com/s/ACdaily'+
                                             '\n产品bug及优化建议链接：'+
                                             '\nhttps://yida.alibaba-inc.com/s/PRactualcombat'
                                             '\n感谢各位！'
                                     ))
requests.post(url,
    headers={'Content-Type': 'application/json'},
    data=json.dumps(obj)
)
