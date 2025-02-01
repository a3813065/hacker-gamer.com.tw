import json

def extract_and_append_unique_user_ids(response_text, output_file="123.txt"):
    """
    從 API 回應中提取 `userid`，檢查是否重複，僅追加寫入唯一的數據到指定文件。
    
    :param response_text: API 回應的 JSON 字符串
    :param output_file: 要寫入的目標文件名（默認為 123.txt）
    """
    try:
        # 解析 JSON 回應
        data = json.loads(response_text)
        # 提取 `userid` 列表
        member_list = data.get("data", {}).get("memberList", [])
        user_ids = [member.get("userid") for member in member_list if "userid" in member]

        # 讀取目標文件中的已存在數據
        try:
            with open(output_file, "r", encoding="utf-8") as file:
                existing_ids = set(line.strip() for line in file)
        except FileNotFoundError:
            # 如果文件不存在，初始化為空集合
            existing_ids = set()

        # 過濾出尚未存在於文件中的 ID
        unique_ids = [user_id for user_id in user_ids if user_id not in existing_ids]

        # 將新數據追加寫入文件
        if unique_ids:
            with open(output_file, "a", encoding="utf-8") as file:
                for user_id in unique_ids:
                    file.write(user_id + "\n")
            print(f"成功寫入 {len(unique_ids)} 個新用戶 ID 到 {output_file} 中。")
        else:
            print("沒有發現新用戶 ID，未進行寫入操作。")

    except json.JSONDecodeError:
        print("無法解析 JSON，請檢查輸入內容是否為正確的 JSON 格式。")
    except Exception as e:
        print(f"發生錯誤：{e}")

# 測試數據
response_text = """
{
    "data": {
        "memberCount": 8401,
        "memberList": [
            {
                "sn": 1739774,
                "userid": "anslook",
                "lowerUserid": "anslook",
                "class": 1,
                "level": 0,
                "classTitle": "",
                "contribute": 20,
                "contributeMtime": "2024-12-01",
                "contributeOver30Days": false,
                "contributeMtimeHumanFormat": "13 \u5929\u524d",
                "accurateContributeMtime": "2024-12-01 13:45:14",
                "ctime": "2024-09-26 15:52:23",
                "nick": "\u5230\u5e95\u522a\u5e7e\u6b21",
                "avatar": "https:\/\/avatar2.bahamut.com.tw\/avataruserpic\/a\/n\/anslook\/anslook_s.png"
            },
            {
                "sn": 1739747,
                "userid": "tender9300",
                "lowerUserid": "tender9300",
                "class": 1,
                "level": 0,
                "classTitle": "",
                "contribute": 40,
                "contributeMtime": "2024-12-14",
                "contributeOver30Days": false,
                "contributeMtimeHumanFormat": "\u4eca\u5929",
                "accurateContributeMtime": "2024-12-14 00:22:02",
                "ctime": "2024-09-26 00:58:37",
                "nick": "\u9752\u6749",
                "avatar": "https:\/\/avatar2.bahamut.com.tw\/avataruserpic\/t\/e\/tender9300\/tender9300_s.png"
            },
            {
                "sn": 1739671,
                "userid": "alen88620",
                "lowerUserid": "alen88620",
                "class": 1,
                "level": 0,
                "classTitle": "",
                "contribute": 25,
                "contributeMtime": "2024-11-26",
                "contributeOver30Days": false,
                "contributeMtimeHumanFormat": "18 \u5929\u524d",
                "accurateContributeMtime": "2024-11-26 09:43:56",
                "ctime": "2024-09-24 16:09:14",
                "nick": "alen",
                "avatar": "https:\/\/avatar2.bahamut.com.tw\/avataruserpic\/a\/l\/alen88620\/alen88620_s.png"
            }
        ]
    }
}
"""

# 調用函數測試
extract_and_append_unique_user_ids(response_text)
