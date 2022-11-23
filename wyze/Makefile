
all: init run

init:
	echo ${WYZE_EMAIL}
	echo ${WYZE_PASSWORD}
	brew install python@3.10
	python3.10 -m pip install --upgrade pip
	python3.10 -m pip install -r requirements.txt

run: 
	python3.10 scripts/main.py

	