# Bad Apple!! 終端 ASCII 播放器

由提供的 `badapple.mp4` 製作，從片頭播放完整動畫與音樂。畫面沒有底部狀態列。

| 項目 | 內容 |
| --- | --- |
| 全長 | 約 03:39（219.07 秒） |
| 畫格 | 6,572 格，30 fps |
| 畫面 | 72 × 28 個 ASCII 字元；終端較矮時自動縮減行數 |
| 停止 | `Ctrl+C`；預設播放一次 |

[觀看開頭預覽](badapple-opening-preview.gif)。

## Windows CMD：不用安裝 Python

只需下載 [badapple-windows.ps1](badapple-windows.ps1)。檔案內已有完整畫格及音樂，無需另外下載 WAV、Node 或 ffmpeg。在 CMD 執行：

```cmd
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\badapple-windows.ps1
```

例如只播放片頭 10 秒：

```cmd
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\badapple-windows.ps1 -Duration 10
```

可用 `-Loop` 循環或 `-NoAudio` 靜音。`-Speed 0.75` 調速與 `-StartAt 60` 從中途開始時，音樂無法同步，需搭配 `-NoAudio`。

## Linux 終端

只需下載 [badapple.pyz](badapple.pyz)，以 Python 3 執行：

```sh
python3 ./badapple.pyz
```

這個檔案也內含畫格和音樂，不需要 Node 或執行時的 ffmpeg。Linux 播放音樂時需要系統已有 `paplay`、`pw-play`、`aplay`、`ffplay` 或 `mpv` 其中一種；程式會自動尋找。沒有音訊工具時可用 `python3 ./badapple.pyz --no-audio`。

可用 `--loop` 循環、`--duration 10` 播放 10 秒。`--speed 0.75` 或 `--start-at 60` 需搭配 `--no-audio`。

Windows 通常沒有預裝 Python，所以預設使用 `.ps1`。若 Windows 已安裝 Python 3，也可執行**同一個** `.pyz`：`python badapple.pyz`。兩套入口都只需各自的一個檔案；原始影片和畫格相同。

終端至少需要 73 欄、16 行；達到 29 行時可完整顯示 72 × 28 的畫面。

## 從 GitHub 下載

公開上傳後，把 `USER/REPO` 換成實際倉庫名稱。Windows CMD：

```cmd
curl.exe -L https://raw.githubusercontent.com/USER/REPO/main/badapple-windows.ps1 -o badapple-windows.ps1
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\badapple-windows.ps1
```

Linux：

```sh
curl -L https://raw.githubusercontent.com/USER/REPO/main/badapple.pyz -o badapple.pyz
python3 ./badapple.pyz
```

`badapple-full.ps1`、`badapple-full.cmd` 和 `badapple-audio.wav` 是原有的 Windows 分檔版。修改後可用 Python 執行 `build_windows_single.py` 或 `build_pyz.py` 重建單檔版；Python 僅用於打包，不是 Windows 單檔版的執行需求。

這個 Git 倉庫目前只有本機提交，尚未上傳 GitHub。公開發布畫格與音樂前，請先確認原片的散布權利。
