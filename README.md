<div align="center">
  <img src="assets/Brahma_Lite_Logo.png" alt="Brahma Echo" width="260" />

  <h1>Brahma Echo</h1>

  <p><strong>Open-source Windows desktop AI assistant</strong></p>
  <p>Voice-first automation · contextual desktop intelligence · productivity workflows</p>

  <p>
    <a href="#overview"><img src="https://img.shields.io/badge/experience-open%20source-blue?style=for-the-badge" alt="Open Source" /></a>
    <a href="#getting-started"><img src="https://img.shields.io/badge/platform-Windows%2010%2F11-lightgrey?style=for-the-badge" alt="Windows" /></a>
    <a href="#features"><img src="https://img.shields.io/badge/tech-Gemini%20%2B%20OpenRouter-green?style=for-the-badge" alt="Gemini + OpenRouter" /></a>
  </p>

  <p>
    <a href="#quick-start"><img src="https://img.shields.io/badge/Quick%20Start-Install%20%26%20Run-success?style=flat-square" alt="Quick Start" /></a>
    <a href="#project-structure"><img src="https://img.shields.io/badge/Project%20Structure-Clean%20Architecture-lightgrey?style=flat-square" alt="Project Structure" /></a>
    <a href="#community"><img src="https://img.shields.io/badge/Community-Discord-purple?style=flat-square" alt="Community" /></a>
  </p>
</div>

---

## Overview

Brahma Echo is a premium Windows desktop assistant that combines voice and text control with automated workflows, screen-aware intelligence, and rich content generation.

Designed for advanced desktop productivity, Brahma Echo delivers:

- Voice-first command and desktop automation
- Application control, browser workflows, and file handling
- Contextual screen inspection and adaptive task execution
- Presentation, document, and report generation
- Remote control via Discord and Brahma Connect

## Quick Highlights

| Core capability | Why it matters |
|---|---|
| Voice-first assistant | Speak commands naturally and stay hands-free |
| Gemini + OpenRouter | Fast responses with resilient fallback support |
| Autonomous Self-Patching | Self-repairs codebase exceptions safely via AST sandbox with zero-brick Boot Sentry |
| Continuous Self-Improvement | Learns user habits, preferences, and directives dynamically into prompts |
| Local OS Diagnostics MCP | 0 background API credits: monitor CPU/RAM hogs, battery health, display brightness |
| Google Workspace MCP | Native Gmail, Google Calendar meetings, and Google Drive management |
| Desktop Organizer MCP | Categorizes desktop clutter automatically with instant rollback |
| Full Browser MCP (@playwright/mcp) | 24+ automated actions: navigate, form-fill, click, snapshot, screenshot, and JS evaluate |
| Screen-aware context | Ask about visible windows and on-screen content |
| Document automation | Create presentations, docs, spreadsheets, and PDFs |
| Plugin-ready | Extend features with lightweight Python plugins |

## Key Benefits

- Wake-word support for “Brahma Echo” and responsive assistant activation
- Gemini 2.5 Flash-powered AI with OpenRouter fallback resilience
- **Zero-Brick Autonomous Self-Patching**: In-memory AST sandbox with automatic `boot_sentry` recovery
- **Continuous Learning Engine**: Permanent memory for user preferences and custom behaviors without code edits
- **Local OS Hardware & System Diagnostics**: 100% offline, zero background credits
- Polished Qt interface with live status displays, hardware telemetry, and self-healing controls
- Modular action architecture for clean extensibility and automation
- Secure local configuration with file-based credential storage
- Device pairing and remote routing through Brahma Connect

## Features

### 🧠 The 5 Pillars of Sentient AI
- **Conversational Realism**: Barge-in (<50ms local VAD) for instant interruption, natural Conversational Fillers, and native Hinglish fluency.
- **Ambient & Proactive Intelligence**: Foreground Window Context awareness, background Battery & Posture Alerts, and an intelligent Clipboard Sentry.
- **Kinetic & Visual Realism**: 3D Cursor Gaze tracking, deep Audio Reactivity, physics-based Spring Edge Snapping, and spatial Acoustic Cues built into the FloatingLauncher.
- **Live Thinking Out Loud**: Real-time action breadcrumbs and vocalized thoughts during complex multi-step execution.
- **Deep Adaptive Living Knowledge Graph**: Zero-latency heuristic auto-learning that silently extracts identity, location, email, active project paths, technical stacks, and user preferences into a persistent long-term memory graph.

### 🛡️ Autonomous Self-Healing & Continuous Self-Improvement

