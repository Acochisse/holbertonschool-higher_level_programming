#!/bin/bash
# Script
curl -swL "%{http_code}" "$1" -o /dev/null
