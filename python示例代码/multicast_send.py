import socket
import argparse

#python multicast_send.py --mcast-group '224.1.1.2'

def run(group, port):
    MULTICAST_TTL = 20
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
    sock.sendto(b'from multicast_send.py: ' +
                f'group: {group}, port: {port}'.encode(), (group, port))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mcast-group', default='224.1.1.1')
    parser.add_argument('--port', default=19900)
    args = parser.parse_args()
    run(args.mcast_group, args.port)