# 드리움 지역 페이지 추가 생성 (area-guro.html 양식). 동 목록은 결앤빛 데이터, 소개 문장은 드리움용으로 새로 작성
import os, re, sys
sys.path.insert(0, "/home/user/test/_build")
from areas_more import MORE
import common as _c
MORE = [a for a in _c.AREAS if "dongs" in a and "picks" in a]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = open(os.path.join(ROOT, "area-guro.html"), encoding="utf-8").read()
CSS = TPL[TPL.index("<style>"):TPL.index("</style>") + 8]
TAIL = TPL[TPL.index("    <!-- CTA -->"):]

# 지역별 한 줄 특징 (드리움 전용 문장)
FEAT = {
 "동대문": "청량리 역세권 주상복합과 이문 · 휘경 뉴타운 입주 단지가 함께 있는 동네",
 "중랑": "면목 · 상봉 · 신내의 아파트와 빌라가 고르게 섞여 있어 창 형태가 다양한 동네",
 "성북": "길음 · 장위 뉴타운 대단지와 성북동 단독주택까지 주거 형태 폭이 넓은 동네",
 "강북": "미아 · 번동 아파트 단지와 북한산 자락 주택가가 어우러진 동네",
 "도봉": "창동 · 쌍문 · 방학의 오래된 단지가 많아 커튼 교체 수요가 꾸준한 동네",
 "은평": "은평뉴타운 · 수색 · 증산 재개발 단지 입주로 새 집 시공이 많은 동네",
 "종로": "평창 · 부암동 주택과 도심 오피스텔, 한옥까지 창 모양이 제각각인 동네",
 "중구": "신당 · 황학 · 약수의 아파트와 도심 오피스텔이 함께 있는 동네",
 "과천": "재건축 신축 단지와 지식정보타운 입주가 이어지는 동네",
 "산본": "1기 신도시 단지가 많아 오래 쓴 커튼 · 레일 교체 상담이 많은 동네",
 "일산": "정발산 · 마두 · 백석의 넓은 거실 통창 아파트가 많은 동네",
 "고양": "덕양 · 삼송 · 원흥 · 지축 신축 단지가 빠르게 늘어난 동네",
 "김포": "한강신도시 · 걸포 · 풍무 신축 아파트 입주가 이어지는 동네",
 "파주": "운정신도시 대단지가 많아 입주 시기 맞춤 시공이 많은 동네",
 "의정부": "민락 · 고산 · 신곡 신축 단지와 기존 주거지가 함께 있는 동네",
 "양주": "옥정 · 회천 신도시 입주로 집 전체 시공 문의가 많은 동네",
 "남양주": "다산 · 별내 · 호평 신도시 단지가 넓게 퍼져 있는 동네",
 "구리": "인창 · 교문 · 갈매 단지가 모여 있는 서울 동쪽 생활권",
 "하남": "미사강변 · 위례 · 감일 신도시 입주 단지가 많은 동네",
 "위례": "송파 · 성남 · 하남에 걸친 신도시로 통창 거실이 많은 동네",
 "광주": "태전 · 오포 · 경안의 아파트와 전원주택이 함께 있는 동네",
 "의왕": "백운호수 · 포일 · 내손 신축 단지가 늘어난 동네",
 "평촌": "범계 · 평촌 · 인덕원 1기 신도시 단지가 모인 안양 동안구 생활권",
 "수원": "광교 · 영통 · 장안 · 권선까지 신도시와 원도심이 함께 있는 동네",
 "용인": "수지 · 기흥 · 동백 · 처인 대단지가 넓게 퍼져 있는 동네",
 "동탄": "동탄1 · 2신도시 대단지와 고층 주상복합이 많은 동네",
 "화성": "봉담 · 향남 · 남양 신축 단지 입주가 이어지는 동네",
 "오산": "세교 신도시와 원동 · 오산동 주거지가 함께 있는 동네",
 "평택": "고덕국제신도시 · 소사벌 · 비전동 신축 단지가 많은 동네",
 "안산": "고잔 · 초지 · 중앙동 재건축 단지가 늘고 있는 동네",
 "이천": "중리 · 안흥 · 증포동 신축 아파트가 늘어난 동네",
 "송도": "국제도시 고층 통창 아파트와 오피스텔이 많은 동네",
 "연수": "연수 · 동춘 · 옥련의 자리 잡은 단지와 송도 생활권이 함께 있는 동네",
 "미추홀": "주안 · 용현 · 학익 재개발 단지 입주가 이어지는 동네",
 "영종": "영종하늘도시 신축 단지가 많고 바닷바람이 강한 동네",
}
GROUP = {"서울": "서울 북부·동부", "경기": "경기", "인천": "인천"}
PROD = {"린넨 커튼": ("sheer", "sheer-white-4-a.png", "쉬폰·린넨 커튼"), "쉬폰 커튼": ("sheer", "sheer-white-2-a.png", "쉬폰커튼"),
        "암막 커튼": ("blackout", "blackout-navy-a.png", "암막커튼"), "콤비 블라인드": ("combi", "combi-beige-a.png", "콤비블라인드"),
        "우드 블라인드": ("wood", "wood-natural-a.png", "우드블라인드"), "허니콤 블라인드": ("roll", "roll-white-a.png", "롤블라인드"),
        "롤스크린": ("roll", "roll-white-a.png", "롤블라인드"), "전동 커튼 · 블라인드": ("dimout", "dimout-grey-a.png", "생활암막커튼")}
