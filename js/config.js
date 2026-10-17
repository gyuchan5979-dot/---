/* ============================================
   드리움 커튼&블라인드 - 사이트 설정
   여기만 수정하면 모든 페이지에 자동 반영됩니다!
   ============================================ */

const SITE_CONFIG = {
    // 📞 연락처
    phone: "010-8353-5979",
    email: "wh597979@naver.com",

    // 💬 카카오 채널
    kakaoUrl: "https://pf.kakao.com/_PJixjX",

    // 📋 Formspree (문의 폼)
    formspreeId: "xlgvaknw",

    // 🏢 회사 정보
    companyName: "드리움 커튼&블라인드",
    ceo: "조규찬",
    address: "서울 전 지역 · 경기 일부",

    // ⏰ 영업 시간
    businessHours: "연중무휴 24시 상담"
};

// 페이지가 로드되면 자동으로 모든 링크에 설정값 적용
document.addEventListener('DOMContentLoaded', () => {

    // 1. 전화번호 링크 자동 설정
    document.querySelectorAll('a[href^="tel:"], .float-phone, [data-link="phone"]').forEach(el => {
        el.href = "tel:" + SITE_CONFIG.phone;
    });

    // 2. 이메일 링크 자동 설정
    document.querySelectorAll('a[href^="mailto:"], [data-link="email"]').forEach(el => {
        el.href = "mailto:" + SITE_CONFIG.email;
    });

    // 3. 카카오 채널 링크 자동 설정 (.btn-kakao, .float-kakao, data-link="kakao" 모두 자동)
    document.querySelectorAll('.btn-kakao, .float-kakao, [data-link="kakao"]').forEach(el => {
        el.href = SITE_CONFIG.kakaoUrl;
        el.target = "_blank";
    });

    // 4. Formspree 폼 자동 설정 (inquiry.html에서만 작동)
    const inquiryForm = document.querySelector('.inquiry-form');
    if (inquiryForm) {
        inquiryForm.action = `https://formspree.io/f/${SITE_CONFIG.formspreeId}`;
    }

    // 5. 텍스트로 표시되는 전화번호 자동 업데이트 (data-text="phone" 속성 있는 곳)
    document.querySelectorAll('[data-text="phone"]').forEach(el => {
        el.textContent = SITE_CONFIG.phone;
    });

    // 6. 텍스트로 표시되는 이메일 자동 업데이트
    document.querySelectorAll('[data-text="email"]').forEach(el => {
        el.textContent = SITE_CONFIG.email;
    });
});