#!/usr/bin/python3
from os import system, rename

def main():
        print("Generating file...")
        fileName = input("Enter the name of your pyx file(with suffix).\n")
        with open("setup.py", "w") as f:
                f.write("from distutils.core import setup\n" +
                        "from Cython.Build import cythonize\n" +
                        "setup(\n" + 
                        "\text_modules = cythonize(" + "\"" + fileName + "\"" + ")\n" +
                        ")\n")
        
        system("python setup.py build_ext --inplace")
        system("ls "+ fileName.strip(".pyx") + ".cp* > file.txt")
        with open("file.txt", "r") as f:
                soFile = f.read()
        system("rm file.txt")
        fileName = fileName.strip(".pyx")
        rename(soFile.strip("\n"), fileName + ".so")
        system("\nls -al\n")
        with open("run.py", "w") as f:
                f.write("import " + fileName)
        system("python run.py")
       
main()
