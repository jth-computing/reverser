# Makefile for hello in Python

all:

run:
	python src/reverser.py

test:
	PYTHONPATH=src python tests/test_reverseno.py
