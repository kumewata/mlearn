from selenium import webdriver

url = "http://www.aozora.gr.jp/cards/000081/files/46268_23911.html"

# PhantomJSのドライバを得る
browser = webdriver.PhantomJS()
# 暗黙的な大気を最大3秒行う
# URLを読み込む
browser.get(url)
# 画面をキャプチャしてファイルに保存
browser.save_screenshot("Wbsite.png")
# ブラウザーを終了
browser.quit()
