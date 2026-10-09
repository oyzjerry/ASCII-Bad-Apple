# ASCII Bad Apple!!

在終端機播放完整的 **Bad Apple!!** ASCII 動畫與音樂。畫格由影片從開頭轉換，沒有底部狀態列。

![Bad Apple!! 開頭預覽](badapple-opening-preview.gif)

- 完整 6,572 格，30 fps，片長約 3 分 39 秒
- 72 × 28 字元畫面；終端高度不足時會自動縮減行數
- Windows 和 Linux 各有一個內含畫格及音樂的單檔版本
- 播放一次、循環、指定時長與靜音模式

## 快速開始

請先把終端調整至至少 **73 欄 × 16 行**；高度達 29 行時可顯示完整畫面。按 `Ctrl+C` 停止。

### Windows：不需要 Python

在 **CMD** 下載 [badapple-windows.ps1](badapple-windows.ps1)，並用 Windows 內建的 PowerShell 執行：

```cmd
curl.exe -fL https://raw.githubusercontent.com/oyzjerry/ASCII-Bad-Apple/main/badapple-windows.ps1 -o badapple-windows.ps1
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\badapple-windows.ps1
```

這個約 20 MB 的檔案已包含畫格與 WAV 音樂，不必另外安裝 Python、Node 或 ffmpeg，也不必下載其他專案檔案。

### Linux：Python 3

下載 [badapple.pyz](badapple.pyz)，再以 Python 3 執行：

```sh
curl -fL https://raw.githubusercontent.com/oyzjerry/ASCII-Bad-Apple/main/badapple.pyz -o badapple.pyz
python3 ./badapple.pyz
```

這個約 15 MB 的檔案也包含畫格與音樂。音樂播放需要系統已有 `paplay`、`pw-play`、`aplay`、`ffplay` 或 `mpv` 其中一種工具；程式會自動選擇。若沒有音訊工具，可用 `python3 ./badapple.pyz --no-audio` 靜音播放。執行時不需要 Node 或 ffmpeg（除非 ffmpeg 是你選用的音訊工具）。

> Windows 通常沒有預裝 Python，因此 Windows 建議使用 `.ps1`。已安裝 Python 3 的 Windows 也可執行同一份 `badapple.pyz`。

## 播放選項

| 功能 | Windows CMD | Linux |
| --- | --- | --- |
| 播放片頭 10 秒 | `powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\badapple-windows.ps1 -Duration 10` | `python3 ./badapple.pyz --duration 10` |
| 循環播放 | `powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\badapple-windows.ps1 -Loop` | `python3 ./badapple.pyz --loop` |
| 靜音播放 | `powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\badapple-windows.ps1 -NoAudio` | `python3 ./badapple.pyz --no-audio` |
| 從 60 秒開始播放 10 秒 | `powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\badapple-windows.ps1 -NoAudio -StartAt 60 -Duration 10` | `python3 ./badapple.pyz --no-audio --start-at 60 --duration 10` |

也可使用 `-Speed 0.75`（Windows）或 `--speed 0.75`（Linux）調整速度。調速或從中途開始時，音樂無法同步，因此需要靜音參數。

## 專案檔案

| 檔案 | 用途 |
| --- | --- |
| `badapple-windows.ps1` | Windows 單檔播放器，內含畫格與音樂 |
| `badapple.pyz` | Windows / Linux 共用的 Python 3 單檔播放器 |
| `badapple-full.ps1`、`badapple-full.cmd` | 原有的 Windows 分檔版，需要旁邊的 `badapple-audio.wav` |
| `badapple-full.py`、`badapple-audio.wav` | Python 原始播放器與 WAV 音樂 |
| `build_windows_single.py`、`build_pyz.py` | 從上述來源重新產生單檔版 |

要修改程式並重新打包時，開發電腦需安裝 Python 3：

```sh
python3 build_windows_single.py
python3 build_pyz.py
```

Windows 使用者可以改用 `python` 執行這兩個打包腳本；**播放** `badapple-windows.ps1` 不需要 Python。

## License and media

本倉庫的播放器程式碼採用 [MIT License](LICENSE)。動畫畫格與音訊由提供的 *Bad Apple!!* 影片轉換，**不因程式碼的 MIT 授權而取得相同授權**。重製或再散布這些影音素材時，請自行確認所需權利。

---

**English:** Play the complete 6,572-frame Bad Apple!! animation with audio in your terminal. On Windows, download `badapple-windows.ps1` and run it with the built-in `powershell.exe`; no Python is required. On Linux, download `badapple.pyz` and run `python3 ./badapple.pyz`. Linux audio requires one of `paplay`, `pw-play`, `aplay`, `ffplay`, or `mpv`; use `--no-audio` otherwise. The MIT license covers the player code, not the converted video frames or audio.
