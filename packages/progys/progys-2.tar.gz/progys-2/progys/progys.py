import sys
import os
from os import *

class Arguments():
    def __init__(self) -> None:
        for arg in sys.argv:
            ARGUMENT = arg

        if ARGUMENT == "--install":
            Instalization()

        elif ARGUMENT == "--help":
            HelpCommand()

class Instalization():
    def __init__(self) -> None:
        super().__init__()

        pkg = input("pkg: ")
        self.install_pkg(package=pkg)

        return None

    def install_pkg(self, package: str):
        os.system(f"pip install {package}")

        print("\ninstalled\nprogys by valahatiy\n")

        return None

class HelpCommand():
    def __init__(self) -> None:
        print("\n     info > \n\n --install [package name]\n --help [help command]\n\n     by valahatiy\n")

        return None

if __name__ == "__main__":
    Arguments()