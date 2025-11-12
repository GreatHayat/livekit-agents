# 🚀 Exploring LiveKit Agents

This repository documents my learning journey with **LiveKit Agents** — exploring how voice and AI workflows come together.
So far, I’ve explored:

* `Agent`
* `AgentSession`
* `Plugins`
* `Workflows`
* `Function Calling`
* `Passing & Saving Data to State`

I’ll continue pushing my experiments and progress here as I go deeper into the LiveKit ecosystem.


## 🧩 Getting Started

Follow these steps to set up and run the project locally.

### 1️⃣ Prerequisites

* Make sure you have **LiveKit CLI** installed:

```bash
brew install livekit-cli
```

* Authenticate with your LiveKit Cloud account:

```bash
lk cloud auth
```

> You must have a **LiveKit Cloud account**. Refer to the [LiveKit Docs](https://docs.livekit.io/agents/start/voice-ai/) for instructions specific to your OS.

---

### 2️⃣ Clone the Repository

```bash
git clone git@github.com:GreatHayat/livekit-agents.git
cd livekit-agents
```

### 3️⃣ Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 5️⃣ Download Required Files

```bash
python3 agent.py download-files
```

### 6️⃣ Run the Agent

* **Console Mode**

```bash
python3 agent.py console
```

* **Dev/Playground Mode**

```bash
python3 agent.py dev
```

Connect to: 👉 [LiveKit Agents Playground](https://agents-playground.livekit.io/)

---

## 📚 Reference

Official Docs: [LiveKit Voice AI Quick Start](https://docs.livekit.io/agents/start/voice-ai/)
