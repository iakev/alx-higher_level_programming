#!/bin/bash
# scrpt to list allowed methods server will accept
curl -sI $1 | grep "Allow" | cut -d " " -f 2-
