https://steve-yegge.medium.com/six-new-tips-for-better-coding-with-agents-d4e9c86e42a9?source=rss-c1ec701babb7------2


Six New Tips for Better Coding With Agents

Steve Yegge

Sun, 07 Dec 2025 06:02:14 GMT

---

1. Software is now throwaway — expect

(...)

We are entering a surprising new phase of software development, in which rewriting things is often easier (and smarter) than trying to fix them.

I first noticed this with unit tests. (...) So one day I said, screw it, delete all the tests and make me new ones. And it got through that exercise SO much faster. The new tests were great, had great coverage, and importantly, the LLM was able to generate them very quickly, compared to trying to reason through the old system behavior vs the new expected behavior.

This generalizes beyond tests: generating almost any code is easier (for AIs) than rewriting it. Hence, recreating software stacks from scratch is starting to become the new normal.

The upshot is that for all the code I write, I now expect to throw it away in about a year, to be replaced by something better. (...) It’s all just stepping-stones to higher velocity.

This spells trouble for third-party SaaS vendors. Companies are also discovering that they can build bespoke business-automation software so easily that they don’t need to re-up their vendor contracts.

