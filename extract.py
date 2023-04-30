import platform,sys,os.path
if platform.python_version_tuple()[0] == "2":
    from Steam2.package import Package
    import Tkinter, tkFileDialog
    tkinter = Tkinter
    tkinter.filedialog = tkFileDialog
else:
    from Steam2.package3 import Package
    import tkinter, tkinter.filedialog
    
root = tkinter.Tk()
root.withdraw()

def main():
    if len(sys.argv) == 3:
        file_path = sys.argv[1]
        dir =  os.path.normpath(sys.argv[2])+ "\\"
    if not file_path:
        file_path = tkinter.filedialog.askopenfilename(title="Select PKG",initialdir=".")
    if file_path == "":
        exit()
    else:
        #filename = "SteamNew.exe"
        f = open(file_path, "rb")
        pkg = Package(f.read())
        #print(pkg.filenames)
        f.close()
        if not dir:
            dir = tkinter.filedialog.askdirectory(title="Select output directory") + "\\"
        if dir == "":
            exit()
        #print(dir)
        for f in pkg.filenames:
            fn = f.decode("utf-8")
            ff = open(dir+fn,"wb")
            ff.write(pkg.get_file(f))
            ff.close()
    
main()