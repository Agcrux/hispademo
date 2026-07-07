@echo off
REM ============================================================
REM  Run the HISPA site locally.
REM
REM  These pages are "Design Component" .dc.html files. At
REM  runtime support.js uses fetch to pull in the shared Nav
REM  and Footer. Browsers BLOCK fetch on file:// URLs, so the
REM  nav tabs / footer only appear when the site is served over
REM  HTTP. This script starts a tiny local web server and opens
REM  the home page in your browser.
REM
REM  Just double-click this file. A second window titled
REM  "HISPA local server" is the web server - close it to stop.
REM ============================================================

setlocal
cd /d "%~dp0"

set "PORT=8000"
set "PAGE=Home.dc.html"
set "URL=http://localhost:%PORT%/%PAGE%"

REM --- Pick a web server: Python preferred, Node fallback. ---
REM --- goto labels are used instead of if-blocks on purpose: ---
REM --- parentheses inside if-blocks break .bat parsing.       ---
set "SERVER="
where python >nul 2>nul && set "SERVER=python -m http.server %PORT%"
if defined SERVER goto run
where py >nul 2>nul && set "SERVER=py -m http.server %PORT%"
if defined SERVER goto run
where npx >nul 2>nul && set "SERVER=npx --yes http-server -p %PORT% -c-1"
if defined SERVER goto run
goto nofound

:run
echo.
echo   HISPA site - local server
echo   =========================
echo   Server : http://localhost:%PORT%
echo   Opening: %URL%
echo.
echo   A second window titled "HISPA local server" is the web server.
echo   Close THAT window to stop the site.
echo.

REM Start the web server in its own window.
start "HISPA local server" %SERVER%

REM Give it a moment to start, then open the browser.
ping -n 3 127.0.0.1 >nul
start "" "%URL%"

echo   Browser launched. You can close this window now.
echo.
pause
goto end

:nofound
echo.
echo   ERROR: Python or Node.js is required to run the local server.
echo   Install Python from https://www.python.org/downloads/
echo   then tick "Add python.exe to PATH" and run this file again.
echo.
pause

:end
endlocal
