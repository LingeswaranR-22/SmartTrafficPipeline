@echo off
echo Running SmartTrafficPipeline...

REM Change to your project directory
cd /d C:\Users\ADMIN\SmartTrafficPipeline

REM Activate virtual environment
call .venv\Scripts\activate

REM Run the pipeline
python pipeline.py

pause

