if ($1 == "help") then
    if ($2 == "install") then
        echo "How to install a package:"
        echo "=========================="
        echo "sudo spi install {repository} {package}"
    elif ($2 == "remove") then
        echo "How to remove a package:"
        echo "========================="
        echo "sudo spi remove {repository} {package}"
    elif ($2 == "upgrade") then
        echo "How to upgrade all packages: "
        echo "=============================="
        echo "sudo spi upgrade"
    elif ($2 == "repo") then
        echo "How to install, remove and upgrade a repository: "
        echo "=================================================="
        echo "Install: "
        echo "sudo spi repo install {url}"
        echo "Remove: "
        echo "sudo spi repo remove {name}"
        echo "Upgrade: "
        echo "sudo spi repo upgrade {name}"
    else then
        echo "Please specify in what category you need help."
        echo "Following are available: "
        echo "install"
        echo "remove"
        echo "upgrade"
        echo "repo"
    fi
elif ($1 == "install") then
    bash /usr/bin/.spi/install/search/init.sh $2 $3
fi