ALL6 = [("sheer", "sheer-white-2-a.png", "쉬폰커튼"), ("blackout", "blackout-navy-a.png", "암막커튼"), ("dimout", "dimout-grey-a.png", "생활암막커튼"),
        ("wood", "wood-natural-a.png", "우드블라인드"), ("combi", "combi-beige-a.png", "콤비블라인드"), ("roll", "roll-white-a.png", "롤블라인드")]
HERO_IMG = ["dimout-ivory-a.png", "sheer-white-4-a.png", "combi-white-a.png", "blackout-beige-a.png", "wood-white-a.png", "roll-beige-a.png"]

def nm(a):  # 화면 표기 이름
    f = a["full"].split()
    return f[-1] if a["region"] != "경기" or a["key"] in ("일산", "평촌", "산본", "동탄", "위례") else a["key"] + ("시" if not a["key"].endswith("시") else "")

missing = [a for a in MORE if not os.path.exists(os.path.join(ROOT, a["file"]))]
made = []
for i, a in enumerate(missing):
    k = a["key"]; name = {"평촌": "평촌", "산본": "산본", "일산": "일산", "동탄": "동탄", "위례": "위례", "송도": "송도", "영종": "영종도"}.get(k) or (a["full"].split()[-1] if a["region"] != "경기" else a["full"].split()[1])
    dongs = a["dongs"]; d4 = "·".join(x.replace("동", "") if len(x) > 2 else x for x in dongs[:4])
    feat = FEAT[k]
    far = "광명 본사에서 바로 출발해" if a["region"] != "서울" else "광명 본사에서 출발해 서울 전역을"
    picks = []
    for p in a["picks"]:
        t = PROD.get(p)
        if t and t not in picks: picks.append(t)
    picks += [x for x in ALL6 if x not in picks]
    picks = picks[:6]
    img = HERO_IMG[i % len(HERO_IMG)]
    url = f"https://deurium.co.kr/{a['file']}"
    kws = [f"{name} 커튼", f"{name} 블라인드", f"{name} 커튼 시공"] + [f"{d} 커튼" for d in dongs[:3]] + [f"{name} 암막커튼", f"{name} 콤비블라인드", f"{name} 맞춤커튼"]
    area_served = ",\n".join([f'        {{ "@type": "City", "name": "{name}" }}'] + [f'        {{ "@type": "Place", "name": "{d}" }}' for d in dongs[:6]])
    prods = "\n".join(f'''                <a href="products.html#{p[0]}" class="ap-card">
                    <div class="ap-thumb"><img src="images/products/{p[1]}" alt="{name} {p[2]} 시공" loading="lazy"></div>
                    <span class="ap-label">{p[2]}</span>
                </a>''' for p in picks)
    tags = "\n".join(f'            <span class="dong-tag"><strong>📍</strong> {d}</span>' for d in dongs)
    html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{name} 커튼·블라인드 시공 | 무료 방문 견적 | 드리움 커튼&블라인드</title>
	<meta name="description" content="{name} 커튼·블라인드 맞춤 시공. {', '.join(dongs[:4])} 등 {a['full']} 전 지역 무료 방문 견적. 광명 본사 직접 실측 · 시공, 쉬폰 · 암막커튼, 콤비 · 우드블라인드 맞춤 제작.">
	<meta name="keywords" content="{', '.join(kws)}">
	<link rel="canonical" href="{url}">

	<meta property="og:title" content="{name} 커튼·블라인드 시공 | 드리움">
	<meta property="og:description" content="{name} 전 지역 무료 방문 견적, 맞춤 커튼·블라인드 시공">
	<meta property="og:image" content="https://deurium.co.kr/images/products/{img}">
	<meta property="og:url" content="{url}">

    <script type="application/ld+json">
	{{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "@id": "{url}",
    "name": "드리움 커튼&블라인드 - {name}",
    "image": "https://deurium.co.kr/images/products/{img}",
    "description": "{name} 커튼·블라인드 전문 시공, 무료 방문 견적",
    "telephone": "010-8353-5979",
    "priceRange": "₩₩",
    "areaServed": [
{area_served}
    ],
    "url": "{url}"
	}}
</script>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css">
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
    {CSS}
