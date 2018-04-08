#!/usr/bin/python3
import subprocess

def main():
        rules()


def rules():
        cmd("iptables -L")

def cmd(command):
        subprocess.run(command, shell=True, check=True)

main()

