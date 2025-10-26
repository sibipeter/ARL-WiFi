# ARLWiFi.spec

import sys
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

a = Analysis(
    ['main.py'],  # Update this path if your entry point is elsewhere
    pathex=[],
    binaries=[],
    datas=[
        ('assets/*', 'assets'),
        ('db/*', 'db'),
        ('logs/*', 'logs'),
    ],
    hiddenimports=collect_submodules('sqlite3'),
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ARL-WiFi',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='assets/icon.ico' if sys.platform == 'win32' else None,
    version='assets/version.txt' if sys.platform == 'win32' else None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ARL-WiFi'
)