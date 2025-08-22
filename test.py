import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI 건강 체크", page_icon="🩺")
st.title("🩺 간단한 자가 건강 체크 & 상처 처치 가이드")

st.write("증상을 입력하거나 상처 사진을 올리면, 기본적인 관리법을 안내합니다.")

# ------------------------------
# 1. 증상 텍스트 입력
# ------------------------------
symptom = st.text_input("현재 느끼는 증상을 입력하세요 (예: 기침, 발열, 두통, 피로 등)")

if st.button("건강 체크하기"):
    if symptom == "":
        st.warning("❗ 증상을 입력해주세요.")
    else:
        symptom_lower = symptom.lower()  # 대소문자 구분 제거
        if "기침" in symptom_lower or "발열" in symptom_lower:
            st.error("호흡기 관련 증상이 의심됩니다.")
            st.write("- 충분한 수분 섭취와 휴식을 취하세요.")
            st.write("- 증상이 3일 이상 지속되면 병원 방문을 권장합니다.")
        elif "두통" in symptom_lower:
            st.info("긴장성 두통 가능성이 있습니다.")
            st.write("- 수면과 스트레스를 관리하세요.")
            st.write("- 통증이 지속되면 신경과 진료를 고려하세요.")
        elif "피로" in symptom_lower or "피곤" in symptom_lower:
            st.info("과로 또는 생활 습관과 관련 있을 수 있습니다.")
            st.write("- 규칙적인 식사와 가벼운 운동을 해보세요.")
            st.write("- 지속된다면 건강검진이 필요할 수 있습니다.")
        elif "복통" in symptom_lower:
            st.info("소화기 관련 증상일 수 있습니다.")
            st.write("- 가벼운 식사와 충분한 휴식을 취하세요.")
            st.write("- 지속되면 내과 진료를 권장합니다.")
        elif "어지럼" in symptom_lower or "어지럼증" in symptom_lower:
            st.info("저혈압이나 빈혈, 탈수 등과 관련 있을 수 있습니다.")
            st.write("- 안정 후 수분과 음식 섭취를 권장합니다.")
            st.write("- 증상이 반복되면 병원 진료를 권장합니다.")
        elif "구토" in symptom_lower:
            st.warning("위장관 관련 증상일 수 있습니다.")
            st.write("- 수분을 충분히 섭취하고 무리한 음식은 피하세요.")
            st.write("- 증상이 계속되면 내과 진료를 권장합니다.")
        elif "속쓰림" in symptom_lower:
            st.info("소화불량이나 위장 질환과 관련 있을 수 있습니다.")
            st.write("- 자극적인 음식 피하고, 소화 잘 되는 음식 섭취하세요.")
            st.write("- 지속되면 소화기 내과 진료를 권장합니다.")
        elif "생리통" in symptom_lower:
            st.info("생리와 관련된 통증일 수 있습니다.")
            st.write("- 따뜻한 찜질과 휴식을 권장합니다.")
            st.write("- 통증이 심하면 진통제 복용 또는 산부인과 상담을 고려하세요.")
        else:
            st.write("해당 증상은 자가 체크 항목에는 없어요.")
            st.write("✅ 증상이 계속된다면 가까운 의료기관을 방문하세요.")

st.markdown("---")

# ------------------------------
# 2. 상처 이미지 업로드
# ------------------------------
uploaded_file = st.file_uploader("상처 부위 사진을 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드된 상처 사진", use_column_width=True)

    st.subheader("상처 유형을 선택하세요")
    wound_type = st.selectbox("상처 유형", ["찰과상(까진 상처)", "절상(칼/날카로운 것에 베인 상처)", "화상", "기타"])

    if wound_type == "찰과상(까진 상처)":
        st.success("👉 처치법: 깨끗한 물로 세척 후, 연고를 바르고 밴드를 붙입니다.")
    elif wound_type == "절상(칼/날카로운 것에 베인 상처)":
        st.success("👉 처치법: 출혈이 멈출 때까지 압박 후, 소독약 처리 후 연고와 거즈를 덮습니다.")
    elif wound_type == "화상":
        st.success("👉 처치법: 흐르는 시원한 물에 10~15분 이상 식힌 후, 화상 전용 연고를 바릅니다.")
    else:
        st.info("👉 처치법: 상처 종류에 따라 다르니, 가까운 약국이나 병원을 방문하세요.")

st.caption("⚠️ 이 프로그램은 교육용 참고 자료이며, 실제 진단과 치료는 반드시 의료 전문가의 진료가 필요합니다.")
