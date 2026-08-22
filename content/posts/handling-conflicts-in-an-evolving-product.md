---
title: "Handling Conflicts in an Evolving Product"
date: 2026-08-13T00:00:00.000+08:00
draft: false
url: /2026/08/handling-conflicts-in-an-evolving-product.html
---

An LLM has no intuition for when a contradiction means a human misunderstood something and when it means the spec is wrong and should change.

### The Bug Bash

Last night I pointed Fable at my bugs list and asked it to review and fix everything. I mentioned some of them might already be fixed, so it had to review them before fixing.

It fixed four bugs, and I verified them. A good night's work.

Two bugs were marked "already fixed" and this is where it gets interesting. My teammate told me that one of the "already fixed" bugs was only partially fixed: there was a specific case where it didn't work.

### The Config Confusion

Some context: We're building a dashboard to manage appointment bookings for a list of services. The bug Fable had marked fixed was that the services list wasn't loading correctly in some places.

But there's a separate feature at play. A setting makes some services available only to repeat customers. When it's on, those services don't appear for new customers, including on the screen where you edit a new customer's appointment.

My QA colleague tested the edit-appointment screen on a new customer, saw those services missing, and read it as the loading bug resurfacing. They didn't realize the repeat-customer setting was on.

The services weren't missing because of a bug; they were missing by design.

**So the correct resolution here is "cannot reproduce."**

### The Conflict Conundrum

What makes this interesting is that Fable knew about the config and the feature. It created a freshly seeded database, confirmed the dropdown reads the live catalogue and refetches on every open, and traced the one difference between the working screen and the "broken" one to that exact setting. It read the code comment saying the edit-screen behavior was deliberate.

Then it got confused when the human said there was still a bug. It created an exception so the edit screen would bypass the gate, wrote tests for the new behavior, opened a PR, and posted a confident root-cause analysis. With the QA saying broken on one side and the spec saying intended on the other, it sided with the human.

### What should it have done?

What would have been desirable? It depends on the context.

In fully autonomous product loops, the correct output is _"Won't Fix, inconsistent product spec,"_ which forces the QA to be more precise about what they want and to override the spec explicitly.

In a human-augmented loop, perhaps something like: _"I created a PR assuming the QA is right, but it conflicts with your spec. It doesn't make sense to show a service you've hidden from new customers just because someone opened the edit screen, so why do you want that?"_

When there are conflicting signals, how do you corral the agents in the right direction to build a coherent product? What guardrails would make it hold its ground to increase coherence in the product? I think this is the next big battle with autonomous software engineering.
