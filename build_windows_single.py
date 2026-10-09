"""Build the standalone Windows PowerShell player from the source player and WAV."""

import base64
import gzip
from pathlib import Path


ROOT = Path(__file__).resolve().parent
source = (ROOT / "badapple-full.ps1").read_text(encoding="utf-8")
audio = (ROOT / "badapple-audio.wav").read_bytes()
encoded = base64.b64encode(gzip.compress(audio, compresslevel=9, mtime=0)).decode("ascii")

source = source.replace(
    "# Native 30 fps, complete video from the first frame. Audio uses the included WAV file.\n"
    "# Run: powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\\badapple-full.ps1",
    "# Native 30 fps, complete video from the first frame. Video and audio are embedded.\n"
    "# Run from CMD: powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\\badapple-windows.ps1",
    1,
)

frame_end = "'@\n$bytes = [Convert]::FromBase64String(($data -replace '\\s', ''))"
if source.count(frame_end) != 1:
    raise RuntimeError("Could not find end of frame payload")
source = source.replace(
    frame_end,
    "'@\n$audioData = @'\n" + "\n".join(encoded[i:i + 76] for i in range(0, len(encoded), 76)) + "\n'@\n"
    + "$bytes = [Convert]::FromBase64String(($data -replace '\\s', ''))",
    1,
)

old_audio = """$audioPlayer = $null
if (-not $NoAudio) {
    if ($Speed -ne 1.0 -or $StartAt -ne 0.0) {
        throw 'Audio stays in sync only at normal speed from the beginning. Add -NoAudio for speed or start-time changes.'
    }
    $audioPath = Join-Path $PSScriptRoot 'badapple-audio.wav'
    if (-not (Test-Path -LiteralPath $audioPath)) {
        throw 'Missing badapple-audio.wav next to the player. Add -NoAudio for silent playback.'
    }
    $audioPlayer = [System.Media.SoundPlayer]::new($audioPath)
    $audioPlayer.Load()
}"""
new_audio = """$audioPlayer = $null
$audioStream = $null
if (-not $NoAudio) {
    if ($Speed -ne 1.0 -or $StartAt -ne 0.0) {
        throw 'Audio stays in sync only at normal speed from the beginning. Add -NoAudio for speed or start-time changes.'
    }
    $audioBytes = [Convert]::FromBase64String(($audioData -replace '\\s', ''))
    $audioCompressed = [System.IO.MemoryStream]::new($audioBytes)
    $audioGzip = [System.IO.Compression.GzipStream]::new($audioCompressed, [System.IO.Compression.CompressionMode]::Decompress)
    $audioStream = [System.IO.MemoryStream]::new()
    try {
        $audioGzip.CopyTo($audioStream)
    } finally {
        $audioGzip.Dispose()
        $audioCompressed.Dispose()
    }
    $audioStream.Position = 0
    $audioPlayer = [System.Media.SoundPlayer]::new($audioStream)
    $audioPlayer.Load()
}"""
if source.count(old_audio) != 1:
    raise RuntimeError("Could not find original audio setup")
source = source.replace(old_audio, new_audio, 1)

old_cleanup = """        $audioPlayer.Dispose()
    }
    [Console]::Write"""
new_cleanup = """        $audioPlayer.Dispose()
    }
    if ($audioStream) { $audioStream.Dispose() }
    [Console]::Write"""
if source.count(old_cleanup) != 1:
    raise RuntimeError("Could not find original audio cleanup")
source = source.replace(old_cleanup, new_cleanup, 1)

target = ROOT / "badapple-windows.ps1"
target.write_bytes(source.replace("\n", "\r\n").encode("ascii"))
print(f"Built {target.name}: {target.stat().st_size:,} bytes")
