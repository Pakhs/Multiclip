# Multiclip

Multiclip is a simple script that can save and recover multiple clipboards\
Only Linux support

## Installation
Download the [zip file](https://github.com/Pakhs/Multiclip/archive/refs/heads/main.zip) or clone the repository on your specified foldier

You will need to install the dependencies using the provided script
```bash
sh setup.sh
```
To run the script you need to first give it executable permissions
```bash
sudo chmod +x multiclip.py
```

# Usage
## Save
This command saves your current clipboard to the file (if already in there, it overrides it) using a key 
```bash
./multiclip.py -s [key]
```
## Load
This command load a saved clipboard to your current clipboard
```bash
./multiclip.py -l [key]
```
## Remove
This command removes a saved clipboard from the file
```bash
./multiclip.py -r [key]
```
## Print
This command prints all your saved clipboards 
```bash
./multiclip.py -p
```

