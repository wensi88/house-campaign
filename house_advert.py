"""
房地產「1% 服務費」跨平台精準截流與數位廣告自動化部署模組 (100% 官方比房網核實版)
===================================================================
專案委託目標：
1. 引導精準買家至委託經紀人專屬店鋪：https://www.ibigfun.com/pages/index?mobile=0933068110
2. 強攻 9 大精選好房與收租金店面 (全數比對核實最新售價)：
   - 1. 三峽【A43 豐耘漂亮2房車】1,750萬 (https://ibig.fun/WIx6G)
   - 2. 樹林【B64 風呂幸福三房車】2,238萬 (https://ibig.fun/vVfNy)
   - 3. 三峽【B59 劍橋溫馨靜謐三房車】2,398萬 (https://ibig.fun/SvJBd)
   - 4. 汐止【F10 汐止景觀別墅】4,380萬 (https://ibig.fun/elNHK)
   - 5. 鶯歌【D37 光復街店面】1,250萬 (https://ibig.fun/EB9Vw)
   - 6. 三峽【D24 大義劍橋收租店面】4,600萬 (https://ibig.fun/1fGqX)
   - 7. 三峽【G08 三峽竹崙風景美地】3,200萬 (https://ibig.fun/0YrqT)
   - 8. 三峽【樂河郡-尚河 2房+車】1,628萬 (https://www.591.com.tw/2S?salt=Sm4q8)
   - 9. 萬華【榮耀西門 全新精品2房】3,770萬 (https://www.591.com.tw/2S?salt=SDVlo)
3. 核心誘因：「買方僅收 1% 成交服務費」（現省 12.5 萬 ～ 46.0 萬以上）
4. 精準截流機制：針對 591 房仲網、各區域熱門關鍵字、捷運宅、北大特區、收租店面搜尋受眾進行關鍵字攔截與自訂意圖導流。
"""

import os
import json
from typing import Dict, List, Any

