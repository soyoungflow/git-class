import requests
url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url)
todos = response.json()

print("전체 개수:", len(todos))

# 리스트 컴프리헨션(list comprehension)
# todos 안에 있는 todo 하나하나를 검사하면서
# completed 값이 False 인 것만 새 리스트로 만듦
not_completed = [
    todo                    # 조건을 만족하면 이 값을 새 리스트에 추가
    for todo in todos        # todos 리스트에서 todo 하나씩 꺼내서
    if not todo["completed"] # completed == False 인 경우만 선택
]

print("완료되지 않은 TODO 개수:", len(not_completed))
print("\n[완료되지 않은 TODO 5개만 출력]")
for todo in not_completed[:5]:
    # todo는 하나의 할 일(dict)
    # todo['id']     → 할 일 번호
    # todo['title']  → 할 일 제목
    print(f"- (id={todo['id']}) {todo['title']}")