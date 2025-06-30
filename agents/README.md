# Agents Directory

This directory contains agent scripts and supporting files for the agno-Test project.

## Key Files

- `.env.example` — Example environment variable file. Copy to `.env` and add your API keys.
- `.env` — Your actual environment variables (should NOT be committed to git).
- `.gitignore` — Ensures sensitive files like `.env` and virtual environments are not tracked by git.
- `requirments.txt` — Python dependencies for agent scripts.
- `basic_agent/basic_agent.py` — Example agent using OpenAI's GPT-4o to answer questions, including in Darija, and saving responses to a file.

## Usage

1. **Install dependencies:**
   ```sh
   pip install -r requirments.txt
   ```
2. **Set up your environment:**
   - Copy `.env.example` to `.env` and add your OpenAI API key.
3. **Run an agent script:**
   ```sh
   python agent_list/basic_agent/basic_agent.py
   ```
   - Responses will be saved in `responses_darija.txt`.

## Security
- Never commit your `.env` file. It is ignored by git for your safety.

## Notes
- You can add more agent scripts or modify existing ones as needed.
- For new environments or API keys, update `.env.example` for team clarity.
