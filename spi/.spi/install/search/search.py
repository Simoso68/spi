from sys import argv
from os import chdir
from subprocess import run

chdir(f"/usr/bin/.spi/repositories/{argv[1]}/packages/{argv[2]}")
with open("instructions.json", "r") as r:
    run(["bash", "/usr/bin/.spi/install/reader/init.sh", "instructions", r.read()])

