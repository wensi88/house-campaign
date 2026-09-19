"""
房地產「1% 服務費」跨平台精準截流與數位廣告自動化部署模組
===================================================================
專案委託目標：
1. 引導精準買家至委託經紀人專屬店鋪：https://www.ibigfun.com/pages/index?mobile=0933068110
2. 強攻兩大精選物件：
   - 物件 1: 三峽【樂河郡-尚河】2房+車 1,628萬 (https://www.591.com.tw/2S?salt=Sm4q8)
   - 物件 2: 萬華【榮耀西門】捷運140m 2房2衛 3,770萬 (https://www.591.com.tw/2S?salt=SDVlo)
3. 核心誘因：「僅收 1% 成交服務費」（現省 16.28 萬 ～ 37.7 萬以上）
4. 精準截流機制：針對 591 房仲網、三峽/萬華區域關鍵字、捷運宅搜尋受眾進行關鍵字攔截與自訂意圖導流。
"""

import os
import json
from typing import Dict, List, Any

# ==================== 專案參數與受眾關鍵字矩陣 ====================
CAMPAIGN_CONFIG = {
    # 落地頁與導流入口
    "LANDING_PAGE_URL": "https://www.ibigfun.com/pages/index?mobile=0933068110",
    "CUSTOM_LANDING_PAGE": "https://your-domain-or-github-io-url.com", # 自建 1% 試算落地頁
    "BROKER_PHONE": "0933068110",
    "BROKER_PHONE_DISPLAY": "0933-068-110",
    
    # 強攻物件資料庫
    "TARGET_PROPERTIES": [
        {
            "id": "item-1628",
            "name": "樂河郡-尚河 2房+車",
            "full_title": "尚河2房+車採光視野佳捷運站550米",
            "region": "新北市三峽區",
            "price_wan": 1628,
            "savings_wan": 16.28,
            "size_ping": 37.4,
            "rooms": "2房",
            "591_url": "https://www.591.com.tw/2S?salt=Sm4q8&s=al&from=share&kind=9",
            "utm_campaign": "sanxia_lehe_1628m"
        },
        {
            "id": "item-3770",
            "name": "榮耀西門 全新捷運2房2衛",
            "full_title": "漢中街,西門捷運站旁140米,全新2房2衛2陽台",
            "region": "台北市萬華區漢中街",
            "price_wan": 3770,
            "savings_wan": 37.70,
            "size_ping": 33.66,
            "rooms": "2房2衛",
            "591_url": "https://www.591.com.tw/2S?salt=SDVlo&s=al&from=share&kind=9",
            "utm_campaign": "wanhua_ximen_3770m"
        }
    ],

    # Google Ads 搜尋意圖關鍵字矩陣 (Intent Interception Keywords)
    "KEYWORD_GROUPS": {
        # 1. 591 品牌與競品意圖攔截詞
        "591_COMPETITOR_INTERCEPT": [
            "591 買屋", "591 房屋交易", "591 台北買房", "591 新北買房",
            "591 仲介服務費", "591 服務費折扣", "591 三峽買屋", "591 萬華買屋"
        ],
        # 2. 三峽 1628 萬物件精準詞
        "SANXIA_1628M_KEYWORDS": [
            "三峽 樂河郡", "樂河郡 尚河", "三峽 2房 車位", "三峽 捷運宅 買屋",
            "三峽 1500萬 1800萬 買房", "三峽 民生街 買屋", "三峽 中古屋 推薦"
        ],
        # 3. 萬華西門 3770 萬物件精準詞
        "WANHUA_3770M_KEYWORDS": [
            "榮耀西門", "西門捷運站 買屋", "漢中街 買房", "萬華 2房 2衛 新成屋",
            "萬華 捷運宅 出售", "西門町 住宅 買賣", "台北市 3500萬 4000萬 捷運"
        ],
        # 4. 1% 讓利 / 房仲服務費痛點詞
        "COMMISSION_SAVINGS_KEYWORDS": [
            "房仲服務費 1%", "買房 仲介費 折扣", "房屋買賣 服務費 談判",
            "買賣房屋 省仲介費", "1% 服務費 房仲", "買方 1% 服務費"
        ]
    },

    # 自訂意圖受眾 (Custom Intent Audience - 曾搜尋或瀏覽以下 URL/關鍵字之用戶)
    "CUSTOM_INTENT_URLS": [
        "https://sale.591.com.tw/?shType=list&regionid=3&section=40", # 591 三峽區售屋
        "https://sale.591.com.tw/?shType=list&regionid=1&section=6",  # 591 萬華區售屋
        "https://www.rakuya.com.tw",                                   # 樂屋網
        "https://buy.housefun.com.tw"                                  # 好房網
    ]
}


