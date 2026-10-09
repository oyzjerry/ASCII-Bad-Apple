# Bad Apple!! 終端 ASCII 播放器

這個版本由提供的 `badapple.mp4` 製作，從原片第一格開始播放完整動畫。播放器只顯示畫面，不會在最下面顯示進度狀態列，也沒有聲音。

## 播放資訊

| 項目 | 說明 |
| --- | --- |
| 片名 | Bad Apple!! |
| 全長 | 約 03:39（219.07 秒） |
| 影格 | 共 6,572 格，30 fps |
| 畫面 | 72 × 28 個 ASCII 字元；終端較矮時會自動縮減行數 |
| 停止 | 按 `Ctrl+C`；預設播放一次後自動結束 |

原本狀態列中的 `00:22/03:39` 表示當時播到 22 秒、全片約 3 分 39 秒；`687/6572` 表示當時第 687 格、全片共 6,572 格。這些即時數字已從播放畫面移除。

## 執行方式

### Windows CMD

將 `badapple-full.cmd` 和 `badapple-full.ps1` 放在同一個資料夾，在 CMD 執行：

```cmd
badapple-full.cmd
```

CMD 版本使用 Windows PowerShell，無需安裝 Python、Node 或 ffmpeg。

### Windows PowerShell

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\badapple-full.ps1
```

### Linux 終端

使用 Python 3 執行單一檔案：

```sh
python3 ./badapple-full.py
```

Python 版只使用標準函式庫，不需安裝其他套件。在已安裝 Python 3 的 Windows CMD，也能執行 `py -3 badapple-full.py`。

## 選項

| 功能 | CMD／PowerShell | Linux／Python |
| --- | --- | --- |
| 循環播放 | `badapple-full.cmd -Loop` | `python3 ./badapple-full.py --loop` |
| 以 0.75 倍速播放 | `badapple-full.cmd -Speed 0.75` | `python3 ./badapple-full.py --speed 0.75` |
| 從 60 秒開始播 10 秒 | `badapple-full.cmd -StartAt 60 -Duration 10` | `python3 ./badapple-full.py --start-at 60 --duration 10` |

終端至少要有 73 欄、16 行；達到 29 行時可完整顯示 72 × 28 的畫面。[觀看開頭 8 秒預覽](badapple-opening-preview.gif)。

## 從 GitHub 下載

上傳後將以下網址中的 `USER/REPO` 換成實際倉庫名稱。CMD 需要下載兩個檔案：

```cmd
curl.exe -L https://raw.githubusercontent.com/USER/REPO/main/badapple-full.cmd -o badapple-full.cmd
curl.exe -L https://raw.githubusercontent.com/USER/REPO/main/badapple-full.ps1 -o badapple-full.ps1
badapple-full.cmd
```

Linux 只需下載 Python 檔：

```sh
curl -L https://raw.githubusercontent.com/USER/REPO/main/badapple-full.py -o badapple-full.py
python3 ./badapple-full.py
```

目前只有本機成品，尚未上傳 GitHub。公開發布內嵌的影片畫格前，請先確認原片的散布權利。
