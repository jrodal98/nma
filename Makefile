build:
	python3 setup.py sdist bdist_wheel
upload:
	twine upload dist/* 
install:
	pip install --user nma
