import requests

# Cookies 設定
cookies = {
    "_ga": "GA1.1.1957928680.1732967366",
    "ckM": "2531167198",
    "buap_modr": "p014",
    "buap_puoo": "p301",
    "ckGUILD_lastBrowse": "[[%22393%22%2C%22%E6%AD%B7%E5%8F%B2%E3%81%AE%E7%B4%B3%E5%A3%AB%E5%85%AC%E6%9C%83<%E3%82%9D%CF%89%E3%83%BB%22]%2C[%2216197%22%2C%22%E5%A0%B4%E5%A4%96%E4%BA%BA%E7%94%9F%22]]",
    "__cf_bm": "mKDJpSKveQTKgl_fc6yuPtBbSyXcrhujBogkMvHPNso-1734356145-1.0.1.1-Q4xXxyx1VD13BCae5ygrGeY76tskUbcg3HDEXHnwcFUld5j1UZ_lbQKNVUun8pDMU5CvDEDJrPkzKFVo9ivUpA",
    # 添加其他需要的 cookies
}

# Headers 設定
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-TW,zh;q=0.9,ja-JP;q=0.8,ja;q=0.7",
    "Cache-Control": "no-cache",
    "Origin": "https://user.gamer.com.tw",
    "Pragma": "no-cache",
    "Referer": "https://user.gamer.com.tw/login.php",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary5oKFBZTGBgOAVY8R"
}

# URL
url = "https://user.gamer.com.tw/ajax/do_login.php"

# 直接設定用戶名和密碼
i = "qweasd891107"  # 用戶名
b = "qweasd20001107"  # 密碼

# 構建請求正文
body = f"""
------WebKitFormBoundary5oKFBZTGBgOAVY8R
Content-Disposition: form-data; name="userid"

{i}
------WebKitFormBoundary5oKFBZTGBgOAVY8R
Content-Disposition: form-data; name="password"

{b}
------WebKitFormBoundary5oKFBZTGBgOAVY8R
Content-Disposition: form-data; name="autoLogin"

T
------WebKitFormBoundary5oKFBZTGBgOAVY8R
Content-Disposition: form-data; name="alternativeCaptcha"

02753364ae07ee19c9614597a81366b2c958e0e81be8b46d67651af3
------WebKitFormBoundary5oKFBZTGBgOAVY8R
Content-Disposition: form-data; name="twoStepAuth"


------WebKitFormBoundary5oKFBZTGBgOAVY8R--
"""

# 發送請求
response = requests.post(url, headers=headers, cookies=cookies, data=body.encode("utf-8"))

# 輸出結果
print(f"用戶名: {i}, 密碼: {b}, 回應狀態碼: {response.status_code}")
print("回應內容:", response.text)
