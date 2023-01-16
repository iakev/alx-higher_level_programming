#!/usr/bin/env bash
# script taking in a URL, sending a request to the URl, and displaying
# size of the body response
curl $1 -sw -w '${size_download}\n' | grep -o '[0-9]*'
