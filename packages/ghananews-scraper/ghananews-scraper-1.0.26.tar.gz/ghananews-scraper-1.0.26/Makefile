release:
	rm -rf build dist
	python setup.py sdist bdist_wheel
	twine upload dist/*

lint:
	pylint --recursive=y ghanaweb myjoyonline yen graphiconline citionline threenews

install:
	pip install -e .

format:
	black *.py

sort:
	isort *.py