#!/bin/bash

# Function to install pip
install_pip() {
    echo "Pip not found. Installing pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
}

# Check if pip is installed
if ! command -v pip3 >/dev/null; then
    install_pip
else
    echo "Pip is already installed."
fi

# Install required packages
echo "Installing required packages..."
pip3 install pytube
pip3 install tkinter

echo "Installation completed."