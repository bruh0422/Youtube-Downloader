# Youtube 音樂下載器
將 Youtube 影片轉換為音訊檔並下載。

## 運作原理
使用 `yt-dlp` 從 Youtube 抓取影片。

## 前置作業
### 複製儲存庫
```bash
git clone https://github.com/bruh0422/Youtube-Downloader.git
cd Youtube-Downloader
```

### 安裝必要檔案
```bash
pip install -r requirements.txt
```
還需要安裝 [FFmpeg](https://ffmpeg.org/)，具體操作步驟請自行 [Google](https://www.google.com/search?q=ffmpeg+install)。

## 開始使用
```bash
python run.py
```
接下來按照程式指定的步驟操作即可。\
下載下來的曲目會儲存到 `output` 資料夾中。
