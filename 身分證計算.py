def is_valid_taiwan_id(id_number):
    # 身分證的首字母對應的數字（戶籍地）
    letters_map = {
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17,
        'I': 34, 'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23,
        'Q': 24, 'R': 25, 'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 30, 'X': 31,
        'Y': 32, 'Z': 33
    }

    # 確認身分證號碼長度應為 10 個字元
    if len(id_number) != 10:
        return False

    # 首字母轉換為對應的數字
    letter = id_number[0].upper()
    if letter not in letters_map:
        return False
    letter_number = letters_map[letter]
    
    # 取得每一位數字，並計算加權和
    digits = [int(x) for x in id_number[1:]]
    
    # 按照給定規則計算 S
    S = (letter_number // 10) + (letter_number % 10) * 9  # 戶籍碼部分
    S += digits[0] * 8 + digits[1] * 7 + digits[2] * 6 + digits[3] * 5 + digits[4] * 4 + digits[5] * 3 + digits[6] * 2 + digits[7] * 1
    
    # 計算檢查碼
    remainder = S % 10
    check_digit = (10 - remainder) % 10
    
    # 檢查是否與最後一位數字一致
    if check_digit == digits[8]:
        return True
    else:
        return False

def generate_possible_id_numbers(prefix_a, suffix_b):
    # prefix_a 為 A127，suffix_b 為 2431
    possible_ids = []
    
    # 生成所有中間 2 位數（從 00 到 99）
    for i in range(100):
        middle_two = f"{i:02d}"  # 保證 2 位數
        id_number = f"{prefix_a}{middle_two}{suffix_b}"
        
        # 檢查此身分證是否有效
        if is_valid_taiwan_id(id_number):
            possible_ids.append(id_number)
    
    return possible_ids

# 測試範例
prefix_a = "A127"  # 首 4 位數
suffix_b = "2431"  # 後 4 位數

possible_ids = generate_possible_id_numbers(prefix_a, suffix_b)

# 輸出所有有效的身分證號
if possible_ids:
    print("有效的身分證號有：")
    for valid_id in possible_ids:
        print(valid_id)
else:
    print("沒有找到有效的身分證號。")
