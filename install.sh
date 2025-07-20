#!/bin/bash

if ! command -v ollama >/dev/null 2>&1; then
  echo "Ollama not found. Installing it..."
  curl -fsSL https://ollama.com/install.sh | sh >/dev/null
fi
echo "[OK] Ollama: installed!"

if [ -f requirements.txt ]; then
  echo "requirements.txt found. It may be necessary to create a venv and install requirements..."
  if [ ! -d venv ]; then
    python3 -m venv venv >/dev/null
  fi
  if [ ! -f venv/bin/activate ]; then
    rm -rf venv
    python3 -m venv venv >/dev/null
  fi
  source venv/bin/activate

  pip install -r requirements.txt --quiet --disable-pip-version-check
  echo "[OK] Pip requirements: installed!"
fi
