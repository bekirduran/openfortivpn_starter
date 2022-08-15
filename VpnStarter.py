from getpass import getpass
import argparse
import os

if __name__ == '__main__':
    #"""https://github.com/bekirduran"""#
    parser = argparse.ArgumentParser("BekirDuran VPN Script")
    parser.add_argument('-s', '--sudo', type=str, help='Sudo password [MUST]')
    parser.add_argument('-p', '--password', type=str, help='Vpn password [MUST]')
    parser.add_argument('-a', '--auth', type=str, help='Authenticator code [MUST]',)
    parser.add_argument('-u', '--username', type=str, help='Vpn username ', default='')
    parser.add_argument('-i', '--ip', type=str, help='Host ip', default='')
    parser.add_argument('-t', '--port', type=str, help='Host post', default='')
    parser.add_argument('-c', '--cert', type=str, help='Trusted cert', default='64d05a2b29cd5d5c1434f21a619bd582a8949a6099f53c28e5cfecd2c9aff2e8')
    args = parser.parse_args()

    args.sudo = getpass("Sudo Password: ")
    args.password  = getpass("VPN Password: ")
    args.auth = input("Authenticator Code: ")

    command = f"openfortivpn {args.ip}:{args.port} -u {args.username} -p {args.password} --otp {args.auth} --trusted-cert {args.cert}"
    os.system("echo %s | sudo -S %s" %(args.sudo,command))
