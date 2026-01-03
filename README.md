# pbp-llm
Simple example of creating a project using Part Based Programming (PBP).

See video https://programmingsimplicity.substack.com/p/pbp-llm-automated-problem-discovery?r=1egdky.

Cloned code repositories [pbp-kit](https://github.com/guitarvydas/pbp-kit) and [agency (Go code to access OpenAI api)](https://github.com/guitarvydas/agency), but, used their code is directly included in this project, not used as sub-modules. This pbp-llm repo should be completely stand-alone.

# usage
`make init` (one time, to fetch npm dependencies)
## Stubbed Out
`make logic`
## Full
- ensure that environment variable OPENAI_API_KEY is set up (put a few $s ($5.00?) into your account at https://platform.openai.com/api-keys)
`make`
## Logged
`make logged`
saves intermediate rephrasings to `out.0.md`

# Expected Output
## Full
```
$ make
node ./pbp/das/das2json.mjs llm.drawio
Created: llm.drawio.json
rm -f out.md
python main.py . 'is concurrency considered difficult?' main llm.drawio.json | node ./pbp/kernel/splitoutput.js
count=1
count=2
count=3
count=4
count=5
Appended to file: out.md
```

## Stubbed Out
```
$ make logic
node ./pbp/das/das2json.mjs logic.drawio
Created: logic.drawio.json
rm -f out.md
python main.py . 'is concurrency considered difficult?' logic logic.drawio.json | node ./pbp/kernel/splitoutput.js
count=1
"Info" : "  @4  probe logic▹logic▹:?=₇: 1"
"Info" : "  @7  probe logic▹logic▹:?=₃: 2"
"Info" : "  @10  probe logic▹logic▹:?=₁: 3"
count=2
"Info" : "  @12  probe logic▹logic▹:?=₅: 4"
"Info" : "  @15  probe logic▹logic▹:?=₃: 2"
"Info" : "  @18  probe logic▹logic▹:?=₁: 3"
count=3
"Info" : "  @20  probe logic▹logic▹:?=₅: 4"
"Info" : "  @23  probe logic▹logic▹:?=₃: 2"
"Info" : "  @26  probe logic▹logic▹:?=₁: 3"
count=4
"Info" : "  @28  probe logic▹logic▹:?=₅: 4"
"Info" : "  @31  probe logic▹logic▹:?=₃: 2"
"Info" : "  @34  probe logic▹logic▹:?=₁: 3"
count=5
"Info" : "  @36  probe logic▹logic▹:?=₅: 4"
"Info" : "  @38  probe logic▹logic▹:?=₃: 2"
"Info" : "  @39  probe logic▹logic▹:?=₉: 5"
Appended to file: out.md
```

Takes much longer (minutes) due to sending questions to openai.
Open out.md to see results.

## logged
```
$ make logged
node ./pbp/das/das2json.mjs logged.drawio
Created: logged.drawio.json
rm -f out.md out.0.md
python main.py . 'is concurrency considered difficult?' logged logged.drawio.json | node ./pbp/kernel/splitoutput.js
count=1
count=2
count=3
count=4
count=5
Appended to file: out.0.md
Appended to file: out.0.md
Appended to file: out.0.md
Appended to file: out.0.md
Appended to file: out.0.md
Appended to file: out.0.md
Appended to file: out.0.md
Appended to file: out.0.md
Appended to file: out.md
```

Takes a whle (minutes) due to sending questions to openai.
Open out.0.md to see intermediate, rephrased questions.
Open out.md to see results.


# UTF-8
Some of the Part names contain Unicode. 

You may need to enable Unicode before running `make` using this version of PBP.

In Linux/Mac:
`export PYTHONUTF8=1`

In Windows:
`set PYTHONUTF8=1`


# Backgrounder
## PBP-LLM: Automated Problem Discovery Using Language Models

### Technical Motivation

As software consultants and contractors, one of our most challenging tasks is understanding what problem we're actually solving. When you ask a customer to describe their problem, they rarely provide a complete answer on the first try. The initial problem statement is often a symptom rather than the root cause.

Daniel Pink, in his [MasterClass on Sales and Persuasion](https://www.masterclass.com/classes/daniel-pink-teaches-sales-and-persuasion), advocates for iterative questioning—asking "why" approximately five times to drill down from surface symptoms to core issues. This "5 Whys" technique, originally developed by Toyota for manufacturing, proves equally valuable for uncovering the real problems in software development.

## From Manual Analysis to Automated Discovery

I've applied this iterative questioning technique to various software engineering problems in a series of blog posts:

- [5 Whys of Software Components](https://guitarvydas.github.io/2020/12/10/5-Whys-of-Software-Components.html)
- [5 Whys of Multiprocessing](https://guitarvydas.github.io/2020/12/10/5-Whys-of-Multiprocessing.html)
- [5 Whys of Full Preemption](https://guitarvydas.github.io/2020/12/10/5-Whys-of-Full-Preemption.html)

While manually working through these analyses, I recognized an opportunity: could we automate this interrogation process using language models? What if an LLM could help us systematically explore a problem space by continuously rephrasing and deepening our understanding of an issue?

### The PBP-LLM Experiment

This project is a Minimum Viable Implementation (MVI) that demonstrates how Parts Based Programming enables previously impractical solutions. The implementation creates a question-and-rephrase loop that queries OpenAI's API iteratively, stopping after a configured limit (typically five iterations). Each iteration takes the previous response and asks the LLM to rephrase or dig deeper into the underlying issues.

What makes this particularly interesting from a PBP perspective is that it showcases asynchronous, component-based architecture applied to a novel problem domain. The components coordinate the loop, manage API calls, and aggregate insights—all while maintaining loose coupling and clear separation of concerns.

### Insights from LLM-Assisted Analysis

Beyond validating the technical approach, this experiment reveals something valuable about the software development landscape. Large Language Models like OpenAI's GPT are trained on corpus data representing current "best practices" in programming. By analyzing their responses to iterative questioning about software problems, we can:

1. **Identify commonly held beliefs** about programming practices and assumptions
2. **Discover blind spots** in conventional wisdom
3. **Recognize which problems** in the software development workflow remain underexplored or poorly understood
4. **Generate new questions** that challenge established practices

The LLM's answers serve as a mirror reflecting the collective knowledge and biases of the programming community. This makes pbp-llm not just a problem-solving tool, but a meta-tool for understanding which problems we should be solving.

### Next Steps

This MVI demonstrates that the core loop works as designed. However, it also suggests numerous improvements and new directions: different questioning strategies, alternative problem domains to explore, and ways to better capture and analyze the insights that emerge from this iterative process. The Parts Based Programming approach makes such experimentation straightforward—we can swap components, adjust the flow, and explore variations without rewriting the entire system.

![API](./api.md)
