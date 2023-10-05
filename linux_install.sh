#!/bin/bash

# Variables
python_version="3.10.0"
python_url="https://www.python.org/ftp/python/$python_version/Python-$python_version.tar.xz"
packages="python-dateutil matplotlib"

# Check if Python is already installed
if command -v python3 &>/dev/null; then
    echo "Python is already installed. Exiting."
    exit 1
fi

# Download Python
echo "Installing Python $python_version..."
curl -o python-installer.tar.xz "$python_url"
tar -xvf python-installer.tar.xz
cd Python-$python_version || exit

# Compile and install Python
./configure
make
sudo make install

# Check Python installation
if [ $? -ne 0 ]; then
    echo "Python installation failed. Exiting."
    exit 1
fi

# Upgrade pip
echo "Upgrading pip..."
sudo python3 -m ensurepip --default-pip
sudo python3 -m pip install --upgrade pip

# Install required packages
echo "Installing required Python packages..."
sudo python3 -m pip install "$packages"

# Check if installation was successful
echo "Verifying installation..."
python3 --version
python3 -m pip list | grep -E "$packages"

# Cleanup
cd ..
rm -rf Python-$python_version python-installer.tar.xz

# Done
echo "Installation completed successfully."
echo "You may need to start a new terminal session to use Python and the installed packages."
