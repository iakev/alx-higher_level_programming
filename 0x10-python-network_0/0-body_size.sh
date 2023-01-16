#!/bin/bash
# script taking in a URL, sending a request to the URl,displaying size of conte
curl $1 -sw '${size_download}\n' | grep -o '[0-9]*'
