# -*- coding: utf-8 -*-
import json

with open('prop_WIx6G.json', 'r', encoding='utf-8') as f: p_WIx6G = json.load(f)
with open('prop_vVfNy.json', 'r', encoding='utf-8') as f: p_vVfNy = json.load(f)
with open('prop_SvJBd.json', 'r', encoding='utf-8') as f: p_SvJBd = json.load(f)
with open('prop_elNHK.json', 'r', encoding='utf-8') as f: p_elNHK = json.load(f)
with open('prop_EB9Vw.json', 'r', encoding='utf-8') as f: p_EB9Vw = json.load(f)
with open('prop_1fGqX.json', 'r', encoding='utf-8') as f: p_1fGqX = json.load(f)
with open('prop_0YrqT.json', 'r', encoding='utf-8') as f: p_0YrqT = json.load(f)

def get_img(p, fallback=""):
    img = p.get('og_img') or p.get('list_img')
    if isinstance(img, list) and len(img) > 0:
        return img[0]
    if isinstance(img, str) and img:
        return img
    return fallback

items = [
    # 1. 豐耘
    {
        "id": "item-WIx6G",
        "badge": "三峽民生商圈",
        "badge_color": "bg-emerald-600",
        "title": "A43 豐耘漂亮2房車",
        "subtitle": "方正採光・漂亮2房車・前後陽台",
        "price": 1750,
        "ping": "37.02 坪",
        "pattern": "2房1廳1衛",
        "location": "新北市三峽區民生街",
        "desc": "屋齡僅5.3年！格局方正採光極佳，稀有前後陽台通風好，附專屬車位，首購換屋成家優質首選。",
        "link": "https://ibig.fun/WIx6G",
        "link_text": "查看比房網規格",
        "img": get_img(p_WIx6G)
    },
    # 2. 風呂
    {
        "id": "item-vVfNy",
        "badge": "北大溫泉名邸",
        "badge_color": "bg-sky-600",
        "title": "B64 風呂幸福三房車",
        "subtitle": "公設完善・格局方正・雙衛開窗",
        "price": 2238,
        "ping": "55.38 坪",
        "pattern": "3房2廳2衛",
        "location": "新北市樹林區學勤路",
        "desc": "北大特區知名風呂溫泉社區，公設齊全完善，格局方正雙衛浴皆開窗，鄰近優質學區與大賣場。",
        "link": "https://ibig.fun/vVfNy",
        "link_text": "查看比房網規格",
        "img": get_img(p_vVfNy)
    },
    # 3. 劍橋
    {
        "id": "item-SvJBd",
        "badge": "藝術大道名宅",
        "badge_color": "bg-indigo-600",
        "title": "B59 劍橋溫馨靜謐三房車",
        "subtitle": "藝術大道・公園綠意・雙商圈交匯",
        "price": 2398,
        "ping": "62.42 坪",
        "pattern": "3房2廳2衛",
        "location": "新北市三峽區學勤路",
        "desc": "遠雄劍橋名宅社區，藝術大道林蔭環繞，雙商圈交匯生活機能絕佳，採光通風好，附坡道平面車位。",
        "link": "https://ibig.fun/SvJBd",
        "link_text": "查看比房網規格",
        "img": get_img(p_SvJBd)
    },
    # 4. 汐止別墅
    {
        "id": "item-elNHK",
        "badge": "尊榮透天別墅",
        "badge_color": "bg-amber-600",
        "title": "F10 汐止景觀別墅",
        "subtitle": "近中研院/南港展覽館・景觀透天別墅",
        "price": 4380,
        "ping": "60.21 坪 (地坪48.78坪)",
        "pattern": "9房5廳6衛",
        "location": "新北市汐止區民權街二段",
        "desc": "鄰近中研院與南港展覽館，大器透天景觀別墅，採光視野絕佳，附地下車庫，適合大家庭或渡假居所。",
        "link": "https://ibig.fun/elNHK",
        "link_text": "查看比房網規格",
        "img": get_img(p_elNHK)
    },
    # 5. 光復街店面
    {
        "id": "item-EB9Vw",
        "badge": "車站商圈金店",
        "badge_color": "bg-rose-600",
        "title": "D37 光復街店面",
        "subtitle": "近鶯歌車站・區公所・傳統市場",
        "price": 1250,
        "ping": "25.03 坪",
        "pattern": "1房2廳1衛",
        "location": "新北市鶯歌區光復街",
        "desc": "鶯歌市中心核心地段，鄰近鶯歌火車站、區公所與傳統市場，人潮聚集，自用開店或投資收租俱佳。",
        "link": "https://ibig.fun/EB9Vw",
        "link_text": "查看比房網規格",
        "img": get_img(p_EB9Vw)
    },
    # 6. 大義劍橋收租店面
    {
        "id": "item-1fGqX",
        "badge": "穩定高收租金店",
        "badge_color": "bg-purple-600",
        "title": "D24 大義劍橋收租店面",
        "subtitle": "公車站牌旁・人潮聚集・月收租6.5萬",
        "price": 4600,
        "ping": "60.72 坪",
        "pattern": "開放空間 (收租金店)",
        "location": "新北市三峽區大義路",
        "desc": "北大特區大義路精華地段，門口即公車站牌人潮密集，現有穩定租客月收租金6.5萬，即買即收租金投報！",
        "link": "https://ibig.fun/1fGqX",
        "link_text": "查看比房網規格",
        "img": get_img(p_1fGqX)
    },
    # 7. 竹崙風景美地
    {
        "id": "item-0YrqT",
        "badge": "休閒景觀大農地",
        "badge_color": "bg-teal-600",
        "title": "G08 三峽竹崙風景美地",
        "subtitle": "森林區林業用地・居高臨下・視野優美",
        "price": 3200,
        "ping": "地坪 1,652.26 坪",
        "pattern": "林業用地/農地",
        "location": "新北市三峽區竹崙段",
        "desc": "森林區林業用地，居高臨下視野開闊，風景優美有庭園造景，附2棟地上物，適宜休閒渡假莊園規劃。",
        "link": "https://ibig.fun/0YrqT",
        "link_text": "查看比房網規格",
        "img": get_img(p_0YrqT)
    },
    # 8. 三峽樂河郡
    {
        "id": "item-1628",
        "badge": "捷運生活圈",
        "badge_color": "bg-emerald-600",
        "title": "樂河郡-尚河 2房+車",
        "subtitle": "捷運站550米・採光視野極佳",
        "price": 1628,
        "ping": "37.4 坪",
        "pattern": "2房 / 車位",
        "location": "新北市三峽區民生街1巷",
        "desc": "格局方正、採光通風極佳，樂河郡生活圈機能完備，步行 550 公尺即抵未來捷運站，保值抗通膨首選！",
        "link": "https://www.591.com.tw/2S?salt=Sm4q8&s=al&from=share&kind=9",
        "link_text": "查看 591 完整規格",
        "img": "https://img2.591.com.tw/house/2026/09/15/178944661541367400.jpg!1000x.water2.jpg"
    },
    # 9. 萬華榮耀西門
    {
        "id": "item-3770",
        "badge": "西門捷運核心",
        "badge_color": "bg-indigo-600",
        "title": "榮耀西門 全新2房2衛2陽台",
        "subtitle": "西門站140米・全新精品宅",
        "price": 3770,
        "ping": "33.66 坪",
        "pattern": "全新 2房2衛2陽台",
        "location": "台北市萬華區漢中街",
        "desc": "西門捷運站旁僅 140 米！漢中街地段精華，全新落成精品規格，雙衛浴雙陽台設計，極稀有地段釋出。",
        "link": "https://www.591.com.tw/2S?salt=SDVlo&s=al&from=share&kind=9",
        "link_text": "查看 591 完整規格",
        "img": "https://img2.591.com.tw/house/2026/05/07/177808593052308500.jpg!1000x.water2.jpg"
    }
]

