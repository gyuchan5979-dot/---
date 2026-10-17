/* =========================================================
   드리움 공통 헤더 · 푸터 (한 곳에서 관리)
   -------------------------------------------------------
   ▸ 헤더/푸터 내용을 바꾸려면 이 파일만 수정하면 전 페이지 반영.
   ▸ 새 지역 페이지 완성 시 COMPLETED_AREAS 에 한 줄 추가.
      규칙: "지역명": "파일명.html",  ← 콜론(:)과 끝 쉼표(,) 꼭!
            맨 마지막 줄만 쉼표 없음.
   ========================================================= */

/* ✅ 완성된 지역 페이지만 등록 */
var COMPLETED_AREAS = {
  "강남": "area-gangnam.html",
  "서초": "area-seocho.html",
  "송파": "area-songpa.html",
  "강동": "area-gangdong.html",
  "성동": "area-seongdong.html",
  "용산": "area-yongsan.html",
  "마포": "area-mapo.html",
  "서대문": "area-seodaemun.html",
  "영등포": "area-yeongdeungpo.html",
  "동작": "area-dongjak.html",
  "양천": "area-yangcheon.html",
  "강서": "area-gangseo.html",
  "구로": "area-guro.html",
  "금천": "area-geumcheon.html",
  "광명": "area-gwangmyeong.html",
  "부천": "area-bucheon.html",
  "안양": "area-anyang.html",
  "시흥": "area-siheung.html",
  "분당": "area-bundang.html",
  "판교": "area-pangyo.html",
  "부평": "area-bupyeong.html",
  "인천서구": "area-incheon-seogu.html",
  "계양": "area-gyeyang.html",
  "남동": "area-namdong.html",
  "관악": "area-gwanak.html",
  "노원": "area-nowon.html",
  "광진": "area-gwangjin.html",
};

/* 푸터에 노출할 전체 지역 순서 (서울 → 경기 → 인천) */
var ALL_AREAS = [
  "강남","서초","송파","강동","강서","양천","영등포","마포","용산","성동",
  "광진","동작","관악","구로","금천","동대문","중랑","성북","강북","도봉",
  "노원","은평","서대문","종로","중구",
  "광명","부천","안양","시흥","분당","판교","과천","산본","일산",
  "부평","인천서구","계양","남동"
];

var areaLinks = ALL_AREAS.map(function (name) {
  return COMPLETED_AREAS[name]
    ? '<a href="' + COMPLETED_AREAS[name] + '">' + name + '</a>'
    : name;
}).join(" · ");

/* ===== 공통 헤더 (상단 알림바 + 헤더) ===== */
var headerHTML = ''
+ '<div class="top-bar">'
+ '  <div class="container">'
+ '    <span class="top-item">🏠 수도권 전 지역 무료 방문 견적</span>'
+ '    <span class="divider">|</span>'
+ '    <span class="top-item">📞 010-8353-5979</span>'
+ '    <span class="divider">|</span>'
+ '    <span class="top-item">💬 카톡 상담 가능</span>'
+ '  </div>'
+ '</div>'
+ '<header class="site-header">'
+ '  <div class="container header-inner">'
+ '    <a href="index.html" class="logo">'
+ '      <img src="images/logo.png" alt="드리움 커튼&블라인드">'
+ '    </a>'
+ '    <nav class="main-nav" id="mainNav">'
+ '      <ul>'
+ '        <li><a href="index.html">홈</a></li>'
+ '        <li><a href="gallery.html">시공 사례</a></li>'
+ '        <li><a href="products.html">제품 안내</a></li>'
+ '        <li><a href="blog.html">블로그</a></li>'
+ '        <li><a href="about.html">회사 소개</a></li>'
+ '        <li><a href="faq.html">자주 묻는 질문</a></li>'
+ '        <li><a href="inquiry.html">견적 문의</a></li>'
+ '      </ul>'
+ '    </nav>'
+ '    <button class="menu-toggle" id="menuToggle" aria-label="메뉴 열기"><span></span><span></span><span></span></button>'
+ '  </div>'
+ '</header>';

