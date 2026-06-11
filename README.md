# NailVesta 國內達人組 — 交接 SOP 手冊

一份給接手者用的互動式操作手冊，把廣達／深達的日常工作整理成可照做的步驟、判斷標準與可複製話術。

## 本機執行
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 部署到 Streamlit Cloud
1. 把 `app.py` 與 `requirements.txt` 放進 GitHub repo
2. 在 share.streamlit.io 連到該 repo，主檔選 `app.py`
3. 只依賴 `streamlit`，不需要 openpyxl／pandas 以外的套件

## 章節
- 交接須知 / 每日工作時間表
- 廣達組 SOP（批達人、評級反饋、達人邀約 & Follow Up）
- 深達組 SOP（每日 / 每週 / 每月）
- 評級制度 3.0 / 話術庫 / 包裹與水單 / 常用連結

## 隨附檔案
- `ad_code.jpg`：Ad Code 找碼圖解，必須跟 `app.py` 放在**同一層**（repo 根目錄），
  「話術庫」頁才顯示得出來。部署到 Streamlit Cloud 時記得一起 push。

## 維護
所有內容都寫在 `app.py` 的各 `render_*()` 函式裡，直接改字串即可，不需懂前端。
常用連結頁的實際網址刻意留空，請向上一手索取後填入（避免把內部連結寫死）。
