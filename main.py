import streamlit as st
from PIL import Image
import base64

# 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 스트레스 해소법",
    page_icon="🌌",
    layout="centered",
    initial_sidebar_state="auto"
)

# 배경 색상 및 스타일 설정 (파란 계열)
st.markdown(
    """
    <style>
    body {
        background-color: #e6f2ff;
    }
    .stApp {
        background-color: #e6f2ff;
        color: #003366;
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: #004080;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        color: #0059b3;
        font-size: 20px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 제목
st.markdown("<div class='title'>MBTI로 알아보는 스트레스 해소법</div>", unsafe_allow_html=True)

# 부제목
st.markdown("<div class='subtitle'>당신의 성격에 딱 맞는 스트레스 해소법을 추천해드릴게요!</div>", unsafe_allow_html=True)

# MBTI별 해소법과 위로 멘트
mbti_data = {
    "INTJ": {
        "tip": "하루쯤은 혼자만의 시간을 가져보세요. 조용한 서재에서 좋아하는 책을 읽거나, 미래를 설계하는 글쓰기를 해보세요. 생산적인 활동이 스트레스를 줄이는 데 도움이 됩니다.",
        "comfort": "당신은 언제나 멀리 보는 사람이에요. 잠시 쉬어가도 괜찮아요."
    },
    "INFP": {
        "tip": "감정이 복잡할 때는 글로 써보세요. 시나 일기를 쓰거나 따뜻한 음악을 들으며 자신의 감정과 조용히 대화해보세요.",
        "comfort": "당신의 따뜻함은 그대로예요. 오늘은 스스로를 안아주는 날로 해요."
    },
    "ENFP": {
        "tip": "새로운 사람을 만나거나 새로운 장소를 가보세요. 여행, 공연, 전시회 등 창의력을 자극하는 경험이 스트레스를 날려줍니다.",
        "comfort": "당신의 에너지는 누구에게나 힘이 돼요. 잠깐 쉬어도 괜찮아요."
    },
    "ISTJ": {
        "tip": "일정 정리나 정리정돈을 통해 마음을 다잡아보세요. 계획이 잘 세워질수록 마음도 안정됩니다.",
        "comfort": "지금까지도 잘해왔어요. 한 걸음 천천히 가도 괜찮아요."
    },
    # 필요 시 모든 16유형 추가 가능
}

# MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", options=sorted(mbti_data.keys()))

# 버튼
if st.button("스트레스 해소법 보기"):
    tip = mbti_data[selected_mbti]["tip"]
    comfort = mbti_data[selected_mbti]["comfort"]

    st.balloons()  # 특수 효과

    st.markdown(f"## 🚀 {selected_mbti}를 위한 스트레스 해소법")
    st.markdown(f"**Tip:** {tip}")
    st.markdown(f"**🌟 위로 멘트:** _{comfort}_")

    st.success("당신의 하루가 조금 더 가벼워지길 바라요. ")

# 푸터
st.markdown("""
---
<div style='text-align: center;'>
    ❤️ 스트레스를 덜어주는 작은 조언이었기를 바랍니다.
</div>
""", unsafe_allow_html=True)