/* ===== 공통 푸터 ===== */
var footerHTML = ''
+ '<footer class="site-footer">'
+ '  <div class="container">'
+ '    <div class="footer-grid">'
+ '      <div class="footer-col">'
+ '        <h4 class="footer-logo">드리움 커튼&블라인드</h4>'
+ '        <p class="footer-slogan">창에 드리운 빛,<br>공간을 디자인하다</p>'
+ '        <div class="footer-contact">'
+ '          <p>📞 010-8353-5979</p>'
+ '          <p>✉️ wh597979@naver.com</p>'
+ '          <p>🕐 연중무휴 24시 상담</p>'
+ '        </div>'
+ '      </div>'
+ '      <div class="footer-col">'
+ '        <h4>바로가기</h4>'
+ '        <ul>'
+ '          <li><a href="index.html">홈</a></li>'
+ '          <li><a href="gallery.html">시공 사례</a></li>'
+ '          <li><a href="products.html">제품 안내</a></li>'
+ '          <li><a href="blog.html">블로그</a></li>'
+ '          <li><a href="about.html">회사 소개</a></li>'
+ '          <li><a href="faq.html">자주 묻는 질문</a></li>'
+ '          <li><a href="inquiry.html">견적 문의</a></li>'
+ '        </ul>'
+ '      </div>'
+ '      <div class="footer-col">'
+ '        <h4><a href="areas.html" style="color:inherit;">시공 지역 →</a></h4>'
+ '        <p class="footer-area">서울 · 경기 · 인천</p>'
+ '        <p class="footer-keywords">' + areaLinks + '</p>'
+ '      </div>'
+ '    </div>'
+ '    <div class="footer-bottom">'
+ '      <p>© 2026 드리움 커튼&블라인드. All Rights Reserved.</p>'
+ '    </div>'
+ '  </div>'
+ '</footer>';

(function () {
  /* 1) 헤더 주입 (자리표시 #site-header 가 있는 페이지만) */
  var headerInjected = false;
  var headerMount = document.getElementById("site-header");
  if (headerMount) {
    headerMount.outerHTML = headerHTML;
    headerInjected = true;
  }

  /* 2) 푸터 주입 */
  var footerMount = document.getElementById("site-footer");
  if (footerMount) {
    footerMount.outerHTML = footerHTML;
  }

  /* 3) 관련글 섹션(블로그 글)과 푸터 간격 확보 */
  var relatedSec = document.querySelector(".related-section");
  if (relatedSec) {
    relatedSec.style.marginBottom = "80px";
  }

  /* 4) 현재 페이지 메뉴 강조 (헤더가 주입됐든 원래 있든 모두 적용) */
  var current = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".main-nav a").forEach(function (a) {
    if (a.getAttribute("href") === current) {
      a.style.color = "var(--color-primary)";
      a.style.fontWeight = "700";
    }
  });

  /* 5) 헤더 이벤트는 "이 파일이 헤더를 주입한 경우에만" 바인딩
        (아직 안 바꾼 페이지는 main.js가 담당 → 중복 방지) */
  if (headerInjected) {
    var menuToggle = document.getElementById("menuToggle");
    var mainNav = document.getElementById("mainNav");
    if (menuToggle && mainNav) {
      menuToggle.addEventListener("click", function () {
        mainNav.classList.toggle("active");
      });
      mainNav.querySelectorAll("a").forEach(function (link) {
        link.addEventListener("click", function () {
          mainNav.classList.remove("active");
        });
      });
    }
    var header = document.querySelector(".site-header");
    if (header) {
      window.addEventListener("scroll", function () {
        header.style.boxShadow =
          window.scrollY > 10 ? "0 2px 8px rgba(0,0,0,0.06)" : "none";
      });
    }
  }
})();