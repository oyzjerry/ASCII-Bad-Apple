"""Rebuild the cross-platform single-file player from the source script and WAV."""

from pathlib import Path
import shutil
import tempfile
import zipapp


root = Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix='.zipapp-', dir=root) as temporary:
    staging = Path(temporary)
    shutil.copy2(root / 'badapple-full.py', staging / '__main__.py')
    shutil.copy2(root / 'badapple-audio.wav', staging / 'badapple-audio.wav')
    zipapp.create_archive(
        staging,
        root / 'badapple.pyz',
        interpreter='/usr/bin/env python3',
        compressed=True,
    )
print(f'Created {root / "badapple.pyz"}')
