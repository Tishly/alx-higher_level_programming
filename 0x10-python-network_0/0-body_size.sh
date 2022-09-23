#!/bin/bash
# A script that takes in and sends a request to a URL, then displays the content-length
curl -sI '$1' | grep -iE 'Content-Lenght: [0-9]+' | cut -d ' ' -f2
