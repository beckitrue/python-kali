# playing with sockets


def create_socket():
    # create a socket
    import socket
    from requests import get

    s = socket.socket()
    print("socket created")

    # select port to listen on
    port = int(input('Enter the port to listen on: '))

    # bind socket and port
    s.bind(('', port))
    print("socket is bound to port: {:d}".format(port))

    # put the socket in listening mode
    s.listen(5)
    print("socket is now listening")

    # find and print our public IP address
    ip = get('https://api.ipify.org').text
    print('My public IP address is: {}'.format(ip))

    # listen until we interrupt the program or it gets an error
    # print a message when we get a connection on the socket we created
    while True:
        conn, addr = s.accept()
        incoming_ip, port = addr
        print('received connection from: {}'.format(incoming_ip))

        geolocation(incoming_ip)


def geolocation(ip):
    # will call ipfy api to do geolocation
    # get fancy with geolocation
    import json

    # open config.json file that has API URL and API Key
    with open('config.json', 'r') as f:
        config = json.load(f)

    geo_url = config['DEFAULT']['API_ENPOINT_IPIFY']
    geo_key = config['DEFAULT']['API_KEY_IPIFY']

    try:
        from urllib.request import urlopen
    except ImportError:
        from urllib2 import urlopen

    url = geo_url + geo_key + '&ipAddress=' + ip

    print(urlopen(url).read().decode('utf8'))

    return


def main():
    # open a socket to listen on
    create_socket()


main()
