import os
import re
import subprocess


def get_ipv4():
    r = os.popen("ipconfig")
    text = r.read()

    ipv4 = re.findall(r'以太网适配器 以太网:(.*?)默认网关', text, re.S)[0]
    ipv4 = re.findall(r'IPv4 地址 . . . . . . . . . . . . :(.*?)子网掩码', ipv4, re.S)[0].replace(" ", "")

    return ipv4.strip()


def server_running(port=6379):
    with os.popen(f"netstat -ano | findstr {port}") as r:
        pids = set([i.strip() for i in re.findall('LISTENING(.*)', r.read())])

    return True if pids else False


def start_cmd(command, close=True):
    if close:
        process = subprocess.Popen(f'start cmd /c {command}', shell=True)
    else:
        process = subprocess.Popen(f'start cmd /k {command}', shell=True)
    return process.pid


def start_python_in_background(path, close=True):
    return start_cmd(command=f'python {path}', close=close)


def close_program_by_port(port):
    with os.popen(f"netstat -ano | findstr {port}") as r:
        pids = set([i.strip() for i in re(r.read(), 'LISTENING(.*?)\n')])

    for pid in pids:
        os.system(f"taskkill /PID {pid.strip()} /T /F")
