#!/bin/bash
# Script
curl -sI "$1" | Content-Length | cut -d " " -f 2
