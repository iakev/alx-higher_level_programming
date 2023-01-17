#!/bin/bash
# scrpt to list allowed methods server will accept
curl -sX OPTIONS $1
