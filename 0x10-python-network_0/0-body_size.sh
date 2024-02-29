#!/usr/bin/env bash
# Get the size of the HTTP response body using cURL
curl -s "$1" | wc -c
