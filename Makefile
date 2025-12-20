NAME=llm
all:
	node ./pbp/das/das2json.mjs $(NAME).drawio
	rm -f out.md
	python main.py . 'is concurrency considered difficult?' main $(NAME).drawio.json | node ./pbp/kernel/splitoutput.js

logic:
	node ./pbp/das/das2json.mjs logic.drawio
	rm -f out.md
	python main.py . 'is concurrency considered difficult?' logic logic.drawio.json | node ./pbp/kernel/splitoutput.js

logged:
	node ./pbp/das/das2json.mjs logged.drawio
	rm -f out.md out.0.md
	python main.py . 'is concurrency considered difficult?' logged logged.drawio.json | node ./pbp/kernel/splitoutput.js

init:
	npm install yargs prompt-sync ohm-js @xmldom/xmldom
