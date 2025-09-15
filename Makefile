default: build

build:
	python3 -m build --wheel

clean:
	rm -rf dist/ build/ *.egg-info

testpub:
	twine upload --repository testpypi --verbose dist/*

pub:
	twine upload dist/*

.PHONY: build clean testpub pub
