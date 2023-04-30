import platform,sys,os.path
if platform.python_version_tuple()[0] == "2":
    from Steam2.package import Package
else:
    from Steam2.package3 import Package
    
def main():
    if len(sys.argv) == 2:
        pkgfile = sys.argv[1]
    else:
        print("usage: probepkg.py <pkg_file>")
        exit()
    f = open(pkgfile, "rb")
    pkg = Package(f.read())
    f.close()
    print("Files:")
    for n in pkg.filenames:
        print("     " + n.decode("utf-8"))
    print("Unpacked file sizes:")
    for k,v in pkg.file_unpacked_sizes.items():
        print("     "+k.decode("utf-8") + ": " + str(v))
    print("PKG Version: " + str(pkg.pkg_ver))
    print("PKG Compression level: " + str(pkg.compress_level))
    print("PKG File chunks amount: " + str(len(pkg.file_chunks)))
main()