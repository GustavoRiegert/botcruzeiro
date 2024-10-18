import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Lista de pacotes que você precisa
packages = [
    'selenium',
    'pyautogui',
    'pyperclip',
    'screeninfo'
]

for package in packages:
    try:
        __import__(package)
    except ImportError:
        install(package)
