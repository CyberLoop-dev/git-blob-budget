<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:14b8a6&height=170&section=header&text=Git%20Blob%20Budget&fontColor=ffffff&fontSize=38&animation=fadeIn" alt="Git Blob Budget banner" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=19&duration=3000&pause=900&color=14B8A6&center=true&vCenter=true&width=820&lines=Find+the+biggest+objects+in+Git+history" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/git-blob-budget)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/git-blob-budget)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/git-blob-budget?style=flat)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/git-blob-budget)

<img src="assets/illustration.svg" alt="Git history size illustration" width="92%"/>

</div>

## :compass: Overview
A read-only CLI that ranks the largest file blobs reachable from Git refs, helping teams spot accidental binaries and repository history growth before clones become expensive.

## :sparkles: Features
- :mag: Scans reachable Git objects without checking out files
- :package: Ranks historical blobs by size and path
- :control_knobs: Supports a minimum-size threshold and JSON output
- :shield: Never rewrites history or deletes objects

## :clapper: Demo
```bash
python main.py --repo . --min-mb 0.5 --limit 10
```
The command prints the largest matching blobs in the selected repository.

## :rocket: Quick Start
```bash
python -m pip install -r requirements.txt
python main.py --repo . --min-mb 1
```
Git must be installed and available on PATH.

## :toolbox: Tech Stack
- Python 3.10+ standard library
- unittest
- Local, read-only Git inspection

## :file_folder: Folder Structure
```text
git-blob-budget/
├── main.py
├── requirements.txt
├── tests/test_core.py
├── examples/README.md
└── assets/illustration.svg
```

## :world_map: Roadmap
- [x] Read-only object inventory
- [x] Human-readable and JSON reports
- [ ] Optional CSV export
- [ ] GitHub Actions summary output

## :handshake: Contributing
Issues and pull requests are welcome. Keep changes focused and add tests for new behavior.

## :page_facing_up: License
MIT - see [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:14b8a6,100:0f172a&height=100&section=footer" alt="Animated wave footer" width="100%"/></div>
