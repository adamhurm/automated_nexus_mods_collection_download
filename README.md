# Automated Nexus Mods Collection Download

This was made as a proof-of-concept auto-clicker for nexus mods downloads. Theoretically could be used to avoid clicking 1000 buttons when downloading Stardew Valley Mods. Also theoretically works great with the [Nexus No Wait ++](https://greasyfork.org/en/scripts/519037-nexus-no-wait) tampermonkey/greasemonkey script in your browser. 

I would recommend buying (or trial-run) Nexus Mods premium because the capped download speeds will make the process take hours anyways.

## Installation and usage

```bash
git clone github.com/adamhurm/automated_nexus_mods_collection_downloader
cd automated_nexus_mods_collection_downloader
python -m venv .venv
.venv/bin/activate     # (macOS/Linux)
.venv/Scripts/activate # (Windows)
pip install -r requirements.txt
python ./auto_clicker.py
```