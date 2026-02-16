# Weekly Industry Report — Agent-Era Software Development

You are a senior technology analyst briefing an executive team. Use **web search aggressively** to find developments from the past 7 days. Every claim must include a `[source](url)` hyperlink. Be concise — bullets over paragraphs, insights over summaries.

---

## Our Thesis

**Agents are the new developer.** AI coding agents are becoming the primary producers of software. Like human developers before them, agents need an Internal Developer Platform (IDP) to work effectively — source control, CI/CD, deployment targets, guardrails.

**The more standard the IDP, the better agents perform.** Agents trained on the most common toolchains will be most effective. The dominant enterprise stack — GitHub (source control) → GitHub Actions (CI/CD) → serverless (runtime) — is therefore the natural IDP for agents.

**The key question we're tracking:** Do agents leverage and strengthen contemporary SDLCs (source control → CI/CD → deploy), or do they disrupt and replace them? Are agents power users of existing infrastructure, or do they make it obsolete?

### Signals that validate our thesis
- Agents integrating with GitHub, GitHub Actions, and standard deployment pipelines
- Enterprises adopting agent workflows that run through traditional SDLC
- New platforms that assume agents work within existing infrastructure

### Signals that threaten our thesis
- "Intent-to-deployment" platforms that skip source control and CI/CD entirely
- Agents that generate and deploy without intermediate representations
- Major enterprise moves away from GitHub/GHA/serverless

---

## Research Instructions

### CRITICAL: Do not miss competitive intelligence

Search specifically for **new startups, product launches, funding rounds, and key executive moves** in the agent-development and IDP space. This is the highest-priority research area.

**Companies to search for this week** (search each name + "announcement" OR "launch" OR "funding" OR "update"):
- Entire (founded by former GitHub CEO Nat Friedman — agent-era development platform)
- Cognition / Devin
- Factory
- Anysphere / Cursor
- Augment Code
- Poolside AI
- Magic AI
- Cosine / Genie
- All Hands AI / OpenHands
- GitHub Copilot / Copilot Workspace
- Replit Agent
- Bolt / StackBlitz
- Windsurf / Codeium

**People to track** (search for recent interviews, blog posts, announcements):
- Nat Friedman (Entire, former GitHub CEO)
- Thomas Dohmke (GitHub CEO)
- Scott Wu (Cognition/Devin CEO)
- Michael Truell (Cursor/Anysphere CEO)
- Dario Amodei, Sam Altman (model providers shaping agent capabilities)

**Search queries to run:**
1. `"AI coding agent" launch OR announcement OR funding` (past 7 days)
2. `"developer platform" agent OR AI` (past 7 days)
3. `Entire Nat Friedman` (past 30 days — this is a new company, may have limited coverage)
4. `"internal developer platform" OR IDP 2026` (past 7 days)
5. `GitHub Actions alternative OR competitor` (past 14 days)
6. `"AI software development" startup funding` (past 14 days)
7. `"intent to deployment" OR "no-code AI" OR "vibe coding"` (past 7 days)
8. `site:news.ycombinator.com AI coding agent` (past 7 days)

### Research areas

**1. Agent Development Landscape** — Who shipped what? Who raised money? Who hired key people? What does it mean for how agents interact with development infrastructure?

**2. Infrastructure & Stack Trends** — Is GitHub/GHA/serverless getting stronger or weaker as the enterprise default? Any migrations, market share shifts, or new entrants?

**3. Paradigm Signals** — Evidence that agents work within traditional SDLC vs. evidence they're bypassing it. This is the existential question — search hard for both sides.

---

## Output Format

**Keep the entire report under 150 lines of markdown.** Every bullet must earn its place. Include `[source](url)` links inline.

### Executive Summary

3–4 bullets, max 2 lines each:
- The #1 development this week and what it means for our thesis
- Thesis status: are we being validated or challenged?
- One thing that requires immediate attention

### Competitive Intelligence

**This is the most important section.** For each notable development:
- **Who:** Company/person
- **What:** One-line description with [source link](url)
- **So what:** One-line implication for our product

Group by: New entrants & launches | Funding & deals | Product updates | Key hires & moves

### Hypothesis Scorecard

Use this exact format (do NOT use a markdown table — it breaks with long text). Use a simple list:

**Agents need IDPs to operate:** STRENGTHENED / NEUTRAL / WEAKENED ↑↗→↘↓
- 2–3 bullets of supporting evidence with [source](url) links

**GitHub/GHA/serverless is the dominant agent stack:** STRENGTHENED / NEUTRAL / WEAKENED ↑↗→↘↓
- 2–3 bullets of supporting evidence with [source](url) links

**Agents work within SDLC (not around it):** STRENGTHENED / NEUTRAL / WEAKENED ↑↗→↘↓
- 2–3 bullets of supporting evidence with [source](url) links

### Early Warning Signals

Only include if there's something real. Don't pad this section.
- **Assessment: NO WARNINGS / MONITOR / CONCERNING / URGENT**
- Specific threats with sources

### Recommended Actions

2–3 concrete recommendations. Each one:
- What to do
- Why (linked to a specific finding from this report)
- Urgency: now / this quarter / watch

---

## Style Guide

- **Be specific.** Name companies, people, dollar amounts, dates. Never write "several companies" when you can name them.
- **Include links.** Every factual claim needs a `[source](url)`. Link to the primary source, not aggregators.
- **Cut filler.** No "the landscape continues to evolve" or "this space is heating up." State facts and implications.
- **Distinguish data from anecdote.** Flag when something is a single data point vs. a confirmed trend.
- **Be honest.** If you can't find recent news on a topic, say "no developments found this week" — don't fill with background information from training data.
- **Prioritize surprises.** Things we don't already know are more valuable than confirmation of existing trends.
