#!/bin/bash
# Script
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
