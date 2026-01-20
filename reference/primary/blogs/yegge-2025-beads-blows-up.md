https://steve-yegge.medium.com/beads-blows-up-a0a61bb889b4?source=rss-c1ec701babb7------2


Beads Blows Up

Steve Yegge

Thu, 06 Nov 2025 09:58:17 GMT

---

In the past week, I’ve had so many people telling me they’re using Beads and that they love it. (...) So from that incredibly rigorous statistical sample, fully 3% of the world’s developers are using Beads!

(...)

The good news is, 3 weeks in, Beads is shaping up to be the Right Thing. It works well for the 2025 coding agent form factor (...) any other agentic coding assistant.

All of them use markdown files for their TODOs and planning. (...) Beads uses lightweight, git-backed issue tracking instead of markdown files.

(...)

In particular, we use Git and JSONL (one line per issue), with a SQLite database, acting as a fast queryable cache layer, which hydrates on demand from the JSONL. (...) Beads feels like there is a central managed server, but there isn’t one. It’s just Git with some hooks and auto-syncing logic.

