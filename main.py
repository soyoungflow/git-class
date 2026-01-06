# from urllib.parse import urlparse, parse_qs

# url = "https://google.com/search?q=python&page=2"

# parsed_url = urlparse(url)
# params = parse_qs(parsed_url.query)

# print("전체 URL:", url)
# print("경로(Path):", parsed_url.path)
# print("쿼리(Query):", parsed_url.query)
# print("쿼리 파라미터:", params)

# items = ["사과", "바나나", "딸기", "포도", "수박"]

# def get_items(skip=0, limit=2):
#     return items[skip: skip + limit]

# print(get_items(skip=1, limit=3))  
# # ['바나나', '딸기', '포도']

import requests

urls = [
    "https://google.com",                # 200 OK
    "https://google.com/nonexist",       # 404 Not Found
    "https://httpbin.org/status/500",    # 500 Internal Server Error
    "https://httpbin.org/status/302"     # 302 Redirect
]

for url in urls:
    response = requests.get(url)
    print(f"URL: {url}")
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        print("→ 정상적으로 데이터를 받았습니다! 😊")
    elif response.status_code == 404:
        print("→ 주소가 잘못되었나봐요! 😢 페이지가 없어요.")
    elif response.status_code == 500:
        print("→ 서버가 아파요! 개발자가 고쳐야 해요 ⚠️")
    elif 300 <= response.status_code < 400:
        print("→ 다른 페이지로 이동시키고 있어요 🔁")
    
    print("-" * 50)

