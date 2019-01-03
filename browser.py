import webbrowser

keyword = input("검색어를 입력해 주세요: ")

url = "https://search.daum.net/search?q="

webbrowser.open(url+keyword)
