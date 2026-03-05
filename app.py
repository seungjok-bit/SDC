import streamlit as st
import pandas as pd
import os

# ------------------------------------------------
# 앱 설정
# ------------------------------------------------
ADMIN_PASSWORD = "space_admin_2026" # 배포 전 비밀번호를 꼭 변경하세요.
DATA_FILE = "founders_list.csv"

def main():
    st.set_page_config(page_title="우주데이터센터 연구회 발기인 신청", page_icon="🚀", layout="centered")

    st.title("🚀 우주데이터센터 연구회 발기인 신청")

    # 1. 발족 선언문 표시 (모바일 가독성을 위해 expander 또는 스크롤 컨테이너 사용)
    st.header("1. 발족 선언문")
    
    declaration_text = """
    **우주데이터센터 연구회 발족을 위한 선언문**

    전 세계는 지금 클라우드 컴퓨팅과 인공지능(AI)의 급속한 확산 속에서 새로운 전환점에 서 있습니다. 클라우드는 더 이상 단순한 IT 인프라가 아니라, 경제·산업·사회 전반을 재구성하는 핵심 기반으로 자리 잡았습니다. AI 기술의 발전은 의료, 금융, 제조, 국방, 문화 콘텐츠 등 거의 모든 영역에서 인간의 역량을 증폭시키고 있으며, 그 중심에는 고성능 컴퓨팅과 이를 지탱하는 데이터센터가 존재합니다.

    그러나 이러한 진보의 이면에는 심각한 한계가 드러나고 있습니다. 대규모 AI 모델 학습과 실시간 추론을 수행하는 클라우드 데이터센터는 막대한 전력을 소비하며, 냉각 시스템만으로도 전체 에너지 사용량의 상당 부분을 차지합니다. 데이터센터 전력 수요는 이미 국가 단위의 전력 소비와 맞먹는 수준으로 성장하고 있으며, 이는 탄소 중립과 지속가능성을 지향하는 인류의 목표와 정면으로 충돌하고 있습니다. 지상 기반 데이터센터 확장은 더 이상 무한히 지속 가능한 해법이 아닙니다.

    이제 우리는 질문해야 합니다. 지구라는 물리적·에너지적 한계를 넘어서는 새로운 컴퓨팅 패러다임은 가능한가? 그 대안으로 떠오르는 개념이 바로 우주 기반 데이터센터, 즉 우주데이터센터입니다.

    우주 공간은 사실상 무한에 가까운 태양 에너지를 제공하며, 대규모 부지 확보나 지역 갈등, 냉각을 위한 물 사용 문제에서도 자유롭습니다. 최근 민간 우주 산업의 비약적 발전은 이러한 상상을 현실적인 기술·산업 과제로 끌어올리고 있습니다. 재사용 발사체와 대형 수송 능력의 확보는, 대규모 컴퓨팅 모듈을 궤도에 배치하고 조립·운용하는 시나리오를 더 이상 공상에 머물지 않게 만들고 있습니다.

    그러나 우주데이터센터는 단순히 “데이터센터를 우주로 옮긴다”는 발상이 아닙니다. 궤도 환경에서의 방사선, 열 제어, 전력 안정성, 정비 가능성, 궤도 유지, 무정지 운영 등 수많은 기술적 모순과 난제가 얽힌 복합 시스템 공학의 결정체입니다. 특히 태양광 기반 상시 전력 공급을 위한 최적 궤도 설계, 방사선 내성 컴퓨팅 기술, 모듈형 서버 구조와 궤도 정비 체계, 대규모 방열 시스템 등은 선행 연구 없이는 접근조차 어려운 영역입니다.

    이에 우리는 학계, 산업계, 연구기관, 정책 전문가가 함께 참여하는 **「우주데이터센터 연구회」**를 발족합니다. 본 연구회는 우주 기반 클라우드 컴퓨팅의 기술적·경제적·환경적 타당성을 종합적으로 연구 토론하고, 단기적으로는 궤도 내 실증(PoC)을, 중장기적으로는 상용 우주데이터센터 구현을 목표로 합니다.

    우주데이터센터는 에너지 위기를 넘어, 인류의 디지털 문명이 확장될 새로운 공간을 여는 시도입니다. 우리는 이 도전을 통해 지속 가능한 AI·클라우드 시대의 기반을 구축하고, 대한민국이 차세대 우주·디지털 인프라 경쟁에서 선도적 역할과 우주 디지털 주권을 확립하는데 기여하고자 합니다. 지구의 한계를 넘어, 우주로 확장되는 컴퓨팅의 미래를 함께 설계할 동료 연구자와 산업 파트너 여러분의 참여를 기대합니다. 함께 힘찬 발걸음을 내디뎌, 미래를 향한 도전을 시작합시다.

    발기인 서울대학교 명예교수 김 승 조
    """
    
    # 선언문을 스크롤 가능한 상자 안에 배치
    st.markdown(f'<div style="height: 300px; overflow-y: scroll; padding: 15px; border: 1px solid #ccc; border-radius: 5px; background-color: #f9f9f9; color: #333;">{declaration_text.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)

    st.divider()

    # 2 & 3. 발기인 정보 입력 폼
    st.header("2. 발기인 참여 신청")
    st.write("발기인으로 참여를 원하시는 분들은 아래 정보를 입력 및 선택해 주십시오.")

    with st.form("application_form"):
        name = st.text_input("성명")
        affiliation = st.text_input("소속 (또는 전 소속)")
        contact = st.text_input("연락처 (휴대폰 번호)")
        dob = st.text_input("생년월일 (예: 19700101) *주민번호 대체")
        
        committee = st.selectbox(
            "희망 분과위원회 선택",
            [
                "선택해주세요",
                "우주데이터센터기획 정책 분과위원회",
                "위성설계기술 분과위원회",
                "대형태양광기술 및 전력관리 분과위원회",
                "위성열제어기술 분과위원회",
                "방사선차폐기술 분과위원회",
                "위성통신기술 분과위원회",
                "우주데이터센터 소프트웨어기술 분과위원회"
            ]
        )

        submit_button = st.form_submit_button("신청서 제출하기")

    if submit_button:
        if name and affiliation and contact and dob and committee != "선택해주세요":
            new_data = pd.DataFrame({
                "성명": [name],
                "소속": [affiliation],
                "연락처": [contact],
                "생년월일": [dob],
                "희망분과": [committee],
                "신청일시": [pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")]
            })

            if os.path.exists(DATA_FILE):
                df = pd.read_csv(DATA_FILE)
                df = pd.concat([df, new_data], ignore_index=True)
            else:
                df = new_data

            df.to_csv(DATA_FILE, index=False, encoding='utf-8-sig')
            st.success("✅ 발기인 신청이 성공적으로 완료되었습니다. 동참해 주셔서 감사합니다.")
        else:
            st.warning("⚠️ 누락된 항목이 있습니다. 모든 항목을 정확히 선택 및 입력해 주세요.")

    st.divider()

    # 4. 관리자 전용 다운로드
    st.header("🔐 관리자 전용 (명단 다운로드)")
    with st.expander("관리자 메뉴 열기"):
        pwd_input = st.text_input("비밀번호를 입력하세요", type="password")
        
        if pwd_input == ADMIN_PASSWORD:
            if os.path.exists(DATA_FILE):
                df = pd.read_csv(DATA_FILE)
                csv = df.to_csv(index=False, encoding='utf-8-sig')
                
                st.download_button(
                    label="📥 발기인 명단 다운로드 (Excel 호환 CSV)",
                    data=csv,
                    file_name='space_data_center_founders.csv',
                    mime='text/csv',
                )
            else:
                st.info("아직 등록된 발기인 데이터가 없습니다.")
        elif pwd_input:
            st.error("비밀번호가 일치하지 않습니다.")

if __name__ == "__main__":
    main()