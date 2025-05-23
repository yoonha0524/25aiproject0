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

# 따뜻한 파란 계열 스타일 설정
st.markdown(
    """
    <style>
    body {
        background-color: #dceeff;
    }
    .stApp {
        background-color: #dceeff;
        color: #002b5c;
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: #003d80;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        color: #336699;
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

# 간단한 MBTI 테스트 섹션
with st.expander("MBTI를 모르시나요? 간단한 테스트로 알아보세요!"):
    q1 = st.radio("사람들과 함께 있을 때 에너지가 충전되나요, 혼자 있을 때 충전되나요?", ["함께 있을 때", "혼자 있을 때"])
    q2 = st.radio("결정을 내릴 때, 직감과 감정을 믿나요, 사실과 논리를 따지나요?", ["직감과 감정", "사실과 논리"])
    q3 = st.radio("계획적인 걸 좋아하나요, 즉흥적인 걸 좋아하나요?", ["계획적", "즉흥적"])
    q4 = st.radio("세부 사항보다 전체적인 그림을 보는 편인가요, 반대인가요?", ["전체적인 그림", "세부 사항"])

    if st.button("테스트 결과 보기"):
        ei = "E" if q1 == "함께 있을 때" else "I"
        tf = "F" if q2 == "직감과 감정" else "T"
        jp = "J" if q3 == "계획적" else "P"
        sn = "N" if q4 == "전체적인 그림" else "S"
        guessed_mbti = ei + sn + tf + jp

        st.markdown(f"### 🧭 예상 MBTI 유형은 **{guessed_mbti}** 입니다!")
        st.markdown("해당 유형을 아래에서 선택해 스트레스 해소법을 확인해보세요.")
        st.snow()

# MBTI별 해소법과 위로 멘트
mbti_data = {
    "INTJ": {"tip": "계획을 세우고 조용한 공간에서 책 읽기, 혹은 미래를 구상해보며 명상하기", "comfort": "🧠 당신의 논리력은 누구보다 빛나요. 혼자만의 시간이 당신에게 큰 힘이 될 거예요. 💡"},
    "INTP": {"tip": "복잡한 퍼즐이나 전략 게임, 혹은 좋아하는 과학 채널 시청", "comfort": "🔍 당신의 창의성은 문제를 해결하는 열쇠예요. 호기심을 마음껏 펼쳐보세요! 🧩"},
    "ENTJ": {"tip": "목표를 재설정하고 운동이나 마인드맵 작성으로 에너지 발산", "comfort": "🚀 당신은 언제나 앞서나가는 리더입니다. 잠시 멈춰 숨을 고르는 것도 전략이에요. 🛤️"},
    "ENTP": {"tip": "새로운 아이디어 떠올리기, 친구들과 가벼운 토론 또는 브레인스토밍", "comfort": "🎯 당신의 재치는 모두에게 영감을 줘요. 가볍게 즐기면서도 의미 있는 걸 찾는 당신이 멋져요. ✨"},
    "INFJ": {"tip": "조용한 명상 시간과 일기 쓰기, 감정 정리를 위한 타로 또는 명언 노트 만들기", "comfort": "🌙 당신의 깊은 사려는 세상을 따뜻하게 합니다. 조용한 곳에서 감정을 정리해보세요. 🕯️"},
    "INFP": {"tip": "감정을 시로 표현하거나 감성적인 음악 듣기, 향초 켜고 명상하기", "comfort": "🎵 당신의 진심은 꼭 전달될 거예요. 감정을 솔직히 느끼는 것도 큰 용기예요. 💖"},
    "ENFJ": {"tip": "친구들과 따뜻한 대화 나누기, 소셜 모임에서 이야기 나누기", "comfort": "💬 당신은 사람들에게 큰 힘이 되어줘요. 가끔은 당신도 기대어 쉬어도 괜찮아요. 🤗"},
    "ENFP": {"tip": "짧은 여행이나 새로운 취미 시작하기, 파티나 소셜 모임 참여", "comfort": "🌈 당신의 열정은 언제나 빛나요! 새로운 경험이 에너지를 되찾는 열쇠가 될 거예요. 🧳"},
    "ISTJ": {"tip": "정리정돈, 계획표 작성, 루틴 재정비로 안정감 찾기", "comfort": "📋 당신의 책임감은 모두에게 귀감이 돼요. 질서 있는 하루가 안정을 줄 거예요. 🧭"},
    "ISFJ": {"tip": "차 한 잔과 함께 좋아하는 드라마 보기, 포근한 담요와 독서", "comfort": "☕ 당신의 배려는 큰 감동을 줍니다. 자신도 소중히 돌보는 시간을 가져보세요. 🛏️"},
    "ESTJ": {"tip": "할 일 목록 정리 후 빠르게 처리하기, 효율적인 정리 및 생산성 도구 사용", "comfort": "⚙️ 당신의 추진력은 누구도 따라올 수 없어요. 일상 속 성취감이 스트레스를 줄여줄 거예요. 📈"},
    "ESFJ": {"tip": "가족이나 친구와 대화 나누기, 따뜻한 손편지 쓰기", "comfort": "👨‍👩‍👧 당신은 늘 따뜻한 존재예요. 사람들과의 연결이 당신을 치유해줄 거예요. 💌"},
    "ISTP": {"tip": "DIY 작업이나 짧은 드라이브, 취미 공방 참여", "comfort": "🛠️ 당신은 조용하지만 강한 사람이에요. 손으로 무언가를 만들며 집중해보세요. 🚗"},
    "ISFP": {"tip": "자연 속 산책이나 미술 활동, 식물 가꾸기", "comfort": "🌿 당신의 감성은 세상을 아름답게 만들어줘요. 자연과 예술은 당신의 마음을 편안하게 해줄 거예요. 🎨"},
    "ESTP": {"tip": "격한 운동이나 외부 활동 참여, 익스트림 스포츠 체험", "comfort": "🔥 당신의 에너지는 모두에게 긍정적 영향을 줘요. 몸을 움직이며 스트레스를 날려보세요! 🏋️"},
    "ESFP": {"tip": "댄스, 노래, 파티 등 즐거운 활동, 야외 피크닉 참여", "comfort": "🎉 당신의 웃음은 모두에게 큰 선물이에요. 즐거움 속에서 당신의 빛이 더욱 빛나요! 🎤"}
}

# MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", options=sorted(mbti_data.keys()))

# 버튼
if st.button("스트레스 해소법 보기"):
    tip = mbti_data[selected_mbti]["tip"]
    comfort = mbti_data[selected_mbti]["comfort"]

    if "자연" in tip or "산책" in tip:
        st.snow()
    elif "운동" in tip or "여행" in tip or "외부" in tip:
        st.balloons()
    elif "드라이브" in tip:
        st.toast("🏞️ 창밖을 바라보며 쉬어가는 여유를 즐겨보세요.")
    else:
        st.toast("✨ 마음의 평화를 찾아보는 시간이 될 거예요.")

    st.markdown(f"## 🚀 {selected_mbti}를 위한 스트레스 해소법")
    st.markdown(f"**Tip:** {tip}")
    st.markdown(f"**🌟 위로 멘트:** _{comfort}_")

    st.success("당신의 하루가 조금 더 가벼워지길 바라요. 💙")

# 푸터
st.markdown("""
---
<div style='text-align: center;'>
    ❤️ 스트레스를 덜어주는 작은 조언이었기를 바랍니다.
</div>
""", unsafe_allow_html=True)
