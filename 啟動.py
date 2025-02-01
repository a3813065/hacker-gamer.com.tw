from 巴哈 import fetch_member_list
from 處理 import extract_and_append_unique_user_ids
def main():
    gsn = 16197  # Guild ID
    sort = 2  # 排序方式
    order = 0  # 排序順序
    prefix = ""  # 前綴

    # 遍歷 {p} 從 1 到 40
    for p in range(1, 8200):
        response = fetch_member_list(gsn, p, sort, order, prefix)
        if response.status_code == 200:
            print(f"Page {p}: {response.text}")
            extract_and_append_unique_user_ids(response.text)
        else:
            print(f"Failed to fetch page {p}. Status Code: {response.status_code}")

if __name__ == "__main__":
    main()