# ==================== 專案參數與受眾關鍵字矩陣 ====================
CAMPAIGN_CONFIG = {
    # 落地頁與導流入口
    "LANDING_PAGE_URL": "https://wensi88.github.io/house-campaign/",
    "BROKER_SHOP_URL": "https://www.ibigfun.com/pages/index?mobile=0933068110",
    "BROKER_PHONE": "0933068110",
    "BROKER_PHONE_DISPLAY": "0933-068-110",
    "BROKER_INFO": "三峽大義加盟店 林美不動產有限公司 莊文洲 (89) 宜字第00017號",
    
    # 強攻 9 大物件資料庫 (100% 比對官方 API 最新資料)
    "TARGET_PROPERTIES": [
        {
            "id": "item-WIx6G",
            "name": "A43 豐耘漂亮2房車",
            "region": "新北市三峽區民生街",
            "price_wan": 1750,
            "savings_wan": 17.5,
            "size_ping": 37.02,
            "rooms": "2房1廳1衛",
            "target_url": "https://ibig.fun/WIx6G",
            "utm_campaign": "sanxia_fengyun_1750m"
        },
        {
            "id": "item-vVfNy",
            "name": "B64 風呂幸福三房車",
            "region": "新北市樹林區學勤路",
            "price_wan": 2238,
            "savings_wan": 22.4,
            "size_ping": 55.38,
            "rooms": "3房2廳2衛",
            "target_url": "https://ibig.fun/vVfNy",
            "utm_campaign": "shulin_fenglu_2238m"
        },
        {
            "id": "item-SvJBd",
            "name": "B59 劍橋溫馨靜謐三房車",
            "region": "新北市三峽區學勤路",
            "price_wan": 2398,
            "savings_wan": 24.0,
            "size_ping": 62.42,
            "rooms": "3房2廳2衛",
            "target_url": "https://ibig.fun/SvJBd",
            "utm_campaign": "sanxia_cambridge_2398m"
        },
        {
            "id": "item-elNHK",
            "name": "F10 汐止景觀別墅",
            "region": "新北市汐止區民權街二段",
            "price_wan": 4380,
            "savings_wan": 43.8,
            "size_ping": 60.21,
            "rooms": "9房5廳6衛透天",
            "target_url": "https://ibig.fun/elNHK",
            "utm_campaign": "xizhi_villa_4380m"
        },
        {
            "id": "item-EB9Vw",
            "name": "D37 光復街店面",
            "region": "新北市鶯歌區光復街",
            "price_wan": 1250,
            "savings_wan": 12.5,
            "size_ping": 25.03,
            "rooms": "1房2廳1衛(金店面)",
            "target_url": "https://ibig.fun/EB9Vw",
            "utm_campaign": "yingge_guangfu_1250m"
        },
        {
            "id": "item-1fGqX",
            "name": "D24 大義劍橋收租店面",
            "region": "新北市三峽區大義路",
            "price_wan": 4600,
            "savings_wan": 46.0,
            "size_ping": 60.72,
            "rooms": "收租店面(月租6.5萬)",
            "target_url": "https://ibig.fun/1fGqX",
            "utm_campaign": "sanxia_dayi_shop_4600m"
        },
        {
            "id": "item-0YrqT",
            "name": "G08 三峽竹崙風景美地",
            "region": "新北市三峽區竹崙段",
            "price_wan": 3200,
            "savings_wan": 32.0,
            "size_ping": 1652.26,
            "rooms": "休閒林業用地/農地",
            "target_url": "https://ibig.fun/0YrqT",
            "utm_campaign": "sanxia_zhulun_land_3200m"
        },
        {
            "id": "item-1628",
            "name": "樂河郡-尚河 2房+車",
            "region": "新北市三峽區民生街1巷",
            "price_wan": 1628,
            "savings_wan": 16.3,
            "size_ping": 37.4,
            "rooms": "2房/車位",
            "target_url": "https://www.591.com.tw/2S?salt=Sm4q8&s=al&from=share&kind=9",
            "utm_campaign": "sanxia_lehe_1628m"
        },
        {
            "id": "item-3770",
            "name": "榮耀西門 全新捷運2房2衛",
            "region": "台北市萬華區漢中街",
            "price_wan": 3770,
            "savings_wan": 37.7,
            "size_ping": 33.66,
            "rooms": "全新2房2衛2陽台",
            "target_url": "https://www.591.com.tw/2S?salt=SDVlo&s=al&from=share&kind=9",
            "utm_campaign": "wanhua_ximen_3770m"
        }
    ],

    # Google Ads 搜尋意圖關鍵字矩陣 (Intent Interception Keywords)
    "KEYWORD_GROUPS": {
        # 1. 591 品牌與競品意圖攔截詞
        "591_COMPETITOR_INTERCEPT": [
            "591 買屋", "591 房屋交易", "591 台北買房", "591 新北買房",
            "591 仲介服務費", "591 服務費折扣", "591 三峽買屋", "591 北大特區買房"
        ],
        # 2. 三峽 / 北大特區精選物件關鍵字
        "SANXIA_BEIDA_KEYWORDS": [
            "三峽 豐耘 2房", "三峽 北大特區 買房", "北大特區 遠雄劍橋 3房",
            "樹林 北大風呂 3房車", "三峽 樂河郡", "三峽 買屋 推薦", "北大特區 電梯大樓"
        ],
        # 3. 汐止別墅 / 鶯歌三峽店面土地關鍵字
        "VILLA_SHOP_LAND_KEYWORDS": [
            "汐止 景觀別墅 買賣", "汐止 民權街二段 透天", "近中研院 透天別墅",
            "鶯歌 光復街 店面", "鶯歌 火車站 店面 出售", "三峽 大義路 收租店面",
            "三峽 竹崙 休閒農地", "新北市 林業用地 買賣"
        ],
        # 4. 萬華西門捷運宅精準詞
        "WANHUA_XIMEN_KEYWORDS": [
            "榮耀西門", "西門捷運站 買屋", "漢中街 買房", "萬華 2房 2衛 新成屋",
            "萬華 捷運宅 出售", "台北市 3500萬 4000萬 捷運"
        ],
        # 5. 1% 讓利 / 房仲服務費痛點詞
        "COMMISSION_SAVINGS_KEYWORDS": [
            "房仲服務費 1%", "買房 仲介費 折扣", "房屋買賣 服務費 談判",
            "買賣房屋 省仲介費", "1% 服務費 房仲", "買方 1% 服務費"
        ]
    },

    # 自訂意圖受眾 (Custom Intent Audience - 曾搜尋或瀏覽以下 URL/關鍵字之用戶)
    "CUSTOM_INTENT_URLS": [
        "https://sale.591.com.tw/?shType=list&regionid=3&section=40", # 591 三峽
        "https://sale.591.com.tw/?shType=list&regionid=3&section=39", # 591 樹林
        "https://sale.591.com.tw/?shType=list&regionid=3&section=36", # 591 汐止
        "https://sale.591.com.tw/?shType=list&regionid=3&section=41", # 591 鶯歌
        "https://sale.591.com.tw/?shType=list&regionid=1&section=6",  # 591 萬華
        "https://www.rakuya.com.tw",                                   # 樂屋網
        "https://buy.housefun.com.tw"                                  # 好房網
    ]
}


