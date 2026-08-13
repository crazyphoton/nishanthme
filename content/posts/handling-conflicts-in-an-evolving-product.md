---
title: 'Handling Conflicts in an Evolving Product'
date: 2026-08-13T00:00:00.000+08:00
draft: false
url: /2026/08/handling-conflicts-in-an-evolving-product.html
---

I asked Fable to connect directly to Linear, review six bug reports, and fix them overnight. I mentioned some of them might already be fixed, so it had to review them before fixing.

It came back saying two were already fixed. It fixed the other four, and I verified them. A good night's work.

The fifth one was interesting. My QA colleague told me that one of the "already fixed" bugs was only partially fixed: there was a specific case where it didn't work.

Some context: we're building a dashboard to manage appointment bookings for a list of services. The bug was that the list of services wasn't loading correctly in some places, and it was now fixed. There was also a setting to make some services available only for repeat customers. For new customers, those services would not be available, even when you were editing their appointment. My QA colleague didn't realize the setting was on, and thought the services list on the edit-appointment screen was buggy because they had tested on a new customer. So the correct resolution here is "cannot reproduce."

What makes this interesting is that Fable knew the rule. It spent the night checking for the issue and verifying it. It created a freshly seeded database, confirmed the dropdown reads the live catalogue and refetches on every open, and traced the one difference between the working screen and the "broken" one to that exact setting. It read the code comment saying the edit-screen behavior was deliberate.

It carved an exception so the edit screen would bypass the gate, wrote tests for the new behavior, opened a PR, and posted a confident root-cause analysis. With the QA saying broken on one side and the spec saying intended on the other, it sided with the human.

The model has no intuition for when a contradiction means a human misunderstood something and when it means the spec is wrong and should change.

What would have been desirable? It depends on the context. In fully autonomous product loops, the correct output is "Won't Fix, inconsistent product spec," which forces the QA to be more precise about what they want and to override the spec explicitly. In a human-augmented loop, perhaps something like: "I created a PR assuming the QA is right, but it conflicts with your spec. It doesn't make sense to show a service you've hidden from new customers just because someone opened the edit screen, so why do you want that?"

When there are conflicting signals, how do you corral the agents in the right direction to build a coherent product? What guardrails would make it hold its ground to increase coherence in the product? I think this is the next big battle with autonomous software engineering.
