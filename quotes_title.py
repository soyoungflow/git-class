import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
resp = requests.get(url)
resp.raise_for_status()
soup = BeautifulSoup(resp.text, "lxml")

# 모든 명언 블록 가져오기 (리스트)
quotes = soup.select("div.quote")

print("📝 현재 페이지 명언 목록")
print("=" * 40)

for i, quote in enumerate(quotes, start=1):
    text_tag = quote.select_one("span.text")
    author_tag = quote.select_one("small.author")

    if text_tag and author_tag:
        text = text_tag.text.strip()
        author = author_tag.text.strip()
        print(f"{i}. {text}  - {author}")
