NAME=llm
all:
	node ./pbp/das/das2json.mjs $(NAME).drawio
	rm -f out.md
	python main.py . 'is concurrency considered difficult?' main $(NAME).drawio.json | node ./pbp/kernel/splitoutput.js

init:
	npm install yargs prompt-sync ohm-js @xmldom/xmldom
