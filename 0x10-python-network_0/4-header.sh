#!/bin/bash
# script that takes URLwith GET and sends header variable X-School-User-Id with the value 98
curl -s -X GET -H "X-School-User-Id: 98" "$1"
