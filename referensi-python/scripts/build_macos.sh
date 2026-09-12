#!/usr/bin/env bash
set -euo pipefail
python -m pip install -U pyinstaller
pyinstaller --noconfirm --windowed --name "Train Traffic Simulator" --paths src src/ttc/__main__.py
