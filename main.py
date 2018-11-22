import tkinter 
import glob
import os
import yaml


# Funktionen definieren

def changeLanguage(sprache):

    # finding Updated Folder
    list_of_files = glob.glob('C:\\Riot Games\\League of Legends\\RADS\\projects\\league_client\\releases\\*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)

    # Constant Folder
    data_folder = latest_file + '\\deploy\\'

    # Read in the file
    with open(data_folder + 'system.yaml', 'r') as file :
        filedata = file.read()

    # Replace the target string

    

    filedata = filedata.replace('- ru_RU', sprache)

    # Write the file out again
    with open(data_folder + 'system.yaml', 'w') as file:
        file.write(filedata)



    lb["text"] = "Auswahl: " + sprache.get()  


# Fenster erstellen

main = tkinter.Tk()

main.geometry("300x200")

# verfügbare Sprachen

sprache = tkinter.StringVar()

deutsch = tkinter.Radiobutton(main, text="Deutsch", variable=sprache, value="- de_DE")
deutsch.pack()

bshow = tkinter.Button(main, text = "Sprache wechseln", command = changeLanguage(sprache))
bshow.pack()
lb = tkinter.Label(main, text = "Auswahl: " )
lb.pack()

main.mainloop()