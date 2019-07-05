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
                print(soFile)
        rename(soFile.strip("\n"), fileName.strip(".pyx") + ".so")
        system("ls -al")
        print("Write: import " + fileName.strip(".so"))
        system("python")
        
main()