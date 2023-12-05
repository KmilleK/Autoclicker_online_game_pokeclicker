# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['autoclicker_hdl\\main.py'],  # Adjust the path to main.py if needed
    pathex=['C:\\Users\\camil\\Documents\\Python Scripts\\Autoclicker'],
    binaries=[],
    datas=[('autoclicker_hdl/clicker_action/**', 'clicker_action'),
           ('autoclicker_hdl/common/**', 'common'),
	('autoclicker_hdl/listener/**', 'listener'),
	('autoclicker_hdl/UI/**', 'UI'),
	('data/**','data')
	],
    hiddenimports=['pynput','sip'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
