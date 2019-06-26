@echo off
echo Begin configuring Python environment.
pip install -r ..\..\requirements.txt
echo Python Environment configuration completed.
timeout /t 10