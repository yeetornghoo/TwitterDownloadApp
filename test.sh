#!/bin/bash

pip install -r requirements.txt

# Define status check for each test
exit_if_error() {
    local exit_code=$?
    if (( $exit_code )); then
        printf '\e[91mCheck failed!'
        exit 1
    fi
}

echo "Black - autoformatting"
black twitterdownloadapp --exclude env
exit_if_error