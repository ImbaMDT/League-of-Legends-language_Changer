# LoL NameChanger 2018
# Updates von LoL Datein checken
# Path von den Neusten Datein finden
# Russland zu Deutschland ändern

# Auswahl der Regionen und Sprachen
# Bessere .exe mit weniger Datein und Icon entwerfen

import glob
import os
#from pathlib import Path
import yaml
import fileinput

# finding Updated Folder
list_of_files = glob.glob('C:\\Riot Games\\League of Legends\\RADS\\projects\\league_client\\releases\\*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

# Constant Folder
data_folder = latest_file + '\\deploy\\'

# Read in the file
with open(data_folder + 'system.yaml', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('- ru_RU', '- de_DE')

# Write the file out again
with open(data_folder + 'system.yaml', 'w') as file:
  file.write(filedata)

