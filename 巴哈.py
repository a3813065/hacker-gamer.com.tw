import requests

def get_headers():
    """
    返回請求所需的 Headers。
    """
    return {
        "authority": "api.gamer.com.tw",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-TW,zh;q=0.9",
        "cache-control": "no-cache",
        "origin": "https://guild.gamer.com.tw",
        "referer": "https://guild.gamer.com.tw/member.php?gsn=393",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }

def get_cookies():
    """
    返回請求所需的 Cookies。
    """
    return {
        "_ga": "GA1.1.1957928680.1732967366",
        "ckM": "2531167198",
        "buap_modr": "p014",
        "ckBahaAd": "-----0--------0-",
        # 添加其他必要的 Cookies...
    }

def fetch_member_list(gsn, p, sort, order, prefix):

    url = f"https://api.gamer.com.tw/guild/v1/member_list.php?gsn={gsn}&p={p}&sort={sort}&order={order}&prefix={prefix}"
    headers = get_headers()
    cookies = get_cookies()
    response = requests.get(url, headers=headers, cookies=cookies)
    return response
