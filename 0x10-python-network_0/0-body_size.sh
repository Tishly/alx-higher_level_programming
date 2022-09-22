#!/bin/bash
# A script that takes in and sends a request to a URL, then displays the content-length
curl -sI "{$url}" | grep -i content-lenght
