import streamlit as st
import random
import os
from gtts import gTTS
from convert import convert_to_thai_text, convert_to_katakana

st.title("タイ語 数字クイズ")


level = st.radio("レベルを選んでください：", [
    "初級 (0-100)",
    "中級 (0-1000)",
    "上級 (0-10000)",
    "パーフェクト (0-99999)"
])


# 範囲設定
if level == "初級 (0-100)":
    max_number = 100
elif level == "中級 (0-1000)":
    max_number = 1000
elif level == "上級 (0-10000)":
    max_number = 10000
else:
    max_number = 99999

# 現在の数字（セッションで保持）
if "current_number" not in st.session_state:
    st.session_state.current_number = random.randint(0, max_number)

number = st.session_state.current_number
thai_text = convert_to_thai_text(number)
katakana = convert_to_katakana(thai_text)

# 表示
st.subheader(f"数字：{number}")

if st.button("答え"):
    st.markdown(f"**タイ語：** {thai_text}")
    st.markdown(f"**カタカナ：** {katakana}")

    # 音声ファイル生成 or 読み込み
    audio_path = f"audio/{number}.mp3"
    if not os.path.exists(audio_path):
        os.makedirs("audio", exist_ok=True)
        tts = gTTS(thai_text, lang="th")
        tts.save(audio_path)

    st.audio(audio_path, format="audio/mp3")

if st.button("NEXT"):
    st.session_state.current_number = random.randint(0, max_number)
    st.rerun()  