# ==================== 模組 1: Google Ads API 部署範本 ====================
def build_google_ads_payload(customer_id: str):
    """
    產生 Google Ads Campaign / AdGroup / 擴充資訊結構
    包含 Responsive Search Ads (RSA) 文案設計與出價策略
    """
    ad_copies = [
        {
            "headlines": [
                "成交僅收 1% 買賣服務費",
                "三峽樂河郡 1628萬 2房車",
                "西門捷運140米 榮耀西門 3770萬",
                "傳統2%現降為1% 省數十萬",
                "專屬經紀人 0933-068-110"
            ],
            "descriptions": [
                "買賣房屋告別高額仲介費！本專案專屬通道成交僅收1%，為您省下辛苦血汗錢。",
                "精選三峽捷運宅1628萬與西門核心全新2房3770萬，產權清晰完整履保，立即預約！"
            ]
        }
    ]
    print(f"[Google Ads] 已建構搜尋攔截廣告結構，涵蓋 {sum(len(v) for v in CAMPAIGN_CONFIG['KEYWORD_GROUPS'].values())} 個核心意圖關鍵字。")
    return ad_copies


def deploy_google_campaign(client, customer_id: str):
    """
    透過 Google Ads API 建立廣告活動 (需填入 google-ads.yaml 設定檔)
    """
    try:
        campaign_service = client.get_service("CampaignService")
        campaign_operation = client.get_type("CampaignOperation")
        campaign = campaign_operation.create

        campaign.name = "房產專案_591意圖攔截與1%讓利專案"
        campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.SEARCH
        campaign.status = client.enums.CampaignStatusEnum.PAUSED
        campaign.manual_cpc.enhanced_cpc_enabled = True

        response = campaign_service.mutate_campaigns(customer_id=customer_id, operations=[campaign_operation])
        print(f"[Google Ads] 建立廣告活動成功: {response.results[0].resource_name}")
    except Exception as e:
        print(f"[Google Ads 提醒] API 執行需憑證授權: {e}")


# ==================== 模組 2: Meta Ads (FB/IG) 受眾與廣告部署 ====================
def deploy_meta_campaign(act_id: str, access_token: str, app_id: str, app_secret: str):
    """
    透過 Meta Business SDK 建立高轉化導流廣告
    鎖定新北三峽、台北萬華周邊 15km 購屋意圖族群
    """
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
                Campaign.Field.name: "房地產 1% 讓利特選專案_導流活動",
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
    """
    產生包含完整 UTM 標籤的導流連結，確保每一筆點擊與諮詢皆能歸因
    """
    base_url = CAMPAIGN_CONFIG["LANDING_PAGE_URL"]
    links = {
        "Google_Search_Ads": f"{base_url}&utm_source=google&utm_medium=cpc&utm_campaign=house_1pct_commission&utm_content=591_intent",
        "Meta_FB_Feed_Ads": f"{base_url}&utm_source=facebook&utm_medium=paid_social&utm_campaign=house_1pct_commission&utm_content=sanxia_ximen_carousel",
        "LINE_Official_Direct": f"{base_url}&utm_source=line&utm_medium=direct_chat&utm_campaign=house_1pct_commission"
    }
    return links


# ==================== 主程式執行與檢視 ====================
if __name__ == "__main__":
    print("=" * 60)
    print("🏠 房地產「1% 服務費」跨平台精準截流與導流系統")
    print("=" * 60)
    
    print("\n【強攻物件清單】")
    for obj in CAMPAIGN_CONFIG["TARGET_PROPERTIES"]:
        print(f" • [{obj['name']}] 總價: {obj['price_wan']}萬 | 省下服務費: ~{obj['savings_wan']}萬 | 591連結: {obj['591_url']}")

    print("\n【精準意圖攔截關鍵字矩陣】")
    for group, kw_list in CAMPAIGN_CONFIG["KEYWORD_GROUPS"].items():
        print(f" ▶ {group} ({len(kw_list)} 個詞): {', '.join(kw_list[:4])}...")

    print("\n【多通路 UTM 追蹤導流連結】")
    for channel, link in generate_utm_links().items():
        print(f" 🔗 {channel}:\n    {link}")

    print("\n系統配置完成。可直接搭配 GitHub Pages / Netlify 上線落地頁，並對接 Google & Meta Ads API 啟用投放。")