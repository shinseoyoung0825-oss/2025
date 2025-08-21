import streamlit as st

# MBTI별 직업 추천 데이터
career_dict = {
    "INTJ": ["연구원", "전략기획자", "데이터 분석가"],
    "ENTP": ["기업가", "마케팅 전문가", "변호사"],
    "INFJ": ["상담가", "작가", "교사"],
    "ESFP": ["배우", "이벤트 기획자", "홍보 담당자"],
    "ISTJ": ["회계사", "군인", "법률 전문가"],
    "ENFP": ["크리에이터", "심리학자", "홍보 전문가"],
    # 필요한 MBTI 계속 추가 가능
}

# 제목
st.title("✨ MBTI 기반 진로 추천 웹앱")

# MBTI 입력
mbti = st.selectbox("당신의 MBTI를 선택하세요:", options=list(career_dict.keys()))

# 추천 버튼
if st.button("추천 직업 보기"):
    st.subheader(f"🔮 {mbti} 유형에게 어울리는 직업은?")
    for job in career_dict[mbti]:
        st.write(f"- {job}")
