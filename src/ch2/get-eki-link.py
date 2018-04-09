from bs4 import BeautifulSoup

html = open("eki-link.html", encoding="utf-8").read()

soup = BeautifulSoup(html, "html.parser")

# <a>タグを抽出する
links = soup.select("a[href]")

# (タイトル, URL)のリストを作る
result = []
for a in links:
    href = a.attrs["href"]
    title = a.string
    result.append((title, href))
print(result)
