import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI 건강 체크", page_icon="🩺")
st.title("🩺✨ 간단한 자가 건강 체크 & 상처 처치 가이드 ✨")

st.markdown("증상을 입력하거나 상처 사진을 올리면, 기본적인 관리법을 안내해드려요 😊")

# ------------------------------
# 1. 증상 입력
# ------------------------------
symptom = st.text_input("💬 지금 어떤 증상이 있나요? (예: 나 속이 쓰려, 배 아파, 토할 것 같아 등)")

if st.button("🔍 건강 체크하기"):
    if symptom.strip() == "":
        st.warning("⚠️ 증상을 입력해주세요!")
    else:
        symptom_lower = symptom.lower()

        if any(word in symptom_lower for word in ["배 아파", "복통", "배가 아파"]):
            st.error("🤢 복통 증상이 의심돼요.")
            st.write("👉 따뜻한 찜질을 해보고, 심한 경우 소화기 내과를 방문하세요.")

        elif any(word in symptom_lower for word in ["어지러", "빙빙", "현기증"]):
            st.warning("😵 어지럼증이 나타나고 있어요.")
            st.write("👉 바로 앉거나 누워서 휴식을 취하고, 수분을 섭취하세요.")

        elif any(word in symptom_lower for word in ["심장", "두근", "심장 두근"]):
            st.error("❤️ 심장 두근거림이 의심돼요.")
            st.write("👉 불안이나 카페인 때문일 수 있으나, 지속되면 심장 내과를 꼭 방문하세요.")

        elif any(word in symptom_lower for word in ["구토", "토할", "토 나올"]):
            st.error("🤮 구토 증상이 있어요.")
            st.write("👉 탈수를 막기 위해 소량씩 수분을 섭취하세요.")

        elif any(word in symptom_lower for word in ["속쓰림", "가슴 쓰림", "더부룩"]):
            st.warning("🔥 속쓰림 증상이 있어요.")
            st.write("👉 기름진 음식, 커피, 야식은 피하세요.")

        elif any(word in symptom_lower for word in ["생리통", "월경통", "배 아픈데 생리"]):
            st.info("🌸 생리통 증상이 의심돼요.")
            st.write("👉 따뜻한 찜질이나 진통제를 복용하세요.")

        else:
            st.write("🤔 입력하신 증상은 현재 데이터에 없어요. 다른 표현으로 시도해주세요!")

# ------------------------------
# 2. 상처 사진 업로드
# ------------------------------
st.markdown("---")
st.subheader("📸 상처 사진 업로드")

uploaded_file = st.file_uploader("상처 부위를 찍어서 올려주세요.", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드한 상처 사진", use_column_width=True)

    st.success("✅ 상처가 확인되었습니다. 기본 처치 방법을 안내드릴게요.")
    st.write("- 깨끗한 물로 상처 부위를 세척하세요.")
    st.write("- 소독약을 바르고, 거즈나 밴드로 덮어주세요.")
    st.write("- 상처가 깊거나 출혈이 멈추지 않으면 병원을 방문하세요.")