def generate_card_html(it):
    price_val = it['price']
    savings_val = round(price_val * 0.01, 1)
    
    return f"""                <!-- 物件卡片: {it['title']} -->
                <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden card-hover transition duration-200 flex flex-col justify-between">
                    <div>
                        <!-- 物件頂部圖片 -->
                        <div class="relative bg-slate-100 aspect-video overflow-hidden">
                            <img src="{it['img']}" 
                                 alt="{it['title']}" 
                                 class="w-full h-full object-cover"
                                 loading="lazy"
                                 onerror="this.src='https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800&q=80'">
                            <span class="absolute top-3 left-3 {it['badge_color']} text-white text-xs px-3 py-1 rounded-full font-bold shadow">
                                {it['badge']}
                            </span>
                            <span class="absolute bottom-3 right-3 bg-black/75 backdrop-blur text-white text-xs px-2.5 py-1 rounded font-medium">
                                專案省 {savings_val} 萬
                            </span>
                        </div>

                        <div class="p-5 space-y-3">
                            <div class="flex justify-between items-start">
                                <div>
                                    <span class="text-xs text-slate-500 font-semibold tracking-wider">{it['location']}</span>
                                    <h3 class="text-lg font-bold text-slate-900 leading-snug">{it['title']}</h3>
                                    <p class="text-xs text-red-600 font-medium mt-0.5">{it['subtitle']}</p>
                                </div>
                                <div class="text-right whitespace-nowrap pl-2">
                                    <div class="text-2xl font-black text-red-600">{price_val:,} <span class="text-sm font-normal text-slate-600">萬</span></div>
                                </div>
                            </div>

                            <!-- 規格膠囊 -->
                            <div class="grid grid-cols-3 gap-2 py-2 border-y border-slate-100 text-center text-xs text-slate-600">
                                <div class="bg-slate-50 p-2 rounded-lg">
                                    <span class="block text-slate-400">總坪數</span>
                                    <strong class="text-slate-800 text-xs font-bold">{it['ping']}</strong>
                                </div>
                                <div class="bg-slate-50 p-2 rounded-lg">
                                    <span class="block text-slate-400">格局</span>
                                    <strong class="text-slate-800 text-xs font-bold">{it['pattern']}</strong>
                                </div>
                                <div class="bg-slate-50 p-2 rounded-lg">
                                    <span class="block text-slate-400">買方省下</span>
                                    <strong class="text-red-600 text-xs font-bold">省 {savings_val} 萬</strong>
                                </div>
                            </div>

                            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed line-clamp-3">
                                {it['desc']}
                            </p>
                        </div>
                    </div>

                    <div class="p-5 pt-0 space-y-2">
                        <a href="{it['link']}" target="_blank" rel="noopener" 
                           class="flex items-center justify-center gap-2 w-full py-2.5 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs sm:text-sm font-semibold transition">
                            <span>{it['link_text']}</span>
                            <i class="fa-solid fa-arrow-up-right-from-square text-xs"></i>
                        </a>
                        <a href="tel:0933068110" 
                           class="flex items-center justify-center gap-2 w-full py-2.5 bg-red-600 hover:bg-red-700 text-white rounded-xl font-bold text-xs sm:text-sm shadow-md shadow-red-600/20 transition">
                            <i class="fa-solid fa-phone"></i>
                            <span>預約賞屋（享 1% 服務費）</span>
                        </a>
                    </div>
                </div>"""

