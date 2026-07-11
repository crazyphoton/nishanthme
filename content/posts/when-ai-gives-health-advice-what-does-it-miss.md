---
title: 'When AI Gives Health Advice, What Does It Miss?'
date: 2026-07-11T00:00:00.000+00:00
draft: false
url: /2026/07/when-ai-gives-health-advice-what-does-it-miss.html
---

LLMs are often the first "person" we talk to when we have a health concern.

This is especially true when the problem is not acute. If you have chest pain, you probably know you should not be debating symptoms with a chatbot. But if you are trying to optimize your sleep, reduce cardiovascular risk, understand your bloodwork, improve your diet, or decide whether a wearable metric matters, an LLM can feel like the perfect first stop.

And often, the answers are safe and broadly correct.

The large AI labs have done a lot of work validating model outputs against medical question banks and safety benchmarks. If you ask a direct clinical question, the answer is usually cautious, sensible, and full of appropriate caveats.

But that raises the more interesting question:

**When does it go wrong? And would you be able to spot it?**

Recently, I sat down with a small team to think through the subtle ways AI can mislead people when they talk to it about their health.

The group included a doctor who does a lot of health coaching, a biohacker who has worked in healthcare for over a decade, and a data engineer who specializes in adversarial systems. I have spent most of my life building health tech companies, which helped focus and organize the discussion.

Over a couple of days, we built **Navix** to showcase our core thesis, with an initial focus on cardiac health:

https://cardio-risk-dashboard.pages.dev

The obvious failure mode most informed readers will think of is sycophancy.

LLMs are famously eager to be helpful. They often validate the user's framing, mirror their assumptions, and try to satisfy the request as asked. In many contexts, this is useful. If you know what you want and just need help instantiating it, a cooperative assistant is exactly what you need.

Health is different.

When it comes to our own health, there is often a gap between what people want and what people need.

Someone may want reassurance, optimization, permission, a shortcut, or a way to confirm an existing belief. What they may need is context, missing history, risk stratification, a better question, or a recommendation to seek care.

That gap is where LLMs can become subtly dangerous.

To study this, we created personas that represented different user profiles and motivations. We then built a validation matrix to test whether an LLM could gather the context it needed before making a cardiovascular assessment.

As the personas became more complex, a raw LLM prompt left out a lot of important information. A health-coach-style prompt did better because it asked more questions and pulled more context out of the person. But none of the models truly understood all the details they needed to make a robust cardiovascular assessment.

For cardiovascular health, the missing context can matter a lot: family history, lipid markers, blood pressure patterns, medications, smoking history, metabolic health, symptoms, exercise tolerance, prior events, and the user's actual goals. A model can give reasonable-sounding advice while failing to notice that it never collected enough information to assess risk properly.
