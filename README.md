# vinbudin-watcher

Simple script for monitoring product stock numbers on vinbudin.is

## Setup and usage

You need to install [python 2.7 and pip](http://docs.python-guide.org/en/latest/starting/install/win/) and install the following python modules:

	pip install -r pip_requirements.txt

Open a terminal in this repository and run

	python worker.py

This writes data to files in the `products` directory.
