#!/bin/bash
cd "$(dirname "$0")"

read -n 1 -s -r -p "YOU ARE FAST PUSHING MAIN!!! ARE YOU SURE?"
"../../.tools/PortableGit/bin/git.exe" add .
"../../.tools/PortableGit/bin/git.exe" commit -m "FAST PUSH MAIN"
"../../.tools/PortableGit/bin/git.exe" push
read -n 1 -s -r -p "done"

# in powershell it goes like this
# hard reset committs
# &"../../.tools/PortableGit/bin/git.exe" reset --hard HEAD~1
# REM check commits
# &"../../.tools/PortableGit/bin/git.exe" log --oneline
# REM do once for flexability
# &"../../.tools/PortableGit/bin/git.exe" remote set-url origin https://ТВОЙ_ТОКЕН@github.com/Konfermat/python-practice.git