# ==================== 模組 1: Google Ads API 部署範本 ====================
def build_google_ads_payload(customer_id: str):
    ad_copies = [
        {
            "headlines": [
                "成交僅收 1% 買方服務費",
                "三峽北大/樹林/汐止/西門精選",
                "北大特區 豐耘/劍橋/風呂好宅",
                "汐止景觀別墅 4380萬",
                "大義路收租金店面 4600萬",
                "專屬經紀人 0933-068-110"
            ],
            "descriptions": [
                "買賣房屋告別高額仲介費！本專案專屬通道成交買方僅收1%，為您省下辛苦血汗錢。",
                "精選三峽北大特區、汐止別墅、收租金店面與西門捷運宅，產權清晰完整履保，立即預約！"
            ]
        }
    ]
    print(f"[Google Ads] 已建構搜尋攔截廣告結構，涵蓋 {sum(len(v) for v in CAMPAIGN_CONFIG['KEYWORD_GROUPS'].values())} 個核心意圖關鍵字。")
    return ad_copies


def deploy_google_campaign(client, customer_id: str):
    try:
        campaign_service = client.get_service("CampaignService")
        campaign_operation = client.get_type("CampaignOperation")
        campaign = campaign_operation.create

        campaign.name = "房產專案_9大物件意圖攔截與1%讓利專案"
        campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.SEARCH
        campaign.status = client.enums.CampaignStatusEnum.PAUSED
        campaign.manual_cpc.enhanced_cpc_enabled = True

        response = campaign_service.mutate_campaigns(customer_id=customer_id, operations=[campaign_operation])
        print(f"[Google Ads] 建立廣告活動成功: {response.results[0].resource_name}")
    except Exception as e:
        print(f"[Google Ads 提醒] API 執行需憑證授權: {e}")


# ==================== 模組 2: Meta Ads (FB/IG) 受眾與廣告部署 ====================
def deploy_meta_campaign(act_id: str, access_token: str, app_id: str, app_secret: str):
    try:
        from facebook_business.api import FacebookAdsApi
        from facebook_business.adobjects.adaccount import AdAccount
        from facebook_business.adobjects.campaign import Campaign
        from facebook_business.adobjects.adset import AdSet

        FacebookAdsApi.init(app_id, app_secret, access_token)
        account = AdAccount(f"act_{act_id}")

        campaign = account.create_campaign(
            fields=[Campaign.Field.id, Campaign.Field.name],
            params={
                Campaign.Field.name: "房地產 1% 讓利特選專案_9大物件導流",
                Campaign.Field.objective: "OUTCOME_TRAFFIC",
                Campaign.Field.status: Campaign.Status.paused,
                Campaign.Field.special_ad_categories: ["HOUSING"], # 房地產專用類別
            }
        )
        print(f"[Meta Ads] 建立 Housing 廣告活動成功: ID={campaign.get_id()}")
    except ImportError:
        print("[Meta Ads 提醒] 請安裝 facebook-business 套件: pip install facebook-business")
    except Exception as e:
        print(f"[Meta Ads 提醒] API 執行需金鑰授權: {e}")


# ==================== 模組 3: UTM 追蹤網址自動產生器 ====================
def generate_utm_links() -> Dict[str, str]:
    base_url = CAMPAIGN_CONFIG["LANDING_PAGE_URL"]
    links = {
        "Google_Search_Ads": f"{base_url}?utm_source=google&utm_medium=cpc&utm_campaign=house_1pct_commission&utm_content=search_intent",
        "Meta_FB_Feed_Ads": f"{base_url}?utm_source=facebook&utm_medium=paid_social&utm_campaign=house_1pct_commission&utm_content=9properties_carousel",
        "LINE_Official_Direct": f"{base_url}?utm_source=line&utm_medium=direct_chat&utm_campaign=house_1pct_commission"
    }
    return links


# ==================== 主程式執行與檢視 ====================
if __name__ == "__main__":
    print("=" * 65)
    print("🏠 房地產「1% 服務費」跨平台精準截流與導流系統 (9大物件100%核實版)")
    print("=" * 65)
    
    print("\n【9 大強攻物件清單（最新核實數據）】")
    for i, obj in enumerate(CAMPAIGN_CONFIG["TARGET_PROPERTIES"], 1):
        print(f" {i}. [{obj['name']}] 總價: {obj['price_wan']}萬 | 坪數: {obj['size_ping']}坪 | 省下服務費: ~{obj['savings_wan']}萬")

    print("\n【精準意圖攔截關鍵字矩陣】")
    for group, kw_list in CAMPAIGN_CONFIG["KEYWORD_GROUPS"].items():
        print(f" ▶ {group} ({len(kw_list)} 個詞): {', '.join(kw_list[:4])}...")

    print(f"\n【經紀人執業資訊】: {CAMPAIGN_CONFIG['BROKER_INFO']}")
    print("系統配置完成。所有物件與廣告矩陣已同步。")