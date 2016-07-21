all: test bench

test:
	python tests.py

bench:
	python benchmarks.py

release:
	python setup.py register sdist upload
