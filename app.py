# -*- coding: utf-8 -*-
"""
NailVesta 國內達人組 — 交接 SOP 手冊
=====================================
給接手的人用的「照著做就會」操作手冊。
內容整理自兩份原始文件：
  - NailVesta_國內達人組日常任務（廣達組日常工作流程）
  - 深達工作（深達組日常／每週／每月工作）

只依賴 streamlit 一個套件，方便部署到 Streamlit Cloud。
若要新增/修改內容，直接改下方各 render_* 函式裡的字串即可。
"""

import streamlit as st

# =============================================================
# 頁面設定
# =============================================================
st.set_page_config(
    page_title="NailVesta 達人組交接 SOP",
    page_icon="💅",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =============================================================
# 樣式
# =============================================================
st.markdown(
    """
    <style>
      .block-container {padding-top: 2rem; max-width: 1100px;}
      h1, h2, h3 {letter-spacing: .5px;}
      .tag {display:inline-block; padding:2px 10px; border-radius:12px;
            font-size:0.8rem; font-weight:600; margin-right:6px;}
      .tag-guang {background:#e0f2fe; color:#0369a1;}
      .tag-shen  {background:#f3e8ff; color:#7e22ce;}
      .card {border:1px solid #e5e7eb; border-radius:12px; padding:16px 18px;
             margin-bottom:14px; background:#ffffff;}
      .card h4 {margin:0 0 8px 0;}
      .muted {color:#6b7280; font-size:0.9rem;}
      .pill {display:inline-block; padding:2px 10px; border-radius:8px;
             font-weight:700; margin-right:6px;}
      .s   {background:#dcfce7; color:#15803d;}
      .ak  {background:#fef9c3; color:#a16207;}
      .bk  {background:#ffedd5; color:#c2410c;}
      .bs  {background:#fee2e2; color:#b91c1c;}
      .sp  {background:#e0e7ff; color:#4338ca;}
      .warn{background:#fef2f2; border-left:4px solid #ef4444; padding:10px 14px;
            border-radius:6px; margin:8px 0;}
      .ok  {background:#f0fdf4; border-left:4px solid #22c55e; padding:10px 14px;
            border-radius:6px; margin:8px 0;}
      .step {background:#f8fafc; border-left:4px solid #3b82f6; padding:10px 14px;
             border-radius:6px; margin:8px 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

# =============================================================
# 側欄導覽
# =============================================================
st.sidebar.title("💅 NailVesta 達人組")
st.sidebar.caption("交接 SOP 手冊 · 照著做就會")

PAGES = [
    "🏠 交接須知（先看這頁）",
    "📅 每日工作時間表",
    "🟦 廣達組 SOP",
    "🟪 深達組 SOP",
    "⭐ 評級制度（3.0）",
    "💬 話術庫（複製即用）",
    "📦 包裹狀態與水單",
    "🔗 常用連結與系統",
]
page = st.sidebar.radio("選擇章節", PAGES, label_visibility="collapsed")

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<span class='tag tag-guang'>廣達</span> 新合作 / 尚未出單的達人<br>"
    "<span class='tag tag-shen'>深達</span> 長期 / 有出單 / 有轉化的達人",
    unsafe_allow_html=True,
)
st.sidebar.caption("有疑問先查這份手冊；查不到再問營銷部門 → 達人部門。")


# =============================================================
# 深達觸達話術（再合作邀約）
# =============================================================
SHEN_OUTREACH_T1 = """Hi love
It's Ava from NailVesta! I hope you've been doing amazing — I'd love to team up with you again. We just launched a bunch of new styles and I immediately thought of you
If you're up for another collab, you can pick 2–3 of your fave styles using this link so I can send them your way:
https://forms.gle/3jQ3ainsrEyqzXjJA
For this collab, we'd love to keep it simple:
• For each set you choose, please post at least 1 video per week
• Ideally, all 2–3 sets can be filmed in face-to-camera + voiceover + hands-on (application) style
This type of content performs really well — based on TikTok data, face-to-camera product reviews have around a 61% conversion rate
If you follow this format, I'll be able to prioritize your videos for ad boosting on our end to help maximize your exposure and results
Can't wait to create something cute together again!
With love,
Ava"""

SHEN_OUTREACH_T0 = """Hi love 💖
It's Ava from NailVesta! I hope you've been doing amazing — I'd love to team up with you again. We just launched a bunch of new styles and I immediately thought of you ✨
If you're up for another collab, you can pick 3–4 of your fave styles using this link so I can send them your way:
✨ https://forms.gle/ZRYf2D2KWETX3n2y7
For this collab, we'd love to set a simple structure:
• For each set you choose, please post at least 1 video per week
• Ideally, all 3–4 sets can be filmed in face-to-camera + voiceover + hands-on (application) style
This type of content performs really well — based on TikTok data, face-to-camera product reviews have around a 61% conversion rate 📈
If you follow this format, I'll be able to prioritize your videos for ad boosting on our end to help maximize your exposure and results 💅✨
Can't wait to create something cute together again!
With love,
Ava"""


# =============================================================
# 各章節
# =============================================================
def render_intro():
    st.title("🏠 交接須知")
    st.markdown(
        "歡迎接手 NailVesta 國內達人組。這份手冊把日常工作拆成可照做的步驟，"
        "**遇到不確定的，先回來查對應章節**。"
    )

    st.subheader("這個團隊在做什麼")
    st.markdown(
        "我們透過 TikTok 達人合作推廣 NailVesta 的美甲產品，分成兩條線："
    )
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            "<div class='card'><h4>🟦 廣達（廣度達人）</h4>"
            "<ul>"
            "<li>新合作達人</li>"
            "<li>尚未出單的達人</li>"
            "<li>主要靠平台合作、有時效性發片</li>"
            "</ul>"
            "<span class='muted'>日常：批達人、評級反饋、回私訊、優化達人池</span></div>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            "<div class='card'><h4>🟪 深達（深度達人）</h4>"
            "<ul>"
            "<li>長期合作達人</li>"
            "<li>已出單、有轉化率的達人</li>"
            "<li>透過公司發貨，不跟平台合作，發片無時效壓力</li>"
            "</ul>"
            "<span class='muted'>日常：維護關係、建聯、盯數據、寄甲冊、做報表</span></div>",
            unsafe_allow_html=True,
        )

    st.subheader("每天最重要的三件事")
    st.markdown(
        "<div class='step'>1. <b>批達人</b>：上午審批當日達人申請，<b>24 小時內</b>完成所有待審。</div>"
        "<div class='step'>2. <b>評級 + 反饋</b>：把前一天發布的影片評級（3.0 系統），並回覆達人。</div>"
        "<div class='step'>3. <b>回私訊</b>：CU / CR、Email、Discord、Instagram 的訊息要及時回。</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='ok'>🌅 工作以<b>洛杉磯時間下午</b>為主（對應北京上午）。完整時段見「每日工作時間表」。</div>",
        unsafe_allow_html=True,
    )


def render_schedule():
    st.title("📅 每日工作時間表")
    st.caption("每日固定節奏，評級與日報採「順序制」由組員輪值。週日加做達人週報。")

    st.markdown(
        """
| 洛杉磯時間 | 北京時間 | 工作內容 |
|---|---|---|
| 4PM–6PM | 7AM–9AM | **視頻評級 3.0 反饋**（評前一天發布的影片並回反饋） |
| 6PM–9PM | 9AM–12PM | **回覆 CU、CR 消息** ＋ **批達人** |
| 9PM–10PM | 12PM–1PM | 午休 |
| 10PM–11PM | 1PM–2PM | **達人池優化**：搜尋新潛力達人、標記高品質素材 |
| 11PM–1AM | 2PM–4PM | **達人日報**（順序制）；週日加做**達人週報** |
"""
    )
    st.markdown(
        "<div class='ok'>「順序制／輪值」：評級反饋與日報由組員依排班表輪流負責，"
        "交接時記得跟上一手確認本週輪到誰。</div>",
        unsafe_allow_html=True,
    )


def render_guang():
    st.title("🟦 廣達組 SOP")
    tab1, tab2, tab3 = st.tabs(["☀️ 上午：批達人", "🌙 下午：評級與反饋", "🤝 達人邀約 & Follow Up"])

    # ---- 上午：批達人 ----
    with tab1:
        st.subheader("核心任務")
        st.markdown(
            "每日上午審批達人申請，**確保 24 小時內完成所有待審項目**。"
            "透過 Lark 篩選當日合作申請，核對達人資料與庫存。"
        )

        st.subheader("操作步驟")
        st.markdown(
            "<div class='step'>1. 進入 <b>Lark → AFFILIATE LIST</b> → 篩選 <b>合作日期 = 今天</b></div>"
            "<div class='step'>2. 逐筆輸入：<b>Handle、Status、Follower、款式、Size、佣金、Affiliate Link、TikTok Link</b></div>"
            "<div class='step'>3. <b>對庫存表</b>：該款式庫存 <b>少於 10 件不可發</b>，需私訊達人改款式（見話術庫「達人想換款式」）</div>"
            "<div class='step'>4. 確認 Follower 條件（見下）</div>"
            "<div class='step'>5. 特殊情況：達人 <b>GMV 很高、觀感好</b>，即使條件略差也可以批</div>",
            unsafe_allow_html=True,
        )

        st.subheader("✅ Follower 通過條件")
        st.markdown(
            "<div class='ok'>"
            "• 年齡 <b>18–34 歲佔比 > 25%</b><br>"
            "• <b>女性比例 > 50%</b><br>"
            "• <b>均播 500+</b>"
            "</div>",
            unsafe_allow_html=True,
        )

        st.subheader("⛔ 不批的達人")
        st.markdown(
            "<div class='warn'>"
            "• 申樣 <b>2 次以上</b>未發片（可能是騙樣達人）<br>"
            "• Status 為 <b>6.0</b><br>"
            "• 內容評級<b>連續 2 次以上低於</b> S / AK / AS / C（拍不出好視頻）<br>"
            "• Status 還是 <b>1.0 或 2.0</b> → 先不批<br>"
            "• 距上次合作 <b>需間隔 2 週以上</b>才可再批<br>"
            "• <b>西語達人基本不批</b>，除非 GMV 和均播特別高"
            "</div>",
            unsafe_allow_html=True,
        )

        st.subheader("⚠️ 特殊：深達在廣達裡申樣怎麼辦")
        st.markdown(
            "<div class='card'>"
            "1. 把該達人**入「深達表」，不入廣達表**<br>"
            "2. 深度合作 <b>status 改成「廣達發出」</b>，一樣填寫款式名稱、合作日期<br>"
            "3. 在群組以**接龍形式**寫：<code>handle - 廣達發出</code>"
            "</div>",
            unsafe_allow_html=True,
        )

    # ---- 下午：評級與反饋 ----
    with tab2:
        st.subheader("評級系統與影片反饋（4 步驟）")
        st.markdown(
            "<div class='step'><b>① 進入評級系統</b><br>"
            "從 Affiliate account 選擇時間排序 → 在 Lark 篩選 <b>發布日期 = 昨天</b> 的影片。</div>"
            "<div class='step'><b>② 處理「找不到人名」</b><br>"
            "去「找不到人名搜」頁面。若金額為 0 仍找不到 → 可能是<b>改名了</b>："
            "回溯合作日期查當時下的款式，再到 Affiliate 對名字。</div>"
            "<div class='step'><b>③ 視頻反饋</b><br>"
            "篩選 <b>Status ≠ 3.0</b> → 到私訊網頁，找對應話術回覆達人。</div>"
            "<div class='step'><b>④ 廣告素材處理</b><br>"
            "篩選「內容反饋」包含 <b>S、C、AK、AS</b> → 全選 Handle → 去廣告部門 → 廣告素材 → "
            "往下到底 → <b>只看前一天日期</b>（不是前一天的就刪掉）。<br>"
            "・<b>有碼</b> → 選「代投放」　・<b>沒碼</b> → 選「追蹤中」</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<div class='ok'>評級完<b>一定要回反饋</b>給達人。各等級對應的判斷標準與要做的動作，見「評級制度（3.0）」章節。</div>",
            unsafe_allow_html=True,
        )

    # ---- 達人邀約 & Follow Up ----
    with tab3:
        st.subheader("達人邀約分層")
        st.markdown(
            "<div class='card'><h4>⭐ 達人邀約 1（T2S）— 新／潛力達人</h4>"
            "強調達人的真實性與潛力，提供 <b>15% 提升佣金、付費影片支援、創意指導</b>等完整資源。</div>"
            "<div class='card'><h4>⭐⭐ 達人邀約 2（T1）— 10–28 單</h4>"
            "針對偶爾出單的達人，提供 <b>2–3 個款式選擇</b>，強調新品上市與再次合作；語調溫暖親切，表達對其內容的欣賞。</div>"
            "<div class='card'><h4>⭐⭐⭐ 達人邀約 3（T0）— 28 單以上</h4>"
            "頂級達人可選 <b>3–4 個款式</b>，提供更多彈性與優先權；強調品牌對其的重視與共同成長的願景。</div>",
            unsafe_allow_html=True,
        )

        st.subheader("Follow Up 時間軸")
        st.markdown(
            """
| 階段 | 時機 | 要做的事 |
|---|---|---|
| **Follow Up 1.0** | 樣品寄出當日 | 歡迎加入、說明品牌理念、預告 5 個工作天內送達 |
| **Follow Up 2.0** | 發貨後兩天 | 提醒包裹即將送達、查看拍攝指南、說明廣告預算支援（$20k+） |
| **Follow Up 3.0** | 發布視頻完成 | 評級視頻並回反饋，請達人做修改／更正 |
| **Follow Up 4.0** | 未發片已過 2 週 | 溫和催促、詢問進度、表達期待、提供協助 |
| **Follow Up 5.0** | 未發片已過 3 週 | 跟進催促、詢問是否需要任何幫忙或有個人因素 |
| **Follow Up 6.0** | 未發片已過 4 週 | 最後提醒，強調手工製作的用心，請求時間表／狀態更新 |
"""
        )


def render_shen():
    st.title("🟪 深達組 SOP")
    st.caption("深達 = 長期、已出單、有轉化的達人。重點在「維護關係」與「找對人深化合作」。")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📆 每日工作", "🗓️ 每週工作", "📊 每月工作", "🎯 觸達流程（廣達轉深達）"]
    )

    with tab1:
        st.markdown(
            "<div class='step'><b>① 更改廣達廣告表狀態</b><br>"
            "透過 <b>curva</b> 點 approve，統計前一天有多少達人並回報中後台；"
            "同時檢查哪些達人好、哪些不好要過篩掉。<b>approve 時務必核對款式對不對。</b></div>"

            "<div class='step'><b>② 回覆 Email / Discord / Instagram</b><br>"
            "・<b>Email</b>：回覆合作內容；深達給 ad code 後入「深度達人 list」即可；與達人建聯。<br>"
            "・<b>Discord</b>：部分深達在裡面聯繫，用來維護達人。<br>"
            "・<b>Instagram</b>：達人會來找合作或聯繫舊深達（偏好 ins）。"
            "有些達人的 Email 是經紀人在回、可能要收費，<b>改用 ins 建聯有時可免付費合作</b>。</div>"

            "<div class='step'><b>③ 轉消息給 Sisley</b><br>黑白頭像的都需要轉。</div>"

            "<div class='step'><b>④ flat fee（付費合作）達人建聯</b><br>"
            "篩選優質付費合作達人，<b>月預算 2000</b>。主要看是否符合粉絲畫像、GMV、均播、帶的品類，"
            "再進一步談合作。可用 <b>fastmoos</b> 分析。</div>"

            "<div class='step'><b>⑤ 盯後台數據</b><br>"
            "看達人近期表現；找出<b>「廣達已出單但尚未轉深達」</b>的達人；"
            "可做一份分析報告，讓組員看怎麼找達人最好。</div>"

            "<div class='step'><b>⑥ 觀察深達發片狀況</b></div>"

            "<div class='step'><b>⑦ 看廣達日報</b><br>從日報分析中找出當日問題在哪、找出優化點。</div>"

            "<div class='step'><b>⑧ 評估寄甲冊</b><br>"
            "看哪些深達可以寄甲冊；<b>有甲冊去發布視頻，轉化率會特別好</b>。</div>",
            unsafe_allow_html=True,
        )

    with tab2:
        st.markdown(
            "<div class='step'><b>① 達人週報製作</b><br>從深達表拉篩選，製作對應週報並分析。</div>"
            "<div class='step'><b>② 優化話術</b><br>制定更好的廣達及深達話術，讓視頻效應最大化，"
            "讓發布的影片<b>S 級多一些</b>。</div>"
            "<div class='step'><b>③ 監督表現</b><br>同時監督深達與廣達的表現。</div>"
            "<div class='step'><b>④ 深達 Bonus</b><br>"
            "隨時看哪些深達達到<b>近 28 天出 10 單</b>，給他們發對應的 bonus。</div>"
            "<div class='step'><b>⑤ 新款寄送</b><br>新款給固定寄款的達人寄出。</div>",
            unsafe_allow_html=True,
        )

    with tab3:
        st.markdown(
            "<div class='step'><b>製作深達月報並分析</b></div>",
            unsafe_allow_html=True,
        )
        st.caption("月報可沿用週報的篩選邏輯，拉整月區間彙總。")

    with tab4:
        st.subheader("什麼是觸達")
        st.markdown(
            "把表現好的廣達轉成深達（**深達二次合作**）。"
            "先判斷達人分層，再發對應話術，最後更新兩張表的狀態。"
        )

        st.subheader("① 分層判斷（依近 28 天 affiliate orders）")
        st.markdown(
            "<div class='card'>"
            "• <b>10–28 單</b>（偶爾出單）＝ <b>T2S / T1</b> → 用「<b>2–3 款</b>」話術<br>"
            "• <b>28 單以上</b> ＝ <b>T0</b> → 用「<b>3–4 款</b>」話術<br>"
            "<span class='muted'>判斷依據都看「近 28 天」的 affiliate orders。</span>"
            "</div>",
            unsafe_allow_html=True,
        )

        st.subheader("② 觸達步驟")
        st.markdown(
            "<div class='step'>1. 找到合適的廣達，找出他的<b>聯繫方式</b></div>"
            "<div class='step'>2. 發對應分層的<b>話術</b>給他（見下）</div>"
            "<div class='step'>3. 在<b>廣達表</b>把該達人狀態改成「<b>深達二次合作</b>」</div>"
            "<div class='step'>4. 在<b>深達表</b>把剛觸達的 <b>handle 填進去</b></div>"
            "<div class='step'>5. 在深度達人 <b>status 改成「優先－已觸達」</b></div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<div class='ok'>完成以上 5 步，這位達人的觸達就完成了。</div>",
            unsafe_allow_html=True,
        )

        st.subheader("③ 觸達話術")
        st.markdown("**T2S / T1（10–28 單，偶爾出單）— 選 2–3 款**")
        st.code(SHEN_OUTREACH_T1, language=None)
        st.markdown("**T0（28 單以上）— 選 3–4 款**")
        st.code(SHEN_OUTREACH_T0, language=None)


def render_grading():
    st.title("⭐ 評級制度（3.0）")
    st.markdown("評級金字塔：由上到下表現遞減。星級對應如下，**評完都要回反饋**。")

    st.markdown(
        "<span class='pill s'>S＝★★★ 三星</span>"
        "<span class='pill ak'>AK / AS / C＝★★ 二星</span>"
        "<span class='pill bk'>BK1–4＝★ 一星（有口播問題）</span>"
        "<span class='pill bs'>BS1–2＝★ 一星（無口播）</span>",
        unsafe_allow_html=True,
    )
    st.write("")

    st.markdown(
        "<div class='card'><h4>🟢 S — 最高評級</h4>"
        "優秀視頻，完全符合推廣要求。<br>"
        "<b>動作：誇達人 ＋ 要廣告碼 ＋ 要聯繫方式</b></div>"

        "<div class='card'><h4>🟡 AK / AS / C — 準 S，差一點</h4>"
        "符合推廣要求，有潛力（口播小問題）。<b>動作：誇達人、給反饋讓再發、要廣告碼。</b><br>"
        "・<b>AK</b>：有口播、沒露臉的準 S<br>"
        "・<b>AS</b>：沒口播、有露臉的準 S<br>"
        "・<b>C</b>：高級、美甲展示</div>"

        "<div class='card'><h4>🟠 BK1–BK4 — 有潛力（口播問題）</h4>"
        "・<b>BK1</b>：視頻 &gt; 60s<br>"
        "・<b>BK2</b>：產品拍攝不清<br>"
        "・<b>BK3</b>：視頻 &lt; 20s<br>"
        "・<b>BK4</b>：沒上手</div>"

        "<div class='card'><h4>🔴 BS1–BS2 — 無口播</h4>"
        "・<b>BS1</b>：無口播、沒上手<br>"
        "・<b>BS2</b>：無口播、沒賣點</div>",
        unsafe_allow_html=True,
    )

    st.subheader("額外特殊情況")
    st.markdown(
        "<div class='card'>"
        "<span class='pill sp'>T</span> 我們的指甲＋別人的鏈接 / 別人的指甲＋我們的鏈接 / 西語<br>"
        "<span class='pill sp'>Haul</span> 混合包裹影片<br>"
        "<span class='pill sp'>D</span> 刪視頻 → 讓達人重發<br>"
        "<span class='pill sp'>S（速投）</span> 若有影片內容一樣都評 S，再標注「速投」"
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='ok'>🔼 <b>PC（可深達）</b>：達到 100（單）或觀感好的美女，"
        "即可同時標記為「<b>可深達</b>」，後續轉入深達流程。</div>",
        unsafe_allow_html=True,
    )


def script_block(title, body, note=""):
    st.markdown(f"**{title}**")
    st.code(body, language=None)
    if note:
        st.caption(note)


def render_scripts():
    st.title("💬 話術庫（複製即用）")
    st.markdown(
        "<div class='warn'>📌 通用原則：所有回覆保持<b>親切、專業、有活力</b>的語調，"
        "適當使用表情符號增加親和力，確保資訊清晰準確。"
        "不確定的對話可至：營銷部門 → 達人部門 → CU 回覆情境 查看。</div>",
        unsafe_allow_html=True,
    )
    st.caption("每段話術右上角有複製鈕，點一下就能複製。")

    script_block(
        "📥 收到 Code 回覆",
        "Got it! Thank you so much for collaborating with us, babe 💅💖 "
        "We're so happy to have you on board!",
    )
    script_block(
        "❓ 詢問 Free Sample（想合作）",
        "Hi love 💕 Thank you so much for reaching out 🩷 "
        "You can request a free sample directly through our TikTok Shop Creator Center "
        "by selecting that style and submitting your request.",
    )
    script_block(
        "📝 問步驟（怎麼申請樣品）",
        "Hi love 💕 of course! I'm happy to help 🥰✨\n"
        "Here's how you can request your free sample step by step 💅:\n"
        "1️⃣ Go to your TikTok Shop → Creator Center\n"
        "2️⃣ Tap \"Free Sample\" at the top\n"
        "3️⃣ In the search bar, type NailVesta 💅\n"
        "4️⃣ Choose the nail style you love and click Apply",
    )
    script_block(
        "🎉 歡迎新達人",
        "I'm so happy to have you join our little family — welcome to NailVesta 💅💕 "
        "I can't wait to see your video!",
    )
    script_block(
        "✅ 批准了",
        "Hi babe! I just approved your request — I can't wait to see your beautiful content 💅✨",
    )
    script_block(
        "✉️ 寄邀請",
        "Hi babe🩷 I just sent the invitation to you! When you request your free sample, "
        "please let me know so I can keep an eye out 💅✨ thank you babe!",
    )
    script_block(
        "⏳ 申樣達人拖延（催發片前的安撫）",
        "Hi love! 💖 Thank you so much for being willing to collaborate with us! "
        "Due to the large number of applications we're currently receiving, it might take "
        "a little bit of time to process, and I truly appreciate your patience. "
        "I'll try my best to make this as quick as possible.",
    )
    script_block(
        "🙅 不符合粉絲畫像 / 不符的達人",
        "Hi love! Thank you so much for kind words. I am so sorry about that—because we've had "
        "a high number of requests and limited sample stock right now, the platform has set some "
        "requirements like minimum average views 🥺. I truly hope we can work together in the "
        "future when things open up a bit more! 💖",
        note="紅字提示：可改用 followers 為由，看達人哪項沒符合再去調整說法。",
    )
    script_block(
        "🔁 達人想換款式",
        "Ok babe 🤍 I'll ship Floral Muse (M) to you — it's the fourth one in the picture. "
        "I think it's going to look so good on you 💅✨💕",
        note="操作：先看達人選的款式還有沒有庫存；若有，去『換貨表』與『總表』更改後再回覆。",
    )
    script_block(
        "📐 尺寸不符",
        "Hi babe 🥹💖 I'm so sorry the size wasn't a perfect fit, I know that can be frustrating. "
        "Since our sample stock is really limited right now, would you mind trying a little "
        "adjustment trick first?\n"
        "✨ Too loose: Use the provided file to carefully file down the edges until the nails "
        "fit your fingers better.\n"
        "✨ Too tight: Use a hair dryer to apply hot air to the bottom of the nails, then gently "
        "press and flatten the bottom part to widen them.\n"
        "Please give it a try and keep me updated. I'd love to know how it works out for you 💖",
    )
    script_block(
        "📌 爆單達人置頂（請求 pin 影片）",
        "Hi babe, your video is truly stunning and I'm honestly obsessed 🥹💗 if it's not too "
        "much trouble, would you mind pinning it on your profile? It lets more people see your "
        "beautiful look right away and can really help your views and followers grow — thank you "
        "so much, I appreciate you!",
    )
    script_block(
        "🌎 西語達人（暫不合作）",
        "Hi love! 💖 Thank you so much for your interest in working with us — we truly appreciate "
        "your support and beautiful energy! At the moment, we don't have any team members who "
        "speak Spanish, so we're not able to fully understand or evaluate Spanish-language content "
        "just yet 😢. We're still a small but growing brand, and we hope to expand our team in the "
        "future to include more language support! Once we have someone on the team who can support "
        "Spanish-speaking creators, we'd love to reach back out and explore a collab with you! "
        "Thank you again for understanding and for thinking of us ✨💕",
    )


def render_logistics():
    st.title("📦 包裹狀態與水單")

    st.subheader("狀態更新規則")
    st.markdown(
        """
| 階段 | 合作日期 | 包裹狀態 | 操作時機 |
|---|---|---|---|
| **1.0 運送中** | 填「**今天**」 | 改為 **In Transit** | 發送 1.0 階段 |
| **2.0 已送達** | 兩天後（篩選合作日期為「**前天**」） | 改為 **Delivered** | 發送 2.0 階段 |
"""
    )
    st.markdown(
        "<div class='ok'>包裹狀態的準確更新是合作流程順暢的關鍵，直接影響後續的評級與反饋時程。</div>",
        unsafe_allow_html=True,
    )

    st.subheader("水單填寫要點")
    st.markdown(
        "<div class='card'>"
        "• 客速類型選「<b>達人補寄</b>」<br>"
        "• <b>Handle 與 Order ID 必須優先填寫</b><br>"
        "• 發貨備註需包含<b>完整姓名、電話和地址</b><br>"
        "• Product Name 填款式；<b>達人若沒特別指定，就按當初發貨的款式</b>填"
        "</div>",
        unsafe_allow_html=True,
    )
    st.caption("以上為廣達水單補寄的填法。")

    st.subheader("📋 跟達人要資訊")
    st.markdown(
        "<div class='step'>補寄前請達人提供：<b>姓名、電話、地址</b>。</div>"
        "<div class='step'><b>地址</b>可以用 AI 工具檢查格式是否正確"
        "（拼字、城市、州別縮寫、郵遞區號）再填單，避免寄錯。</div>",
        unsafe_allow_html=True,
    )


def render_links():
    st.title("🔗 常用連結與系統")
    st.markdown(
        "<div class='warn'>下方是原文件列出的工作工具清單。"
        "<b>實際網址請向上一手索取並填入下方說明中</b>（避免把內部連結寫死在程式裡）。</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
| 系統 / 工具 | 用途 |
|---|---|
| **廣告表** | 管理所有廣告素材與投放狀態 |
| **換貨管理**（換貨話數、換貨表） | 換貨話術記錄與換貨表單查詢 |
| **庫存表 / 廣達總表 / 深達總表** | 即時庫存查詢與達人總表管理 |
| **批達人 / 評級 3.0 系統**（TikTok 系統） | 批達人申請與影片評級 |
| **3.0 反饋話術 / 訂單查詢** | 反饋話術與達人 handle 訂單搜尋 |
| **FAQ 問題整理** | 常見問題彙整 |
| **達人日報 / 達人日報 SOP** | 日報填表規則與範例 |
| **腳本拆解 / 爆款視頻例子** | 腳本拆解與爆款視頻範例 |
| **Lark — Affiliate List / Affiliate Account** | 批達人、評級時的主要操作後台 |
| **fastmoos** | 分析達人 GMV、均播、品類（深達建聯篩選用） |
| **curva** | 廣達廣告表 approve（深達每日工作） |
"""
    )

    st.subheader("📨 寄送 Invite 流程（Creator Center）")
    st.markdown(
        "<div class='step'>進入 <b>Find Creator</b> → 貼上 handle → 往下找到 <b>Invite</b> → "
        "點擊最上方連結 → 發送 Invite</div>",
        unsafe_allow_html=True,
    )


# =============================================================
# 路由
# =============================================================
ROUTES = {
    PAGES[0]: render_intro,
    PAGES[1]: render_schedule,
    PAGES[2]: render_guang,
    PAGES[3]: render_shen,
    PAGES[4]: render_grading,
    PAGES[5]: render_scripts,
    PAGES[6]: render_logistics,
    PAGES[7]: render_links,
}
ROUTES[page]()

st.sidebar.markdown("---")
st.sidebar.caption("整理自《國內達人組日常任務》與《深達工作》兩份文件 · v1")
