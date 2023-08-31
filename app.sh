#!/bin/bash

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python -m venv .venv
fi

echo "[*] activating virtual environment"
source .venv/bin/activate

echo "[*] installing python packages..."
pip install scikit-learn Flask
python app.py

echo "[*] opening in the browser"
python -c "import webbrowser; webbrowser.open('$app_url')"
wait
echo "[*] click Ctl+C to cancel"
deactivate
deactivate
