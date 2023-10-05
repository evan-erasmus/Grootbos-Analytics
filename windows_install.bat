@echo off
setlocal

:: Variables
set "python_version=3.10.0"
set "python_url=https://www.python.org/ftp/python/%python_version%/python-%python_version%-amd64.exe"
set "packages=python-dateutil matplotlib"

:: Check if Python is already installed
where python >nul 2>&1
if %errorlevel% equ 0 (
    echo Python is already installed. Exiting.
    exit /b 1
)

:: Download Python
echo Installing Python %python_version%...
bitsadmin /transfer python-download /priority normal %python_url% python-installer.exe
python-installer.exe /quiet PrependPath=1 Include_test=0

:: Check Python installation
if %errorlevel% neq 0 (
    echo Python installation failed. Exiting.
    exit /b 1
)

:: Upgrade pip
echo Upgrading pip...
python -m ensurepip --default-pip
python -m pip install --upgrade pip

:: Install required packages
echo Installing required Python packages...
python -m pip install %packages%

:: Check if installation was successful
echo Verifying installation...
python --version
python -m pip list | findstr "%packages%"

:: Cleanup
echo Cleanup...
del /q python-installer.exe

:: Done
echo Installation completed successfully.
echo You may need to restart your command prompt or shell to use Python and the installed packages.
endlocal