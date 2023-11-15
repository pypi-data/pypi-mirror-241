# run with testfiles
# testfiles is a list of files inside the test directory

import os
import shutil

def main():
    # current directory
    cwd = os.getcwd()
    # mkdir for input and output
    os.system("mkdir " + cwd + "/test/input")
    os.system("mkdir " + cwd + "/test/output")
    # copy testfiles to input
    for file in os.listdir(cwd + "/test"):
        file = str(file)
        if file.endswith(".csv"):
            shutil.copy(cwd + "/test/" + file, cwd + "/test/input")
    # run chainmerger and set input and output, then remove input
    os.system("python3 chainmerger.py -i " + cwd + "/test/input -o " + cwd + "/test/output")
    os.system("rm -rf " + cwd + "/test/input/*")
    # wait until enter is pressed
    
    print(" _______        _    __ _ _                                _       ")
    print("|__   __|      | |  / _(_) |                              | |      ")
    print("   | | ___  ___| |_| |_ _| | ___  ___   _ __ ___  __ _  __| |_   _ ")
    print("   | |/ _ \/ __| __|  _| | |/ _ \/ __| | '__/ _ \/ _` |/ _` | | | |")
    print("   | |  __/\__ \ |_| | | | |  __/\__ \ | | |  __/ (_| | (_| | |_| |")
    print("   |_|\___||___/\__|_| |_|_|\___||___/ |_|  \___|\__,_|\__,_|\__, |")
    print("--------------------------------------------------------------__/ |")
    print("-------------------------------------------------------------|___/ ")
    print("-------------------------------------------------------------------")
    print("Check the output directory to debug.")
    input("Press enter to clean test directory...")
    print("-------------------------------------------------------------------")

    # remove output and input
    os.system("rm -rf " + cwd + "/test/output")
    os.system("rm -rf " + cwd + "/test/input")

if __name__ == "__main__":
    main()