from tkinter.tix import WINDOW
from traceback import format_exc

import requests
from tkinter import *

window = Tk()
window.title("Poggit Browser")
window.iconphoto(False, PhotoImage(file="poggit.png"))
entry = Entry(window, width=50)
entry.pack()
entry.insert(0, "Enter the desired project.")

def submitProject():
    project = entry.get()
    releases = requests.get("https://poggit.pmmp.io/releases.json?name=" + project).json()

    if len(releases) == 0:
        text = "Please specify an existing project."
    else:
        text = "Found " + project + "."

    Label(window, text=text).pack()

    entryTwo = Entry(window, width=50)
    entryTwo.pack()
    entryTwo.insert(1, "Enter the desired version.")

    def submitVersion():
        version = entryTwo.get()
        releases = requests.get("https://poggit.pmmp.io/releases.json?name=" + entry.get()).json()

        for release in releases:
            if version == release["version"]:
                selected = release
                break

        try:
            selected
        except NameError:
            Label(window, text="Please enter a valid version.").pack()
        else:
            Label(window, text="Found version " + version).pack()

            entryThree = Entry(window, width=50)
            entryThree.pack()
            entryTwo.insert(2, "Enter the desired information.")

            def submitInformation():
                information = entryThree.get()

                if information not in selected.keys():
                    Label(window, text="Please specify valid information of the project, list found at https://github.com/poggit/support/blob/master/api.md.").pack()
                else:
                    Label(window, text=project + " " + version + " " + information + ": " + str(selected[information])).pack()
            informationButton = Button(window, text="Submit Information", command=submitInformation)
            informationButton.pack()

    versionButton = Button(window, text="Submit Version", command=submitVersion)
    versionButton.pack()

projectButton = Button(window, text="Submit Search", command=submitProject)
projectButton.pack()

window.mainloop()