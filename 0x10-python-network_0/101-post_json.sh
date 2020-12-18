#!/bin/bash
# Script
curl -sX POST -h "Content_Type: application/json" -d @"$2" "$1"
