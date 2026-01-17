# Automated Nexus Mods Collection Download

This was made as a proof-of-concept auto-clicker for nexus mods downloads. Theoretically could be used to avoid clicking 1000 buttons when downloading Stardew Valley Mods. Also theoretically works great with the [Nexus No Wait ++](https://greasyfork.org/en/scripts/519037-nexus-no-wait) tampermonkey/greasemonkey script in your browser. 

I would recommend buying (or trial-run) Nexus Mods premium because the capped download speeds will make the process take hours anyways.

## Installation and usage

```bash
git clone github.com/adamhurm/automated_nexus_mods_collection_download
cd automated_nexus_mods_collection_download
python -m venv .venv
.venv/bin/activate     # (macOS/Linux)
.venv/Scripts/activate # (Windows)
pip install -r requirements.txt
python ./auto_clicker.py
```

## Note on images

This relies on the static images in this repo: [download_manually.png](download_manually.png) and [continue.png](continue.png)


If they change in the future, you could always use this same code and just replace with screenshots of the new buttons.
