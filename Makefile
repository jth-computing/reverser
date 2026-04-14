# Makefile for hello in Python

all:

run:
	python src/reverser.py

test:
	PYTHONPATH=src python tests/test_reverseno.py

coverage:
	rm -rf .coverage
	PYTHONPATH=src coverage run tests/test_reverseno.py
	PYTHONPATH=src coverage report
