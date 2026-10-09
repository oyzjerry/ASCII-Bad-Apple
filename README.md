# Bad Apple!! 終端 ASCII 播放器

由提供的 `badapple.mp4` 製作，從片頭播放完整動畫與音樂。畫面沒有底部狀態列。

| 項目 | 內容 |
| --- | --- |
| 全長 | 約 03:39（219.07 秒） |
| 畫格 | 6,572 格，30 fps |
| 畫面 | 72 × 28 個 ASCII 字元；終端較矮時自動縮減行數 |
| 停止 | `Ctrl+C`；預設播放一次 |

原本狀態列中的 `00:22/03:39` 表示當時播放到 22 秒；`687/6572` 表示當時第 687 格。這些即時數字已從畫面移除。[觀看開頭預覽](badapple-opening-preview.gif)。

## 同一檔案在 Windows 與 Linux 執行

**推薦下載 [badapple.pyz](badapple.pyz)。** 這是約 14.8 MB 的單檔 Python 程式，裡面已有完整畫格與音樂；播放時會自動判斷系統、選擇音訊方式，並在結束後清除暫存音檔。兩邊都需要 Python 3，不需要 Node 或執行時的 ffmpeg。

Windows CMD：

```cmd
py -3 badapple.pyz
```

若電腦有 Python 3 但沒有 `py` 啟動器，改用 `python badapple.pyz`。

Linux 終端：

```sh
python3 ./badapple.pyz
```

Windows 音訊使用內建的 WAV 播放功能。Linux 需要系統上有 `paplay`、`pw-play`、`aplay`、`ffplay` 或 `mpv` 其中一種；程式會自動尋找。沒有音訊工具時可以使用 `--no-audio` 靜音播放。

| 功能 | Windows CMD | Linux |
| --- | --- | --- |
| 循環播放 | `py -3 badapple.pyz --loop` | `python3 ./badapple.pyz --loop` |
| 靜音 | `py -3 badapple.pyz --no-audio` | `python3 ./badapple.pyz --no-audio` |
| 從片頭播放 10 秒（有音樂） | `py -3 badapple.pyz --duration 10` | `python3 ./badapple.pyz --duration 10` |
| 0.75 倍速 | `py -3 badapple.pyz --no-audio --speed 0.75` | `python3 ./badapple.pyz --no-audio --speed 0.75` |
| 從 60 秒開始播 10 秒 | `py -3 badapple.pyz --no-audio --start-at 60 --duration 10` | `python3 ./badapple.pyz --no-audio --start-at 60 --duration 10` |

調速或從中途開始時音訊無法同步，因此須加 `--no-audio`。終端至少需要 73 欄、16 行；達到 29 行時可完整顯示原本的 72 × 28 畫面。

## Windows 不安裝 Python 的方式

將 `badapple-full.cmd`、`badapple-full.ps1` 和 `badapple-audio.wav` 放在同一資料夾，在 CMD 執行：

```cmd
badapple-full.cmd
```

這個入口使用 Windows PowerShell。可加 `-Loop` 循環、`-NoAudio` 靜音；調速或從中途開始需同時加 `-NoAudio`。

## 從 GitHub 下載

公開上傳後，把 `USER/REPO` 換成實際倉庫名稱。單檔版只需下載 `badapple.pyz`：

```cmd
curl.exe -L https://raw.githubusercontent.com/USER/REPO/main/badapple.pyz -o badapple.pyz
py -3 badapple.pyz
```

Linux：

```sh
curl -L https://raw.githubusercontent.com/USER/REPO/main/badapple.pyz -o badapple.pyz
python3 ./badapple.pyz
```

倉庫中的 `badapple-full.py` 和 `badapple-audio.wav` 是單檔版的來源；修改後可執行 `python3 build_pyz.py` 重新打包。這個 Git 倉庫目前只有本機提交，尚未上傳 GitHub。公開發布畫格與音樂前，請先確認原片的散布權利。
