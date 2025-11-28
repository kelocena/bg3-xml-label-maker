# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['app\\index.py'], # main file
    pathex=[], # a list of paths to search for imports, i.e. 'app\\imports'
    binaries=[],
    datas=[('app\\indices', 'app\\indices')], # my non .py files ('src', 'dst in bundled app')
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='BG3_LabelMaker',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='BG3_LabelMaker',
)
