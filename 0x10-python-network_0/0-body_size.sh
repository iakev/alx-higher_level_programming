#!/bin/bash
# script taking in a URL, sending a request to the URl,displaying size of conte
curl -s $1 | wc -c
