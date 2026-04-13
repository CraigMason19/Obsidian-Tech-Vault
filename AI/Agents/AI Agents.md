#AI 

Automated processes / workflows / chains using AI. `Agentic AI` means as using agents as a workflow. 

Resources
- [5 Types of AI Agents: Autonomous Functions & Real-World Applications](https://www.youtube.com/watch?v=fXizBc03D7E&list=WL&index=56&t=343s&pp=iAQBsAgC)
- [YT - AI Agents Explained](https://www.youtube.com/watch?v=hLJTcVHW8_I&list=WL&index=60)
- [AI Agents in 38 Minutes](https://www.youtube.com/watch?v=sNvuH-iTi4c&list=WL&index=42)

[[#Overview]]
[[#Differences to LLM's]]

---
## Overview

An Agent is a workflow that executes multiple steps to complete a task.

They are a pipeline of transformations to reach an outcome which can be simple or complex interacting with API's, services and [[LLM]]'s

For example, a simple chain may look like this...
- do this -> do this -> do this -> result 

and a more complex one might be...
- goal -> evaluate -> checks criteria -> evaluates until goal is met

How I think of them
- Analogous to flow charts.
- Reminds me of blender nodes. Where you can make shaders without coding by making chains of nodes.

---
## Differences to [[LLM]]'s

**LLM's**
- Passive. Whereas agents can act on their own based upon certain criteria.
- Only has access to training data and not current up to date data. It can now search via the internet but this is not part of the LLM.
- Have no context about you. It's general and not specific.

**Agents**
- Can be given a `knowledge` (The context you give it, what it needs to know).
- Can be given a `memory` (What it has learned in the previous iterations of the task).
- Can access external tools / API's.
- Can operate a dynamic pipeline by choosing which tools to use (if you give it access to tools)
- Can generate a sequence of actions based on the prompt.
- Can be given sub-agents that perform certain roles.
- Can be given heuristics to drive outcomes.
- Can execute actions
- Can be given autonomy to make decisions

---