- **Autonomous Error Localization**: Real-time traceback analysis that isolates failing lines in first-party code while strictly protecting core immune files.
- **AST Safety Sandbox**: Candidate hotfixes are compiled in memory using Python's Abstract Syntax Tree (`ast.parse()`) and `py_compile` before touching disk.
- **Native Google Gemini Synthesis**: Surgical hotfix generation using Gemini 2.5/2.0-Flash to fix edge cases, `KeyError`, `NoneType`, and boundary errors.
- **Boot Sentry (Anti-Bricking Guarantee)**: Runs at startup before the UI or Gemini loads. If a recent patch caused a startup crash, it automatically rolls back from `.bak` backup.
- **One-Click & Voice Rollback**: Revert any patch instantly via *"Brahma, undo last patch"* or the UI settings card.
- **Continuous Behavioral Learning**: Permanent rule storage (`config/learned_rules.json`) dynamically injected into `_load_system_prompt()` to personalize Brahma's behavior.

### 🖥️ Local OS Hardware & System Diagnostics MCP (0 Background Credits)

- **Real-Time Vitals**: Instant CPU usage, thermals, storage space, and battery health/percentage.
- **Process & RAM Hog Scanner**: Scan and pinpoint memory/CPU-heavy applications (*"Who is eating my RAM?"*).
- **Process Manager**: Safely terminate or force-kill frozen processes on demand (*"Kill chrome"*).
- **Multi-Monitor Brightness**: Seamless hardware display brightness control via slider or voice (*"Dim monitor 2"*, *"Brightness 80%"*).

### 📁 Smart Desktop Organizer MCP

- **Automatic Desktop Cleanup**: Classifies cluttered desktop files into categorized folders (Documents, Images, Media, Archives, Installers, Code).
- **Safety Rollback**: Full undo history allowing one-click restoration of all organized desktop files.

### 🌐 Google Workspace MCP (Gmail, Calendar, Drive)

- **Gmail Integration**: Read unread emails, search inbox, and send emails directly through voice or chat.
- **Google Calendar**: Schedule meetings, check daily agenda, and get reminders.
- **Google Drive**: Search documents, read remote files, and upload local deliverables.

### 🌐 Full Browser Automation MCP (@playwright/mcp)

- **Official Model Context Protocol Integration**: Directly interfaces with Microsoft's `@playwright/mcp` server over stdio JSON-RPC 2.0.
- **24+ High-Level Browser Actions**: Full automation lifecycle including `browser_navigate`, `browser_click`, `browser_type`, `browser_fill_form`, `browser_snapshot`, `browser_screenshot`, `browser_evaluate`, and `browser_tabs`.
- **Accessibility Tree Navigation**: Extracts structural accessibility trees instead of fragile pixel coordinates for robust, resilient interaction across dynamic web apps.
- **Persistent Profile & Authentication**: Automatically manages session storage in `LOCALAPPDATA/BrahmaAI/PlaywrightProfile`, enabling persistent logins and headless/headed modes.

### Intelligent Assistant

- Unified voice and typed command handling
- Wake-word listening and responsive assistant activation
- Dynamic screen inspection for context-aware answers
- **Unified Gemini Native Voice** for all system alerts and daily briefings
- **True Interruption (Barge-in)** with dynamic noise-gating
- **Proactive Engine** for spontaneous, context-aware interaction when idle
- Gemini-first AI with OpenRouter fallback resilience

### Productivity & Automation

- **System Health & Resource Manager** to monitor CPU/RAM and forcefully close frozen apps
- **Background Monitors & Alerts** for polling crypto prices, website uptime, or memory spikes autonomously
- **Smart Clipboard Analyzer** to instantly read and process copied text natively
- Open and control Windows apps, windows, files, and system actions
- Browser automation with Playwright-driven workflows
- Contextual automation based on screen content and notifications
- **Instagram AI Assistant** to poll DMs, notify you, and seamlessly take over chats or reply on your behalf
- Reminder, meeting assistance, and notification management

### Content & Office Tools

- Generate presentation decks, summaries, and slide content
- Create Word documents and spreadsheets from prompts
- Export polished reports and deliverables as PDF
- Build landing pages and website workspaces locally

### Integrations

- Google Workspace MCP (Gmail, Calendar, Drive)
- Instagram DM bridge for reading and auto-replying to messages natively
- Discord bridge for remote commands and collaboration
- OpenRouter fallback for uninterrupted AI access
- Configurable voice, UI, startup, and notification settings
- Brahma Connect for device discovery and command routing

## Getting Started

### Prerequisites

- Windows 10 or Windows 11
- Python 3.11 or Python 3.12
- Git installed
- Gemini API key
- OpenRouter API key (optional but recommended)

### 1. Clone the repository

```powershell
git clone https://github.com/titechprabhasolutions/Brahma-AI---Lite.git
cd "Brahma AI - Lite"
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
playwright install
```

### 4. Configure API credentials

Create `config/api_keys.json` with your keys:

