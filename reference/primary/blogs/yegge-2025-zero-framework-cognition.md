https://steve-yegge.medium.com/zero-framework-cognition-a-way-to-build-resilient-ai-applications-56b090ed3e69?source=rss-c1ec701babb7------2


Zero Framework Cognition: A Way to Build Resilient AI Applications

Steve Yegge

Wed, 22 Oct 2025 04:34:50 GMT

---

In my code, I always want the AI to make decisions. (...) When we reach a decision point, send it back to the model. Don’t try to hack this on the client side with regular expression matching!

(...)

And that’s how we came up with ZFC: Zero Framework Cognition.

(...)

Core Architecture Principle: This application is pure orchestration that delegates ALL reasoning to external AI. We build a “thin, safe, deterministic shell” around AI reasoning with strong guardrails and observability.

