@echo off

call %CGRU_LOCATION%\software_setup\setup_maya.cmd
set "MAYA_MODULE_PATH=\\alpha\tools\Itsavile\tools\Itsalive\maya\plugins\MSLiveLink;%MAYA_MODULE_PATH%"
set "PYTHONPATH=\\alpha\tools\Itsavile\tools\Itsalive\maya\scripts;%PYTHONPATH%"

if "%GPU_LIST%" == "" (
    "%APP_DIR%\bin\Render.exe" %*
) else (
    "%APP_DIR%\bin\Render.exe" -r redshift -gpu %GPU_LIST% %*
)