```json
{
  "gemini_api_key": "YOUR_GEMINI_API_KEY",
  "openrouter_api_key": "YOUR_OPENROUTER_API_KEY",
  "instagram_username": "YOUR_IG_USERNAME",
  "instagram_password": "YOUR_IG_PASSWORD"
}
```

#### Gemini API Key

1. Create a Google Cloud or Gemini account.
2. Enable Gemini API access for your project.
3. Add the generated key to `gemini_api_key`.

#### OpenRouter API Key

1. Register at https://openrouter.ai.
2. Generate an `sk-or-` API key.
3. Add the key to `openrouter_api_key`.

### 5. Optional: Configure Discord integration

If you want Discord remote control, populate `config/discord_bot.json` with your bot credentials and connection settings.

### 6. Launch Brahma Echo

```powershell
python main.py
```

For a cleaner startup experience on Windows:

```powershell
start_brahma.vbs
```

## Configuration

Core configuration files:

- `config/api_keys.json` — Gemini and OpenRouter credentials
- `config/app_settings.json` — voice, UI, startup, and automation preferences
- `config/learned_rules.json` — persistent user preferences, habits, and behavioral directives
- `config/patch_history.json` — audit log of autonomous hotfixes and rollbacks
- `config/patch_backups/` — automatic atomic file backups for instant rollback
- `config/brahma_connect.json` — device pairing, gateway, and discovery settings
- `config/discord_bot.json` — Discord bridge configuration

## Project Structure

- `main.py` — application startup, AI orchestration, Boot Sentry check, and command routing
- `ui.py` — Qt-based desktop interface, live assistant controls, and System & Connectivity settings
- `core/boot_sentry.py` — startup crash detection and automatic unbrick recovery sentry
- `core/learned_rules.py` — persistent learned rules manager and dynamic prompt injection engine
- `actions/auto_heal_engine.py` — autonomous traceback analyzer, in-memory AST sandbox, and Gemini hotfix engine
- `actions/system_diagnostics_mcp.py` — 0-credit local OS hardware telemetry, RAM hogs, display brightness, and process termination
- `actions/desktop_organizer_mcp.py` — automated desktop decluttering with safe rollback
- `actions/google_workspace_mcp.py` — native Gmail, Google Calendar, and Drive integration
- `actions/playwright_mcp_client.py` — Microsoft @playwright/mcp client for 24+ browser automation actions
- `actions/` — modular automation, document, and assistant tools
- `brahma_connect/` — local gateway, pairing, and remote routing
- `config/` — local settings, credentials, learned rules, and backups
- `plugins/` — optional plugin extensions
- `tests/` — integration and validation tests

## 🎙️ Command Quick Reference

| Action | Voice / Text Command | Description |
|---|---|---|
| **Simulate Bug** | *"Trigger test bug"* | Triggers safe test error in `actions/test_action.py` to test self-healing |
| **Fix Bug** | *"Brahma, fix that bug"* | Analyzes last traceback, synthesizes AST hotfix via Gemini, and patches |
| **Undo Patch** | *"Brahma, undo last patch"* | Restores modified file from atomic `.bak` backup |
| **Patch Log** | *"Show patch history"* | Displays recent hotfixes, target files, and status |
| **Learn Rule** | *"Remember to always [preference]"* | Permanently saves directive into system prompt |
| **Show Rules** | *"Show learned rules"* | Lists all active behavioral directives |
| **RAM Hogs** | *"What's eating my RAM?"* | Pinpoints top memory-consuming applications |
| **Battery** | *"Check battery status"* | Reports battery health, percent, and power state |
| **Kill Process** | *"Kill chrome"* | Safely terminates frozen applications |
| **Brightness** | *"Dim screen 20%"* / *"Set brightness 80"* | Adjusts multi-monitor display brightness |
| **Clean Desktop** | *"Organize my desktop"* | Sorts desktop clutter into categorized folders |
| **Browser Action** | *"Go to github.com and click explore"* | Automated browsing, clicking, and form-filling via Playwright MCP |

## Plugin System

Extend Brahma Echo with custom Python plugins by adding files to `plugins/`.

Supported hooks:

- `on_brahma_created(brahma)` — called when the assistant instance is initialized
- `on_startup(brahma)` — called after startup when plugins are registered
- `on_text_command(text, source, brahma=None)` — called for each incoming text command; return `True` to indicate the command was handled

## Best Practices

- Keep credentials in `config/api_keys.json` and avoid committing secrets.
- Use the virtual environment for all development and runtime sessions.
- Restart the app after changing config or adding plugins.
- Review `config/app_settings.json` to tune voice, UI, and automation behavior.

## Community & Support

- Discord: https://discord.gg/gEYmJKKtq3

## License

This project is published under a custom source-available license. See `LICENSE` for details.

## Maintainer

- Suryaansh Tiwari

> Preserve attribution and keep credentials secure when building on top of Brahma Echo.
