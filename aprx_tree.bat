@echo off
REM This batch file launches the ArcGIS Pro Python environment to run the aprx-tree-viewer.py script

REM Define the path to the ArcGIS Pro Python executable
set PythonPath="C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"

REM Define the relative path to the aprx-tree-viewer-run.py script
set ScriptPath="%~dp0aprx_tree_viewer_run.py"

REM Check if the second argument (aprx file path) was provided

if "%~1"=="" (
    echo No .aprx file specified. Please provide a path to an .aprx file.
    exit /b 1
    pause
)

REM Launch the Python script with the provided .aprx file path as the argument
%PythonPath% "%ScriptPath%" "%~1"

