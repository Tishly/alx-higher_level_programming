#!/bin/bash
# A script that takes in and sends a request to a URL, then displays the content-length
curl -sI "$1" | grep 'Content-Lenght' | cut -d ' ' -f 2
