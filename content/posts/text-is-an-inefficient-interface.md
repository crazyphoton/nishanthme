---
title: 'Text is an Inefficient Interface'
date: 2026-08-05T00:00:00.000+08:00
draft: false
url: /2026/08/text-is-an-inefficient-interface.html
---

<div style="text-align: center;">

![Four turtles stacked tallest to smallest with a glitchy dashboard on top; beside them, info bubbles shrink at each layer as bits of data fall away](/img/text-is-an-inefficient-interface.svg)

</div>

Automated Value Generation is a process of humans communicating context to the AI. You provide context and constraints the LLM can't get by itself, and if you do it well, throw in enough tokens and some prayers, out comes value! Or that's the hope.

But humans are not very good at sending context to AI. We're impatient, so we send half-baked instructions and expect the model to fill in the gaps. Sometimes it does a good job; sometimes it totally misses the point.

There's a little dance these days where the newer models ask you a few questions to anchor the response, but that's about it. Too many questions and we get impatient, so the model spits out a large, complicated summary of the decisions it made on our behalf.

But why words at all? The savvier among us have switched to talking to the AI. Speech is higher-density, but that's still ultimately constrained by words. Text is an inefficient interface to begin with, and it's made worse by the fact that AI is notoriously bad at communicating with words; honestly, if you delve into it (heh), it's gotten worse.

There are better ways.

## The spec that ate itself

I've been trying spec-driven development: using LLMs to write a detailed spec and understand the boundaries of a system before building it. The spec itself grew, and within a couple of hours we had fifty pages. I built sidebars and sections for easier navigation, but describing changes ("the third paragraph under the section about X, change the framing") was getting annoying.

But code is free! We can build custom interfaces for communicating with the AI.

What worked: pulling the spec up in a browser, highlighting text, commenting inline. The comments fed into a task system the agent was watching, so it picked them up and worked while I kept reviewing. Highlight, comment, move on.

That's when it clicked: text is a flexible interface, but it is a very inefficient one.

## Disposable interfaces

Since then I've built a Kanban board with custom fields for one specific project. The agent posts tasks and progress, I drop comments, and instead of scrolling a chat log I'm looking at a living picture of the work. Sometimes I maintain dashboards, a chart, an annotated document, even throw away interfaces that explain a spec. The right interface depends on what you're optimizing for and what you need clarity on right now. It doesn't have to be visual, either: a friend of mine has the AI read him a voice summary, generated with a different prompt from the text summary it writes out.

The unlock is that these are cheap now. AI makes it easy to spin up a review dashboard on the fly. So you build one for this project, maybe just this session, use it, and throw it away. It doesn't need to be a product. It needs to exist for an afternoon.

## Custom tools for custom work

You don't want to know everything the AI could tell you. You want the important bits, transformed into something indicative, in the form that lets you make the next decision, and you want an interface that communicates that decision back as efficiently as possible.

Chat is general-purpose, and general-purpose is precisely wrong when the whole problem is *what should I be paying attention to?*

Why not build an entire app for it?

## Practical implementation for beginners

This is most useful for heavy, long-running tasks where you expect many iterations with the AI.

1. **Think about the best interface for telling the AI what to do.** Claude.md isn't your only tool. You can comment on top of your own website and throw the feature away later. You can generate density maps of the text you're writing, or word clouds. Ask yourself: what would tell me the AI is off track, and how do I want that communicated?
2. **Ask Claude to build it**, as a website, or on top of your existing interface. It has to take inputs from you and write them to a todo list.
3. **Start a loop** that reads off the todo list and implements items using background workers.

## Turtles all the way

We are creating layers upon layers of interpretation here, and there is a loss with each translation. Interfaces drift: your agent might not remember to update the dashboard, so it needs regular pruning to stay true to the task at hand. Remember not to get too attached to your todo list. Throw it away when it's no longer useful!
