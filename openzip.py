import zipfile
from optparse import OptionParser
from threading import Thread

# Uses brute force to unlock a password protected zip file
# Takes the name of the zip file and dictonary files as arguements
# Returns the password to the zip file
# Uses optparse to parse command line arguements and print help messages
# Uses threading to speed up the program
# Wrote this for Python3


def extract_zip(zfile, password):
    try:
        # convert the password string to bytes or there's an error
        password_bytes = password.encode()
        zfile.extractall(pwd=password_bytes)
        print("[+] Password Found: " + password + '\n')
    except RuntimeError:
        pass


def main():
    usage = "usage: %prog -f <zipfile> -d <dictionary file>"
    parser = OptionParser(usage)
    parser.add_option('-f', dest='zname', type='string',
                      help='specify zip file')
    parser.add_option('-d', dest='dname', type='string',
                      help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname is None) or (options.dname is None):
        parser.error("Wrong number of arguments")
        return 0
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)

    # read the dictionary file line by line and
    # call extract_zip to see if it's the right password
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extract_zip, args=(zFile, password))
        t.start()


if __name__ == "__main__":
    main()