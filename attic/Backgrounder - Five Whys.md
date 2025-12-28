This is a backgrounder that I want to include in README.md of the `pbp-llm` project to explain what this experimental MVI can achieve and how it might suggest new approaches to problems in our software workflow.

Please rephrase and reword this backgrounder to make it easier to understand the technical motivation of the PBP (Parts Based Programming) code. The result should be in markdown format, about several paragraphs long, or about 1/2 to 1 page of text long, targeted at practicing programmers who want to learn how to use PBP and to see how previously unthinkable problems can be solved with PBP.

As a software consultant or contractor, you need to figure out what the customer's problem is.

If you ask the customer, you find that the customer usually can't fully verbalize the problem and tends to give an insufficient answer to the question.

Daniel Pink, in his Masterclass [ed. give a reference or pointer to the masterclass.com in which Pink is featured], promotes the idea of re-phrasing the customer's answer about 5 times, to drill down and discover what the core of the problem is.

I brainstormed with this technique a few times in several blog articles:
- https://guitarvydas.github.io/2020/12/10/5-Whys-of-Software-Components.html
- https://guitarvydas.github.io/2020/12/10/5-Whys-of-Multiprocessing.html
- https://guitarvydas.github.io/2020/12/10/5-Whys-of-Full-Preemption.html

I realized that it would be nice to have a machine help with 5 whys analysis of various problems. I mocked up a simple question / re-phrase loop that accesses OpenAI's API in a loop that stops the process after some limit has been reached, i.e. it loops 5 times.

This project - pbp-lmm - is an MVI (Minimum Viable Implementation) brainstorming experiment to see how such a loop would work. We can see that the loop works as expected, but, I already have ideas on what I might want to improve and what other questions I would want to feed into the hopper.

The OpenAI LLM is trained on "best practices" in programming. Studying it's answers reveals commonly held beliefs about programming and can suggest which problems need to be solved for improving the software development workflow.
