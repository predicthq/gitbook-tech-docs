---
description: >-
  An AI-native notebook for exploring and building with PredictHQ - available
  inside the PredictHQ WebApp.
---

# Bolt

{% hint style="success" %}
**Bolt is coming soon.** It will be available to all PredictHQ customers shortly. If you have questions in the meantime, contact your PredictHQ account team.
{% endhint %}

Bolt combines a conversational AI interface with a persistent notebook of interactive cards. Ask questions in natural language, and Bolt retrieves real data from PredictHQ's APIs, guides you toward the right products for your situation, and surfaces results as cards you can explore, share, and take directly into your integration.

### What You Can Do

**Explore PredictHQ data through conversation.** Ask about events, demand signals, locations, and forecast inputs in plain language. Bolt queries PredictHQ's APIs on your behalf and returns real results - not synthetic examples.

**Get guided to the right solution.** Bolt understands PredictHQ's products and how they fit together. Rather than returning a generic answer, it steers you toward the right approach for your use case - running a Beam analysis before querying features, using Predicted Impact Area rather than a fixed radius, and following the integration patterns that produce the best outcomes.

**Build with the results.** Every card in the notebook includes a production-ready API code snippet alongside the visualisation and raw data. When you find something useful, the code to reproduce it is already there.

**Work iteratively.** Cards persist across the session and accumulate in the notebook as the conversation progresses. Follow up, refine, and drill down - the notebook becomes an artefact you can revisit and share with your team.

### How It Works

Bolt's interface has two panels that work together.

The **chat panel** is where you type questions and see responses. Bolt can execute multi-step workflows - creating a Saved Location, running a Beam analysis, and returning demand-calibrated features - from a single conversational exchange.

The **notebook panel** is where results appear as cards. Each card has three tabs:

* **Preview** - an interactive chart or map of the results
* **Code** - a production-ready API snippet you can take directly into your integration
* **Data** - the raw API response

Cards are managed by Bolt as the conversation evolves - cards that are no longer relevant are collapsed, while cards you pin stay in view. The notebook is the persistent artefact; the chat is how you drive it.

### PredictHQ Best Practices Built In

Bolt is configured with PredictHQ's integration best practices. It follows the recommended workflow automatically:

* Creates Saved Locations before running Beam analyses
* Uses Predicted Impact Area rather than fixed radii
* Runs Beam to identify which events drive demand at each location before retrieving features
* Uses the Features API for demand signals and the Events API for drill-down and explainability
* Applies industry context to calibrate results

This means Bolt produces better results out of the box than querying the APIs directly without guidance - and helps you understand why each step matters as you work through it.

### Getting Started

Bolt is available inside the [PredictHQ WebApp](https://control.predicthq.com/bolt). Select **Bolt** from the navigation to open the interface.

{% hint style="success" %}
**Bolt is coming soon.** It will be available to all PredictHQ customers shortly. If you have questions in the meantime, contact your PredictHQ account team.
{% endhint %}

Start by describing your use case or location - for example:

* _"What events are impacting demand at my hotel in Chicago next month?"_
* _"Set up a Beam analysis for our restaurant in Sydney"_
* _"Show me demand signals for a retail location in London"_

Bolt will guide you from there.

### Next Steps

* [MCP Server](mcp.md) - connect Bolt's capabilities to your own AI assistant or coding environment
* [Agent Skills](build-with-ai.md#agent-skills) - install PredictHQ best practices into your AI coding agent
* [Integration Guides](../integrations/integration-guides/) - move from exploration to a production integration
