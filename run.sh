#!/bin/bash

if [ "$1" == "--install" ]; then
  echo "Installation in progress..."
  chmod +x install.sh
  ./install.sh
  echo -e "Finished installation.\n"
fi

echo "Running Ollama server and Django webserver..."

if ! pgrep -f "ollama serve" >/dev/null; then
  echo "Ollama server not found. Starting it..."
  ollama serve >> ollama.log 2>&1 &
  OLLAMA_PID=$!
  trap "kill $OLLAMA_PID" EXIT
fi
echo "[OK] Ollama server: on!"

if [ -f requirements.txt ]; then
  source venv/bin/activate
fi

echo "Starting Django dev webserver..."
python3 manage.py migrate >> django.log 2>&1 &
python3 manage.py runserver >> django.log 2>&1 &
DJANGO_PID=$!
trap "kill $DJANGO_PID" EXIT
echo "[OK] Django webserver: on!"

echo -e "\nYou can track the servers logs using:"
echo "- Ollama: tail -f ollama.log"
echo "- Django: tail -f django.log"
echo "- Both: tail -f ollama.log django.log"
echo -e "\nBoth Ollama and Django processes are tied to this."
echo "You can end all processes sending a SIGKILL (ctrl+c)."

wait
