from sys import argv
from subprocess import run
from json import loads, JSONDecodeError

try:
    j = loads(argv[1])
except JSONDecodeError:
    print("ERROR: Invalid JSON format!")
    exit()

try:
    download = j["download"]["url"]
    mirrors = j["download"]["mirrors"]
    if len(mirrors) == 0:
        print("No mirrors provided!")
    dependencies = j["dependencies"]
    location = j["location"]
    pre = j["preinstall"]
    post = j["postinstall"]
except KeyError:
    print("ERROR: Missing keys in JSON!")
    exit()
else:
    if len(dependencies) < 0:
        print("Downloading dependencies ...")
        for dependency in dependencies:
            run(["sudo", "bash", "/usr/bin/.spi/install/managers/init.sh", "dependency", dependency])
    else:
        print("No dependencies detected.")
    print("Installing main package ...")
    run(["sudo", "bash", "/usr/bin/.spi/install/download/get.sh", download, location])

    # --- INDEV --- #
    try:
        ...
    except FileNotFoundError:
        ...