#!/bin/bash
# A script to set email and subject header variables
curl -s -X POST -d "email: test@gmail.com&subject: I will always be here for PLD" "$1"
