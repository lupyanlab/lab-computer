# Setting up a computer to run psychopy experiments

This repo contains information and instructions for running cognitive psychology experiments on macOS and Windows computers.

## Download this repo

To use this repo, download the .zip file from here: <https://github.com/lupyanlab/lab-computer/archive/master.zip>

## Clone this repo

If you are familiar with `git` you can clone the repo. That way you can stay up to date with the latest changes.

```bash
git clone https://github.com/lupyanlab/lab-computer.git
```

For detailed installation instructions and troubleshooting, see the wiki for this repo here: <https://github.com/lupyanlab/lab-computer/wiki>

## What can I do once I have this repo?

```bash
cd ~/lab-computer  # wherever the repo is unzipped or cloned

# If you have `conda` installed,
# install the lab environment
conda create -f anaconda-environments/psychopy-environment-macos.yml

# Activate the lab environment named "psychopy"
source activate psychopy

# Test psychopy
cd psychopy-tests/

# List available tests
ls test_*.py

# Run tests
python test_psychopy.py
python test_psychopy_sound.py
```
