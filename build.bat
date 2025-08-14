@echo off
REM Build script for Windows
REM exit on error

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

echo Build completed successfully!
pause
