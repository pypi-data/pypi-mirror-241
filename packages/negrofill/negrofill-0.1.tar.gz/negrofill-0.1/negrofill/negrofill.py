import sys
import os

class Help():
    def __init__(self) -> None:
        print("\nThis Test Help Command\n--help\n")

class Package_Installer():
    def __init__(self, pkg) -> None:
        print()
        os.system(f"pip install {pkg}")

if __name__ == "__main__":
    try:
        FIRST_ARG = sys.argv[1]
        SECOND_ARG = sys.argv[2]
        THIRD_ARG = sys.argv[3]
        FOURTH_ARG = sys.argv[4]
        FIVETH_ARG = sys.argv[5]

    except:
        pass

    try:
        if FIRST_ARG == "--help":
            Help()

        if FIRST_ARG == "--install":
            Package_Installer(pkg=sys.argv[2])

    except:
        pass