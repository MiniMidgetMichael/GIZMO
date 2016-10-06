import sys, os


def determineOS():
    OS = sys.platform.casefold()
##    OS = "Linux-3.3.0-8.fc16.x86_64-x86_64-with-fedora-16-Verne"  #DEBUG
    win = (OS.find("win") != -1)
    if (win):
        return "win"
    else:
        return "*nix"

if __name__ == "__main__":
    OS = determineOS()
    print (OS)
