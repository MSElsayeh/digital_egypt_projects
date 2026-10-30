#!/bin/bash

while true; do
    echo "Welcome to DECI's Password Manager"
    echo 'To create your master key, write "create master"'
    echo 'To add a new entry, write "create entry"'
    echo 'To retrieve an entry, write "get entry"'
    echo 'To exit, write "exit"'

    read -p "Enter your command: " command

    case $command in
        "create master")
            python3 Masterkey_creationandHashing.py
            ;;
        "create entry")
            python3 Storing_Passwords.py
            ;;
        "get entry")
            python3 Retrieving_Passwords.py
            ;;
        "exit")
            echo "Exiting DECI's Password Manager. Goodbye!"
            break
            ;;
        *)
            echo "Invalid command. Please try again."
            ;;
    esac
    echo ""
done