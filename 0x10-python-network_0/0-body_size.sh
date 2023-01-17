#!/bin/bash
# script taking in a URL, sending a request to the URl,displaying size of conte
curl -o -sw '${size_download}\n' $1
