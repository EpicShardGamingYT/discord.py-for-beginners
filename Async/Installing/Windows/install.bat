@echo off
echo Make sure batch is on desktop before you run
set /p "block="
cls
echo Checking if you installed python...
echo -----------------------------------
cd ..
cd AppData\Local\Programs
cd Python
cd Python36 || Python35
if exist python.exe (
    echo Python Is Installed!
    echo -------------------------------------------------------
    goto install
)
if not exist python.exe (
    echo Python is not found! either you havent installed it or it is in another path, it is recommended that you have to install it or check it by yourself!
    echo Install Python from https://www.python.org if you haven't
    echo -------------------------------------------------------
    echo if you have checked and python is installed, do 'y', if not then do 'n'
    set /p "cho=>"
    if %cho%==Y goto install
    if %cho%==y goto install
    if %cho%==n goto pase
    if %cho%==N goto pase
)

:install
python -m pip install discord.py --disable-pip-version-check
echo -------------------------------------------------------
echo Done installing discord.py (or if you have it already installed, it should show that requirements already satisfied thing)
goto pase

:pase
pause
