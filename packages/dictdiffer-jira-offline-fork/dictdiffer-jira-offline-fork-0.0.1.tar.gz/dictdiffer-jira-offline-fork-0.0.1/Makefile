PACKAGE_NAME=dictdiffer
TEST?=0


.PHONY: clean
clean:
	rm -rf build dist

.PHONY: package
package: clean
	python3 -m pip install --upgrade setuptools wheel
	rm -rf $(PACKAGE_NAME).egg-info dist
	python3 setup.py sdist bdist_wheel

.PHONY: publish-pypi
publish-pypi:
	docker build -f Dockerfile.twine -t mafrosis/twine .
	docker run --rm -v $$(pwd)/dist:/dist:ro \
		mafrosis/twine \
		check -r testpypi /dist/*
	docker run --rm -v $$(pwd)/dist:/dist:ro \
		-e TWINE_USERNAME -e TWINE_PASSWORD \
		mafrosis/twine \
		upload -r testpypi /dist/*
