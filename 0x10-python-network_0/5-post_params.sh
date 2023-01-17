#!/bin/bash
# script to POST to url using curl displaying resonse body
curl -sX POST -F 'email=test@gmail.com' -F 'subject=I will always be here for PLD' $1
