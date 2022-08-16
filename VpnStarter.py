from getpass import getpass
import subprocess
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Bekir DURAN VPN Script")
    parser.add_argument('-s', '--sudo', type=str, help='Sudo password [MUST]')
    parser.add_argument('-p', '--password', type=str, help='Vpn password [MUST]')
    parser.add_argument('-a', '--auth', type=str, help='Authenticator code [MUST]',)
    parser.add_argument('-u', '--username', type=str, help='Vpn username ', default='bekir.duran')
    parser.add_argument('-i', '--ip', type=str, help='Host ip', default='85.105.135.252')
    parser.add_argument('-t', '--port', type=str, help='Host post', default='10443')
    parser.add_argument('-c', '--cert', type=str, help='Trusted cert', default='64d05a2b29cd5d5c1434f21a619bd582a8949a6099f53c28e5cfecd2c9aff2e8')
    args = parser.parse_args()

    args.password  = getpass("VPN Password: ")
    args.auth = input("Authenticator Code: ")
    
    subprocess.call(["sudo","openfortivpn", f"{args.ip}:{args.port}", "-u", f"{args.username}", "-p", f"{args.password}", "--otp", f"{args.auth}", "--trusted-cert", f"{args.cert}"], shell=False)
