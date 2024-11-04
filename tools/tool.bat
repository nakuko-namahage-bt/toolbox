@echo off

rem Set UTF-8 (if using Japanese)
chcp 65001

rem Execute Python script
python tool.py

rem Don't close console
rem cmd /k

rem Don't close console until entering some key
pause

rem Close console
exit
