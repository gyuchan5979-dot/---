# 드리움 커튼&블라인드 홈페이지 (deurium.co.kr)

카페24 웹호스팅의 정적 HTML 사이트입니다. `main` 브랜치에 반영되면
`.github/workflows/deploy.yml`이 FTP로 변경된 파일만 자동 업로드합니다.
이 파일(CLAUDE.md)과 `.github/`는 서버에 올라가지 않습니다.

사장님(조규찬 대표)이 사진과 현장 정보를 채팅으로 보내면 아래 절차대로
시공 후기를 추가합니다. 답변은 한국어로, 쉬운 말로 합니다.

## 사이트 구조

- `blog-N-slug.html` : 블로그 글. 실제 시공 사례는 "시공 후기" 카테고리 글로 올림 (blog-8 ~ blog-14 참고)
- `blog.html` : 블로그 목록. 카드(`<a class="blog-card" data-cat="review">`)를 "모든 글" 맨 위에 추가
- `sitemap.xml` : 새 글 `<url>` 추가 (`lastmod`는 작성일)
- `images/blog/` : 시공 후기 사진 (`{현장slug}-{번호}.jpeg`)
- `images/cases/` : 지역 페이지(`area-*.html`)에서 쓰는 제품별 사진 (`{제품}-{색상}-{공간}-{번호}.jpeg`)
- `gallery.html` : `galleryData` 배열로 렌더링 (현재 case-1~12는 예시 데이터)
- `js/config.js` : 전화번호, 카카오, Formspree 등 공통 설정
- `js/includes.js` : 공통 헤더/푸터

## 시공 후기 추가 절차

1. 다음 번호 확인: `ls blog-*.html` 중 가장 큰 번호 + 1
2. 사진을 `images/blog/{slug}-{1..n}.jpeg`로 저장. 긴 변 1600px, 품질 82 정도로 줄여 용량을 300KB 내외로 맞춤
3. 가장 최근 시공 후기(예: `blog-14-wonjong-sheer.html`)를 복사해 새 글 작성
   - `<title>`, description, keywords, og:* (og:image 확장자는 실제 파일과 일치), og:url
   - post-hero(카테고리·제목·📍위치·🪟제품·📅날짜), 요약 박스, 사진별 figure + 설명, 태그, 관련 글
   - 지역명·아파트명·제품명을 자연스럽게 넣어 검색 노출(SEO)을 고려
4. `blog.html` "모든 글" 맨 위에 카드 추가 (NEW 배지), 오래된 카드의 NEW 배지는 최근 5~6개만 유지
5. `sitemap.xml`에 새 글 추가
6. 깨진 링크/이미지 경로 확인 후 커밋 → `main`에 반영되면 자동 배포
