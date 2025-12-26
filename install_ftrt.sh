#!/data/data/com.termux/files/usr/bin/bash
# install_ftrt.sh
pkg update
pkg install python python-scikit-learn python-numpy python-pandas python-matplotlib
pip install --upgrade pip
pip install -r requirements.txt  # si tienes uno
