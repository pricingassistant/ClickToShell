"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['clicktoshell.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist' : {
        'CFBundleDevelopmentRegion' : 'en',
        'NSPrincipalClass' : 'NSApplication',
        'NSAppleScriptEnabled' : 'YES',
        'LSUIElement' : 'YES',
        'CFBundleIdentifier' : 'com.pricingassistant.clicktoshell',
        'CFBundleURLTypes' : [{
                'CFBundleURLName' : 'Click To Shell',
                'CFBundleURLSchemes' : [
                    'callto',
                    'tel',
                    'sms'
                ]
        }]
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
