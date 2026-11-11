+++
title = 'What Does an LLM Find Interesting?'
date = 2026-11-11T12:00:00+08:00
draft = false
+++

{{< figure src="/img/what-does-an-llm-find-interesting-wisps-vs-robot.png" width="1536" height="1024" alt="A thoughtful man with a cloud of faint, half-formed ideas drifting above his head—a castle, a sailboat, mountains—while a cheerful robot holds up its own neat, finished framed picture of a resolved landscape" class="tc" >}}

Why do I choose something to write on? How much do I know before I write? How do I figure out what I want to say?

This post started out as a feeling that there was something in a Terence Tao video that tied back to some other ideas I had been thinking about. (That feeling has since been relegated to a different post, because I chose to go meta on this one.) I didn't know what the link was, I just felt a connection. I could name some of the connections, but I realised later that there were also subconscious connections with other ideas I explored a while back.

They were wisps of an idea, wisps that I did not fully understand. In order to actually communicate the wisps (to a human or an LLM) I had to serialise them into text. I had to follow the feeling and do some "tool calling" to crystallise the idea to something I could explain in words. Sometimes, nothing worth talking about materialized (which is not to say there was nothing worth talking about just that I failed to find it). Sometimes an exploration that yielded nothing strengthened an earlier idea. LLMs can help with this serialisation by giving you options to choose from based on vague snippets but without a full exploration of the ideas they don't have a full picture of what you actually found interesting!

Writing is as much a process of figuring out what I care about as it is about communicating what I care about.

Could an LLM go through this process of picking a thread and crafting an interesting story by itself? What does an LLM find interesting? And if it wrote about an interesting thing, would I care?

I asked Claude: "tell me about a connection you find interesting" and it gave me an interesting blurb about how diffusion models apply in different contexts and how image generation models run the diffusion in reverse.

{{< details summary="Claude's answer" >}}
The same equation describes how heat spreads through a metal bar, how stock options get priced, and how modern AI image generators work.

Heat. In 1822, Joseph Fourier wrote down the heat equation. It describes how a hot spot spreads out and flattens over time. Each point drifts toward the average of its neighbors.

Finance. In 1900, five years before Einstein's paper on Brownian motion, a French student named Louis Bachelier modeled stock prices as a random walk. Decades later, the Black–Scholes equation for pricing options turned out to be the heat equation with a change of variables. The "heat" is uncertainty about the price, and it spreads out as time passes.

Image generation. Diffusion models, the kind behind many image generators, start with a real image and add a little random noise at each step until only static remains. That forward process is literally diffusion, the same flattening Fourier described. The model learns to run the process backward. It starts from static and removes the noise step by step until an image comes out.

What I find interesting is the direction of travel. For two centuries, people used this math to predict how order dissolves into noise: heat evens out, prices blur, ink spreads in water. Diffusion models flip it around and use the same physics to build structure out of noise. To run diffusion in reverse, you have to know at every step which way leads toward something real. That's what the model learns.

There's also a more general point here. Nature seems to reuse a small set of patterns, so once you understand one of them deeply, you often find you understand several fields you never studied.
{{< /details >}}

The write up was not far from my interests, I could have been reading about diffusion models, come up with this insight and found it interesting. But it is not my idea at this point in time.

LLMs communicate well when the idea originates with them. What they seem to be bad at is crystallising my half-formed thoughts and communicating it back to me. [In my previous post]({{< relref "ai-slop-is-a-human-problem.md" >}}), I said that the gap was missing context. Which is true, but I also argued that I gave it enough context through bullet points. I don't think I did. As I realise now, I am building the context as I write. Not just in terms of what someone like me will find interesting, but also in terms of what I myself find interesting.
