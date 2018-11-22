# League of Legends Language Changer
# Finds the newest Folder in 
# C:\Riot Games\League of Legends\RADS\projects\league_client\releases
# Edits the system.yaml

import os
import datetime
# <><><><><><><><><><>  Get Today's Date  <><><><><><><><><><>
today = datetime.date.today()
today = str(today)
# <><><><><><><><><><>  Get Today's Files  <><><><><><><><><><>
folder = "C:/Riot Games/League of Legends/RADS/projects/league_client/releases"
print (folder)
folderContent = os.listdir(folder)
eligibleFiles = []
for i, file in enumerate(folderContent):
     if file.startswith(today):  # or -> if today in file
          eligibleFiles.append(file)
print(eligibleFiles)