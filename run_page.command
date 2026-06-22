#!/bin/bash
# ============================================================
#  Run the HISPA site locally on macOS.
#
#  These pages are "Design Component" .dc.html files. At runtime
#  support.js uses fetch() to pull in the shared Nav and Footer.
#  Browsers BLOCK fetch() on file:// URLs, so the nav tabs and
#  footer only appear when the site is served over HTTP. This
#  script starts a tiny local web server and opens the home page.
#
#  HOW TO USE:
#    First time only, make it runnable (in Terminal, in this folder):
#        chmod +x run_page.command
#    Then just double-click run_page.command in Finder.
#    (Or run it any time with:  bash run_page.command)
#
#  Press Ctrl+C in the Terminal window, or close the window, to stop.
# ============================================================

# Move into the folder this script lives in.
cd "$(dirname "$0")" || exit 1

PORT=8000
PAGE="Home.dc.html"
URL="http://localhost:${PORT}/${PAGE}"

# --- Pick a web server: Python 3 preferred, then python, then Node. ---
if command -v python3 >/dev/null 2>&1; then
  SERVER=(python3 -m http.server "$PORT")
elif command -v python >/dev/null 2>&1; then
  SERVER=(python -m http.server "$PORT")
elif command -v npx >/dev/null 2>&1; then
  SERVER=(npx --yes http-server -p "$PORT" -c-1)
else
  echo ""
  echo "  ERROR: Python 3 or Node.js is required to run the local server."
  echo "  macOS usually has Python 3 once you install the Command Line Tools:"
  echo "      xcode-select --install"
  echo "  Or install Python from https://www.python.org/downloads/"
  echo ""
  read -n 1 -s -r -p "  Press any key to close..."
  exit 1
fi

echo ""
echo "  HISPA site - local server"
echo "  ========================="
echo "  Server : http://localhost:${PORT}"
echo "  Opening: ${URL}"
echo ""
echo "  Keep THIS Terminal window open while you use the site."
echo "  Press Ctrl+C (or close this window) to stop the server."
echo ""

# Open the browser a moment after the server comes up.
( sleep 1.5; open "$URL" ) &

# Run the server in the foreground so Ctrl+C / closing the window stops it.
exec "${SERVER[@]}"
