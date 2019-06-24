# scan with nmap
from optparse import OptionParser
import nmap


# pass target host and target port to nmap
def nmapScan(tgtHost, tgtPort):
    nScan = nmap.PortScanner()
    nScan.scan(tgtHost, tgtPort)
    state = nScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print(" [*] " + tgtHost + " tcp/" + tgtPort + " " + state + '\n')


def main():
    usage = "usage: %prog -H <target host> -p <target port>"
    parser = OptionParser(usage)
    parser.add_option('-H', dest='tgtHost', type='string',
                      help='specify target host IP or FQDN')
    parser.add_option('-p', dest='tgtPort', type='string',
                      help='specify target port[s] comma separated: 22,80')
    (options, args) = parser.parse_args()
    if (options.tgtHost is None) or (options.tgtPort is None):
        parser.error("Wrong number of arguments")
        return 0
    else:
        tgtHost = options.tgtHost
        tgtPorts = str(options.tgtPort).split(',')

    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort)


if __name__ == "__main__":
    main()
