import os
import json
import time

from git import Repo


class File:
    """All functions related to the json file are in this class."""

    def __init__(self):
        pass

    def openFile(self, fileName):
        """Opens txt file.

        :param fileName: (string): Complete filename with programming language.
        :return: list: Json of the txt file.
        """
        try:
            with open(fileName, encoding="utf8") as f:
                return json.load(f)
        except:
            print("Create default file")
            fileClass.writeToFile(fileName, None)

    def writeToFile(self, fileName, repoJson):
        """Writes to txt file.

        :param fileName: (string): Complete filename with programming language.
        :param repoJson: (list): The json object to written in the txt file.
        :return: list: Json of the txt file.
        """
        with open(fileName, "w", encoding="utf-8") as file:
            json.dump(repoJson, file, ensure_ascii=False, indent=5)

    def deleteFiles(self, files):
        """Remove file from os.

        :param files: (list): List of paths to be deleted.
        """
        for file in files:
            os.remove(file)

Error =[]
class CloneRepo:
    """Automatically downloads the repositories from the list."""

    def __init__(self, construct):
        """
        :param construct: The construct for which the functions from this class should be executed.
        """
        self.curConstruct = construct
        pass

    def cloneRepoFromList(self):
        """Clones all repos from the list."""
        dir = "./" + str(self.curConstruct) + "Repos.txt" # change dir here
        repos = fileClass.openFile(dir)

        print("Start with cloning.")
        for repo in repos["repositories"]:
            print("Current repo: " + str(repo["index"]))
            path = ("./git-repos/" + str(self.curConstruct).lower() + "/")

            repo_name = f'{repo["repoFullName"].replace("/", "-")}'
            full_path = path + repo_name
            if not os.path.isdir(full_path):
                try:
                    Repo.clone_from(
                        f'https://github.com/{repo["repoFullName"]}.git', full_path
                    )
                    time.sleep(5)
                except Exception as inst:
                    Error.append(str(repo["index"]))
                    print("Problem during cloning: " + str(inst))
            else:
                print("Already cloned")
        print("Done cloning.")
        if len(Error) > 0:
            print("Errors occurred during cloning:")
            for error in Error:
                print(f"Error with repo index: {error}")
        
        
fileClass = File()
cloning = CloneRepo("Callback")

cloning.cloneRepoFromList()