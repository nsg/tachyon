
dev: env deps
	. env/bin/activate \
		&& python app/app.py

deps:
	. env/bin/activate \
		&& pip install -r app/requiremts.txt


virtualenv:
	type virtualenv || ( echo "You need to install virtualenv"; exit 1 )

env: virtualenv
	virtualenv env

.PHONY: virtualenv dev deps
