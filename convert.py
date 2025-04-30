# convert.py

digit_text = ["ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
digit_kana = ["スーン", "ヌン", "ソーン", "サーム", "シー", "ハー", "ホック", "ジェット", "ペート", "ガーオ"]
unit_text = ["", "สิบ", "ร้อย", "พัน", "หมื่น"]
unit_kana = ["", "シップ", "ローイ", "パン", "ムーン"]

def convert_to_thai_text(n):
    if n == 0:
        return digit_text[0]
    result = ""
    num_str = str(n)
    length = len(num_str)
    for i, ch in enumerate(num_str):
        digit = int(ch)
        pos = length - i - 1

        if digit == 0:
            continue

        if pos == 1:
            if digit == 1:
                result += "สิบ"
            elif digit == 2:
                result += "ยี่สิบ"
            else:
                result += digit_text[digit] + "สิบ"
        elif pos == 0:
            if digit == 1 and length > 1:
                result += "เอ็ด"
            else:
                result += digit_text[digit]
        else:
            result += digit_text[digit] + unit_text[pos]
    return result

def convert_to_katakana(thai_text):
    # 特例
    special_cases = {
        "ยี่สิบ": "イーシップ",
        "สิบเอ็ด": "シップエット",
        "เอ็ด": "エット",  # 単体のหนึ่ง→เอ็ด（11や101など）
    }

    for k, v in special_cases.items():
        thai_text = thai_text.replace(k, v)

    # 一般変換
    for t, k in zip(unit_text, unit_kana):
        thai_text = thai_text.replace(t, k)
    for t, k in zip(digit_text, digit_kana):
        thai_text = thai_text.replace(t, k)

    return thai_text
