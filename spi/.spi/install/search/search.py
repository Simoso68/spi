from sys import argv
from os import chdir
from subprocess import run

try:
    from colorama import Fore, init
except ImportError:
    print("Missing dependency: colorama")
    print("Stopping SPI ...")
    exit()

chdir(f"/usr/bin/.spi/repositories/{argv[1]}/packages/{argv[2]}")
with open("instructions.json", "r") as r:
    run(["bash", "/usr/bin/.spi/install/reader/init.sh", "instructions", r.read()])

