import json
import requests
from concurrent.futures import ThreadPoolExecutor
import time

# 请求头
headers = {
    "Host": "xiaoyaoyou.mmw1984.link",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    "sec-ch-ua-mobile": "?1",
    "Authorization": "Bearer nk-mmxww51709481", 
    "User-Agent": 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36 EdgA/115.0.1901.196', 
    "Content-Type": "application/json",
    "accept": "text/event-stream",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-platform": '"Android"',
    "Origin": 'https://xiaoyaoyou.mmw1984.link',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://xiaoyaoyou.mmw1984.link/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6'
}

# 请求参数
data = {
  "messages":[
     {
        "role":"system",
        "content":"\nYou are ChatGPT, a large language model trained by OpenAI.\nKnowledge cutoff: 2021-09\nCurrent model: gpt-3.5-turbo-16k-0613\nCurrent time: 2023/8/29 22:07:25\n"
     },
     {
        "role":"user", 
        "content":"写一篇5000字的随机论文"
     }
  ],
  "stream":True,
  "model":"gpt-3.5-turbo-16k-0613",
  "temperature":0.4,
  "presence_penalty":0,
  "frequency_penalty":0,
  "top_p":0.5
}

# 请求URL
url = 'https://xiaoyaoyou.mmw1984.link/api/openai/v1/chat/completions'

# 发送请求的函数
def send_request():
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response

# 并发数
concurrent_requests = 10

while True:
    with ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
        futures = {executor.submit(send_request) for _ in range(concurrent_requests)}

    for future in futures:
        response = future.result()  
        console.log(response.status_code)
         console.log(response.text)

    # 等待一段时间再进行下一次循环
  await new Promise(resolve => setTimeout(resolve, 1000)) 

