import requests
import re
import json
import time
# 設置 User-Agent 和 Cookies
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-TW,zh;q=0.9,ja-JP;q=0.8,ja;q=0.7,yue-CN;q=0.6,yue;q=0.5,en-US;q=0.4,en;q=0.3",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Referer": "https://acg.gamer.com.tw/acgPlayList.php?s=108886",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1"
}

cookies = {
    "_ga": "GA1.1.1957928680.1732967366",
    "ckM": "2531167198",
    "ckGUILD_lastBrowse": "[[%22393%22%2C%22%E6%AD%B7%E5%8F%B2%E3%81%AE%E7%B4%B3%E5%A3%AB%E5%85%AC%E6%9C%83<%E3%82%9D%CF%89%E3%83%BB%22]%2C[%2216197%22%2C%22%E5%A0%B4%E5%A4%96%E4%BA%BA%E7%94%9F%22]]",
    "ckBH_lastBoard": "[[%224918%22%2C%22RPG%E8%A3%BD%E4%BD%9C%E5%A4%A7%E5%B8%AB%22]%2C[%2274934%22%2C%22%E9%B3%B4%E6%BD%AE%22]]",
    "__cf_bm": "MT6wKesmVZDdn0HBxY.yr8G3qa8qSzYRKd2_RVZ3dMc-1734357130-1.0.1.1-FzPEGUCYfPKC1KZL10fx19JqQy.IwYZ7D9HSFqNt0_74SzPN1Lh0yQPX4zRotkS8CgpYCUtdxPOHbkQoo3R5mA",
    "__gads": "ID=95ec04b3a641999f:T=1732967372:RT=1734357138:S=ALNI_Mb249qSSK4wiGTZhlhY2LwihEq6OA",
    # 在這裡繼續添加其他cookies...
}

# URL 的基礎
base_url = "https://acg.gamer.com.tw/acgPlayList.php?tnum=368597&s=108886&t=1"

# 正則表達式模式，匹配 "https://home.gamer.com.tw/{username}"
pattern = r'//home\.gamer\.com\.tw/([a-zA-Z0-9_]+)'

# 目標文件
output_file = "2.txt"

# 迭代頁面數字 i 從 1 到 5
for i in range(3145, 7680):
    time.sleep(2)
    # 構造每個請求的 URL，動態設置 page={i}
    url = f"{base_url}&page={i}"

    # 發送 GET 請求
    response = requests.get(url, headers=headers, cookies=cookies)

    # 輸出回應結果
    print(f"Requesting page {i}, Status Code: {response.status_code}")

    # 用正則表達式匹配所有用戶名
    usernames = re.findall(pattern, response.text)
    
    # 讀取目標文件中的已存在數據
    try:
        with open(output_file, "r", encoding="utf-8") as file:
            existing_usernames = set(line.strip() for line in file)
    except FileNotFoundError:
        # 如果文件不存在，初始化為空集合
        existing_usernames = set()

    # 過濾出尚未存在於文件中的用戶名
    unique_usernames = [username for username in usernames if username not in existing_usernames]

    # 將新數據追加寫入文件
    if unique_usernames:
        with open(output_file, "a", encoding="utf-8") as file:
            for username in unique_usernames:
                file.write(username + "\n")
                print(username)
        print(f"成功寫入 {len(unique_usernames)} 個新用戶名到 {output_file} 中。")
    else:
        print("沒有發現新用戶名，未進行寫入操作。")