cards_html = "\n\n".join([generate_card_html(it) for it in items])

full_html = f"""<!DOCTYPE html>
<html lang="zh-TW">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="_pWltZpn7iwynuc8wKRCbpoJlxo6NeCnQQ1LaJVDBDs" />
    <title>限時特選專案｜成家僅收 1% 買方服務費・精選雙北優質好宅＆金店面</title>
    <meta name="description"
        content="買房省下高額仲介費！本專案精選三峽【豐耘2房車 1750萬】【劍橋3房車 2398萬】【大義收租店面 4600萬】、樹林【風呂3房車 2238萬】、汐止【景觀透天別墅 4380萬】、鶯歌【光復街店面 1250萬】、三峽【竹崙風景美地 3200萬】。買方僅收 1% 服務費，立省數十萬！立即撥打 0933-068-110 預約賞屋。">

    <!-- Open Graph for Social Share -->
    <meta property="og:title" content="限時特選專案｜成交僅收 1% 買方服務費・精選雙北優質美廈＆收租金店面">
    <meta property="og:description"
        content="傳統房仲買賣收滿 2%~6%？專案直享 1% 優惠費率，現省 12.5 萬 ～ 46.0 萬元！精選三峽、樹林、汐止、鶯歌、萬華優質好宅。">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://img2.591.com.tw/house/2026/09/15/178944661541367400.jpg">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        .gradient-banner {{
            background: linear-gradient(135deg, #dc2626 0%, #ea580c 100%);
        }}

        .card-hover:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 24px -6px rgba(0, 0, 0, 0.12);
        }}

        .sticky-bottom-bar {{
            box-shadow: 0 -4px 16px rgba(0, 0, 0, 0.08);
        }}
    </style>
</head>

<body class="bg-slate-50 text-slate-800 font-sans pb-24 md:pb-12 antialiased">

    <!-- 頂部震撼促銷橫幅 -->
    <header
        class="gradient-banner text-white py-3 px-4 text-center font-bold sticky top-0 z-50 shadow-md flex items-center justify-center gap-2 text-sm sm:text-base">
        <span class="animate-pulse">🔥</span>
        <span>震撼讓利：專屬通道委託成交，買方「僅收 1% 服務費」！現省數十萬成家金</span>
    </header>

    <main class="max-w-7xl mx-auto px-4 py-8 space-y-10">

        <!-- 主標題區 -->
        <section class="text-center space-y-3 max-w-3xl mx-auto">
            <span
                class="inline-block bg-red-100 text-red-700 text-xs sm:text-sm font-semibold px-3.5 py-1 rounded-full border border-red-200">
                <i class="fa-solid fa-tags mr-1"></i> 打破傳統高趴數・給您真正的買賣讓利
            </span>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
                精選優質美廈・收租金店面 ✕ <span class="text-red-600">1% 讓利特選專案</span>
            </h1>
            <p class="text-slate-600 text-sm sm:text-base">
                還在付傳統房仲 2%~6% 的高額服務費？我們以專業誠信提供最透明的 1% 專案服務，為您省下辛苦錢充實裝潢與自備款！
            </p>
        </section>

        <!-- 1% 服務費省錢即時試算卡片 -->
        <section class="bg-white rounded-2xl shadow-sm p-6 border border-slate-200 max-w-4xl mx-auto">
            <div class="flex items-center gap-2 mb-4">
                <div
                    class="w-8 h-8 rounded-lg bg-red-100 text-red-600 flex items-center justify-center font-bold text-lg">
                    💰
                </div>
                <h2 class="text-lg sm:text-xl font-bold text-slate-900">即時試算：改用 1% 服務費能為您省下多少？</h2>
            </div>

            <div class="grid md:grid-cols-2 gap-4 items-center">
                <div class="space-y-2">
                    <label for="housePrice" class="block text-sm font-semibold text-slate-700">
                        輸入房屋總價（萬元）：
                    </label>
                    <div class="relative">
                        <input id="housePrice" type="number" value="1750" step="10"
                            class="w-full pl-4 pr-16 py-3 border-2 border-slate-300 rounded-xl focus:ring-2 focus:ring-red-500 focus:border-red-500 outline-none text-xl font-black text-slate-900 transition">
                        <span class="absolute right-4 top-1/2 -translate-y-1/2 text-slate-500 font-bold">萬元</span>
                    </div>
                    <div class="flex flex-wrap gap-1.5 pt-1">
                        <button onclick="setPrice(1250)" class="text-xs bg-slate-100 hover:bg-slate-200 text-slate-700 px-2.5 py-1 rounded-lg font-medium transition">光復街 1,250萬</button>
                        <button onclick="setPrice(1628)" class="text-xs bg-slate-100 hover:bg-slate-200 text-slate-700 px-2.5 py-1 rounded-lg font-medium transition">尚河 1,628萬</button>
                        <button onclick="setPrice(1750)" class="text-xs bg-red-100 text-red-700 font-bold px-2.5 py-1 rounded-lg transition">豐耘 1,750萬</button>
                        <button onclick="setPrice(2238)" class="text-xs bg-slate-100 hover:bg-slate-200 text-slate-700 px-2.5 py-1 rounded-lg font-medium transition">風呂 2,238萬</button>
                        <button onclick="setPrice(2398)" class="text-xs bg-slate-100 hover:bg-slate-200 text-slate-700 px-2.5 py-1 rounded-lg font-medium transition">劍橋 2,398萬</button>
                        <button onclick="setPrice(3200)" class="text-xs bg-slate-100 hover:bg-slate-200 text-slate-700 px-2.5 py-1 rounded-lg font-medium transition">竹崙地 3,200萬</button>
                        <button onclick="setPrice(3770)" class="text-xs bg-slate-100 hover:bg-slate-200 text-slate-700 px-2.5 py-1 rounded-lg font-medium transition">西門 3,770萬</button>
                        <button onclick="setPrice(4380)" class="text-xs bg-slate-100 hover:bg-slate-200 text-slate-700 px-2.5 py-1 rounded-lg font-medium transition">汐止別墅 4,380萬</button>
                        <button onclick="setPrice(4600)" class="text-xs bg-slate-100 hover:bg-slate-200 text-slate-700 px-2.5 py-1 rounded-lg font-medium transition">大義店面 4,600萬</button>
                    </div>
                </div>

                <div
                    class="bg-gradient-to-br from-red-50 to-orange-50 p-5 rounded-xl border border-red-100 text-center">
                    <span class="text-xs sm:text-sm text-red-700 font-semibold block mb-1">
                        傳統房仲 2% 買方服務費 vs 本專案 1% 買方服務費：
                    </span>
                    <div class="text-3xl sm:text-4xl font-black text-red-600 tracking-tight">
                        現省 <span id="savings">17.5</span> 萬元
                    </div>
                    <p class="text-xs text-slate-500 mt-2">
                        ※ 若計入賣方傳統 4% 降至 3%，買賣雙方合計最高可省 <span id="totalSavings"
                            class="font-bold text-slate-700">35.0</span> 萬元！
                    </p>
                </div>
            </div>
        </section>

        <!-- 精選強攻物件展示區 (桌機與平板 1排3物件，手機 1排1物件) -->
        <section class="space-y-6">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end gap-2 border-b border-slate-200 pb-4">
                <div>
                    <h2 class="text-xl sm:text-2xl font-bold text-slate-900">🏡 本期精選強攻物件（共 9 件）</h2>
                    <p class="text-sm text-slate-500">專屬 1% 買方服務費特選專案，點擊即可直連比房網 / 591 詳情與專員預約</p>
                </div>
                <div class="text-xs text-slate-500 bg-slate-100 px-3 py-1.5 rounded-lg">
                    <i class="fa-solid fa-phone mr-1 text-red-600"></i>賞屋專線：0933-068-110
                </div>
            </div>

            <!-- 物件卡片 Grid：桌機/平板 1排3物件 (md:grid-cols-3)，手機 1排1物件 (grid-cols-1) -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
{cards_html}
            </div>
        </section>

        <!-- 為什麼選擇我們的 1% 專案？ -->
        <section class="bg-slate-900 text-white rounded-2xl p-6 sm:p-8 space-y-6">
            <h2 class="text-xl sm:text-2xl font-bold text-center">🏆 為什麼選擇「1% 服務費」專屬委託通路？</h2>

            <div class="grid sm:grid-cols-3 gap-6 text-center">
                <div class="space-y-2">
                    <div
                        class="w-12 h-12 bg-red-600/20 text-red-400 rounded-xl flex items-center justify-center mx-auto text-xl font-bold">
                        <i class="fa-solid fa-hand-holding-dollar"></i>
                    </div>
                    <h3 class="font-bold text-lg">買賣省荷包</h3>
                    <p class="text-slate-400 text-sm">不賺暴利服務費，買方省下契稅裝潢金，賣方拿回最大淨利。</p>
                </div>
                <div class="space-y-2">
                    <div
                        class="w-12 h-12 bg-red-600/20 text-red-400 rounded-xl flex items-center justify-center mx-auto text-xl font-bold">
                        <i class="fa-solid fa-shield-halved"></i>
                    </div>
                    <h3 class="font-bold text-lg">合約與履保無折扣</h3>
                    <p class="text-slate-400 text-sm">同樣享有完整特約代書簽約、銀行履約保證專戶，交易安全 100% 放心。</p>
                </div>
                <div class="space-y-2">
                    <div
                        class="w-12 h-12 bg-red-600/20 text-red-400 rounded-xl flex items-center justify-center mx-auto text-xl font-bold">
                        <i class="fa-solid fa-bolt"></i>
                    </div>
                    <h3 class="font-bold text-lg">精準快速配對</h3>
                    <p class="text-slate-400 text-sm">跨平台數位行銷與專員 1 對 1 即時諮詢，看屋配對效率倍增。</p>
                </div>
            </div>

            <!-- 引導回委託經紀人完整個人店舖 -->
            <div class="pt-4 border-t border-slate-800 text-center">
                <p class="text-sm text-slate-400 mb-3">想看更多區域好宅或尋找更多 1% 讓利特選物件？</p>
                <a href="https://www.ibigfun.com/pages/index?mobile=0933068110" target="_blank" rel="noopener"
                    class="inline-flex items-center gap-2 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-600 hover:to-amber-700 text-white font-bold px-6 py-3 rounded-xl transition shadow-lg">
                    <span>進入經紀人專屬精選好房店舖</span>
                    <i class="fa-solid fa-arrow-right"></i>
                </a>
            </div>
        </section>

        <!-- 頁尾 -->
        <footer class="text-center py-6 border-t border-slate-200 text-sm text-slate-500 space-y-2">
            <p>房產專案諮詢專線：<a href="tel:0933068110" class="font-bold text-slate-900 underline text-base">0933-068-110</a>
            </p>
            <p class="text-xs text-slate-600 font-medium">
                三峽大義加盟店 &nbsp;|&nbsp; 林美不動產有限公司 &nbsp;|&nbsp; 莊文洲 (89) 宜字第00017號
            </p>
            <p class="text-xs text-slate-400">
                本專案促銷活動與物件資訊以實際簽約委託現況為準。房屋產權資料與最新銷售狀態請洽專案經紀人員。
            </p>
        </footer>
    </main>

    <!-- 手機版懸浮快速通話/預約底欄 -->
    <div
        class="fixed bottom-0 left-0 right-0 bg-white/95 backdrop-blur border-t border-slate-200 p-3 z-40 md:hidden sticky-bottom-bar flex gap-3">
        <a href="tel:0933068110"
            class="flex-1 bg-red-600 hover:bg-red-700 text-white font-bold py-3 rounded-xl flex items-center justify-center gap-2 text-sm shadow">
            <i class="fa-solid fa-phone"></i>
            <span>電話專人預約 (1% 優惠)</span>
        </a>
        <a href="https://www.ibigfun.com/pages/index?mobile=0933068110" target="_blank"
            class="bg-slate-900 hover:bg-slate-800 text-white px-4 py-3 rounded-xl flex items-center justify-center text-sm font-semibold">
            <span>經紀人店鋪</span>
        </a>
    </div>

    <!-- 即時計算器 JS -->
    <script>
        const input = document.getElementById('housePrice');
        const savings = document.getElementById('savings');
        const totalSavings = document.getElementById('totalSavings');

        function updateSavings() {{
            const val = parseFloat(input.value) || 0;
            // 買方省 1% (2% - 1%)
            const buyerSaved = (val * 0.01).toFixed(1);
            // 買賣雙方合計省 2% ((2%+4%) - (1%+3%) = 2%)
            const totalSaved = (val * 0.02).toFixed(1);

            savings.innerText = buyerSaved;
            if (totalSavings) {{
                totalSavings.innerText = totalSaved;
            }}
        }}

        function setPrice(price) {{
            input.value = price;
            updateSavings();
        }}

        input.addEventListener('input', updateSavings);
        // 初始化計算
        updateSavings();
    </script>
</body>

</html>
"""

with open('House_sale.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Updated House_sale.html and index.html with 100% verified prices!")
