# json_todo_one.py
import requests

# 1) 요청 보낼 URL
url = "https://jsonplaceholder.typicode.com/todos/1"

# 2) GET 요청 보내기
response = requests.get(url)

# 3) 상태 코드 확인
print("Status Code:", response.status_code)

# 4) JSON 응답으로 파싱하기
data = response.json()   # <- 핵심!

print("응답 타입:", type(data))  # dict 인지 확인

# 5) 전체 데이터 출력
print("전체 데이터:", data)

# 6) 특정 필드 꺼내보기
print("ID:", data["id"])
print("제목(title):", data["title"])
print("완료 여부(completed):", data["completed"])