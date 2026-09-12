@echo off
python -m pip install -U pyinstaller
pyinstaller --noconfirm --windowed --name "Train Traffic Simulator" --paths src src\ttc\__main__.py