</head>
<body>

    <!-- 공통 헤더 (includes.js가 채움) -->
    <div id="site-header"></div>

    <!-- 지역 히어로 -->
    <section class="area-hero">
    <div class="container">
        <span class="area-badge">📍 {name} 전 지역 시공</span>
        <h1><span class="highlight">{name}</span> 커튼·블라인드<br>맞춤 시공</h1>
        <p>{', '.join(dongs[:4])} 등 {name} 어디든<br>무료로 방문해 직접 실측합니다</p>
        <div class="area-hero-buttons">
            <a href="inquiry.html" class="btn btn-primary">📋 무료 견적 받기</a>
            <a href="tel:010-8353-5979" class="btn btn-outline">📞 010-8353-5979</a>
        </div>
    </div>
	</section>

    <!-- 지역 소개 -->
    <section class="area-info">
        <div class="container">
            <div class="area-info-grid">
                <div class="area-info-text">
					<h2>{name} 커튼·블라인드<br>드리움이 찾아갑니다</h2>
					<p>{name}은(는) <strong>{feat}</strong>입니다. 같은 단지라도 향과 층에 따라 빛이 들어오는 양이 달라서, 드리움은 꼭 현장에서 창을 직접 보고 원단을 추천해 드려요.</p>
					<p>{far} <strong>{name} 전 지역</strong>을 방문하고, 정밀 실측부터 제작 · 시공까지 직접 책임집니다.</p>
					<p>낮에는 빛을 부드럽게 들이는 쉬폰부터 숙면을 위한 암막커튼, 관리 쉬운 콤비 · 우드블라인드까지 — <strong>{name} 무료 방문 견적</strong>으로 시작해 보세요.</p>
			</div>
			<div class="area-info-img">
				<img src="images/products/{img}" alt="{name} 커튼 블라인드 시공 예시">
			</div>
            </div>
        </div>
    </section>

    <!-- 동네 리스트 -->
    <section class="area-dong">
    <div class="container">
        <h2>{name} 어디든 방문합니다</h2>
        <p>{a['full']} 전 지역 무료 방문 견적 가능</p>
        <div class="dong-list">
{tags}
        </div>
    </div>
</section>

    <!-- {name} 인기 시공 제품 -->
    <section class="area-products">
        <div class="container">
            <div class="section-head">
                <p class="section-tag">PRODUCTS</p>
                <h2 class="section-title">{name} 인기 시공 제품</h2>
                <p class="section-sub">{name} 고객님들이 많이 찾는 커튼·블라인드</p>
            </div>
            <div class="ap-grid">
{prods}
            </div>
            <div class="ap-more">
                <a href="products.html" class="btn btn-outline">전체 제품 보기 →</a>
            </div>
        </div>
    </section>

''' + TAIL.replace("구로구 무료 방문 견적 신청", f"{name} 무료 방문 견적 신청")
    open(os.path.join(ROOT, a["file"]), "w", encoding="utf-8").write(html)
    made.append((a, name, d4))

# areas.html 카드 추가 (각 지역 그룹의 '그 외' 카드 앞)
p = os.path.join(ROOT, "areas.html"); s = open(p, encoding="utf-8").read()
titles = {"서울": "🏙️ 서울 지역", "경기": "🌳 경기 지역", "인천": "🌊 인천 지역"}
for reg, title in titles.items():
    cards = "".join(f'''                    <a href="{a['file']}" class="area-link-card active">
                        <div class="area-link-icon">📍</div>
                        <h3>{n}</h3>
                        <p>{d}</p>
                        <span class="badge go">바로가기 →</span>
                    </a>
''' for a, n, d in made if a["region"] == reg and a["file"] not in s)
    gi = s.index(title); di = s.index('                    <div class="area-link-card disabled">', gi)
    s = s[:di] + cards + s[di:]
open(p, "w", encoding="utf-8").write(s)

# includes.js 지역 링크
p = os.path.join(ROOT, "js/includes.js"); s = open(p, encoding="utf-8").read()
comp = "".join(f'  "{a["key"]}": "{a["file"]}",\n' for a, n, d in made if f'"{a["key"]}":' not in s)
s = s.replace("};\n\n/* 푸터에 노출할 전체 지역 순서", comp + "};\n\n/* 푸터에 노출할 전체 지역 순서", 1)
m = re.search(r"var ALL_AREAS = \[(.*?)\];", s, re.S); cur = re.findall(r'"([^"]+)"', m.group(1))
order = {"서울": [], "경기": [], "인천": []}
for n in cur:
    r = "인천" if n in ("부평", "인천서구", "계양", "남동") else ("경기" if n in ("광명", "부천", "안양", "시흥", "분당", "판교", "과천", "산본", "일산") else "서울")
    order[r].append(n)
for a, n, d in made:
    if a["key"] not in cur: order[a["region"]].append(a["key"])
new = "var ALL_AREAS = [\n  " + ",\n  ".join(",".join(f'"{x}"' for x in order[r]) for r in ("서울", "경기", "인천")) + "\n];"
s = s[:m.start()] + new + s[m.end():]
open(p, "w", encoding="utf-8").write(s)

# sitemap
p = os.path.join(ROOT, "sitemap.xml"); s = open(p, encoding="utf-8").read()
for a, n, d in made:
    loc = f"https://deurium.co.kr/{a['file']}"
    if loc not in s:
        s = s.replace("</urlset>", f"    <url>\n        <loc>{loc}</loc>\n        <lastmod>2026-10-22</lastmod>\n        <changefreq>monthly</changefreq>\n        <priority>0.8</priority>\n    </url>\n\n</urlset>")
open(p, "w", encoding="utf-8").write(s)
print("made", len(made), [n for a, n, d in made])
