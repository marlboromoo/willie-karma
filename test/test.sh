#!/bin/sh
cd $(dirname $0)
PYTHONPATH=../ python -m pytest test.py
