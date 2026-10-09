# Bad Apple!! 終端 ASCII 播放器

這個版本由提供的 `badapple.mp4` 製作，從原片第一格開始播放完整動畫與音樂。畫面不會在最下面顯示進度狀態列。

## 播放資訊

| 項目 | 說明 |
| --- | --- |
| 片名 | Bad Apple!! |
| 全長 | 約 03:39（219.07 秒） |
| 影格 | 共 6,572 格，30 fps |
| 畫面 | 72 × 28 個 ASCII 字元；終端較矮時會自動縮減行數 |
| 音樂 | 同資料夾的 `badapple-audio.wav`，由原片音軌轉成 32 kHz 單聲道 WAV；約 14 MB |
| 停止 | 按 `Ctrl+C`；預設播放一次後自動結束 |

原本狀態列中的 `00:22/03:39` 表示當時播到 22 秒、全片約 3 分 39 秒；`687/6572` 表示當時第 687 格、全片共 6,572 格。這些即時數字已從播放畫面移除。

## 執行方式

### Windows CMD

將 `badapple-full.cmd`、`badapple-full.ps1` 和 `badapple-audio.wav` 放在同一個資料夾，在 CMD 執行：

```cmd
badapple-full.cmd
```

CMD 版本使用 Windows PowerShell，無需安裝 Python、Node 或 ffmpeg。

### Windows PowerShell

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\badapple-full.ps1
```

同樣需要把 `badapple-audio.wav` 放在腳本旁邊。

### Linux 終端

將 `badapple-full.py` 和 `badapple-audio.wav` 放在同一個資料夾，用 Python 3 執行：

```sh
python3 ./badapple-full.py
```

Python 腳本只使用標準函式庫。Linux 播放音訊時還需要系統上有 `paplay`、`pw-play`、`aplay`、`ffplay` 或 `mpv` 其中一種；腳本會自動尋找。在已安裝 Python 3 的 Windows CMD，也能執行 `py -3 badapple-full.py`。

## 選項

| 功能 | CMD／PowerShell | Linux／Python |
| --- | --- | --- |
| 循環播放 | `badapple-full.cmd -Loop` | `python3 ./badapple-full.py --loop` |
| 靜音播放 | `badapple-full.cmd -NoAudio` | `python3 ./badapple-full.py --no-audio` |
| 以 0.75 倍速播放 | `badapple-full.cmd -NoAudio -Speed 0.75` | `python3 ./badapple-full.py --no-audio --speed 0.75` |
| 從 60 秒開始播 10 秒 | `badapple-full.cmd -NoAudio -StartAt 60 -Duration 10` | `python3 ./badapple-full.py --no-audio --start-at 60 --duration 10` |

調速或從中途開始時，內建音訊無法同步，必須使用靜音選項；`-Duration`／`--duration` 從片頭播放時仍可帶音樂。沒有音檔或 Linux 音訊工具時也可以選擇靜音。終端至少要有 73 欄、16 行；達到 29 行時可完整顯示 72 × 28 的畫面。[觀看開頭 8 秒預覽](badapple-opening-preview.gif)。

## 從 GitHub 下載

上傳後將以下網址中的 `USER/REPO` 換成實際倉庫名稱。CMD 需要下載三個檔案：

```cmd
curl.exe -L https://raw.githubusercontent.com/USER/REPO/main/badapple-full.cmd -o badapple-full.cmd
curl.exe -L https://raw.githubusercontent.com/USER/REPO/main/badapple-full.ps1 -o badapple-full.ps1
curl.exe -L https://raw.githubusercontent.com/USER/REPO/main/badapple-audio.wav -o badapple-audio.wav
badapple-full.cmd
```

Linux 需要下載 Python 腳本與音檔：

```sh
curl -L https://raw.githubusercontent.com/USER/REPO/main/badapple-full.py -o badapple-full.py
curl -L https://raw.githubusercontent.com/USER/REPO/main/badapple-audio.wav -o badapple-audio.wav
python3 ./badapple-full.py
```

目前只有本機成品，尚未上傳 GitHub。公開發布內嵌的影片畫格與音樂前，請先確認原片的散布權利。
