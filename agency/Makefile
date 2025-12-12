all:
	go build examples/cli/main.go

clean:
	rm -f main

test:
	./main -model gpt-4o-mini -maxTokens 1000 -temp=1 -prompt "concise responses" "is concurrency considered difficult?"
