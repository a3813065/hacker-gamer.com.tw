@echo off
setlocal enabledelayedexpansion

set INPUT_FILE=2.txt
set OUTPUT_FILE=666.txt

if not exist "%INPUT_FILE%" (
    echo 输入文件不存在！
    exit /b
)

rem 清空输出文件
type nul > "%OUTPUT_FILE%"

rem 逐行读取输入文件
for /f "usebackq tokens=*" %%a in ("%INPUT_FILE%") do (
    set "line=%%a"
    set "first_four=!line:~0,4!"
    rem 检查每行的前四个字符是否包含 "09"
    echo !first_four!| findstr "09" >nul
    if not errorlevel 1 (
        echo %%a>> "%OUTPUT_FILE%"
    )
)

echo 处理完成！
pause