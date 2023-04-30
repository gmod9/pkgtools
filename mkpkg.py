import platform,sys,os.path,os
if platform.python_version_tuple()[0] == "2":
    from Steam2.package import Package
    import Tkinter, tkFileDialog
    tkinter = Tkinter
    tkinter.filedialog = tkFileDialog
else:
    from Steam2.package3 import Package
    import tkinter, tkinter.filedialog

def main():
    if len(sys.argv) == 3:
        files_dir = os.path.normpath(sys.argv[1])+ "\\"
        outfile =  sys.argv[2]
    else:
        files_dir = tkinter.filedialog.askdirectory(title="Select input directory") + "\\"
        outfile = tkinter.filedialog.asksaveasfilename(title="Save target PKG file",initialdir=".")
        if dir == "" or outfile == "":
            exit()
    pkg = Package()
    listdir = os.listdir(files_dir)
    for f in listdir:
        if os.path.isfile(files_dir+f):
            data = open(files_dir+f,"rb")         
            pkg.put_file(bytes(f, 'utf-8'),data.read())
            data.close()
    pkgfile = open(outfile,"wb")
    pkgfile.write(pkg.pack())
    pkgfile.close()

main()