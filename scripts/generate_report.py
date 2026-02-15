#!/usr/bin/env python3
"""Generate a weekly industry research report using Claude with web search."""

import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import anthropic


REPO_ROOT = Path(__file__).resolve().parent.parent
PROMPT_PATH = REPO_ROOT / "prompts" / "weekly-research.md"
OUTPUT_DIR = REPO_ROOT / "output"


def load_prompt() -> str:
    return PROMPT_PATH.read_text(encoding="utf-8")


def generate_report(prompt: str, model: str, additional_context: str) -> str:
    client = anthropic.Anthropic()

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    user_message = f"Today's date is {now}. Focus your research on developments from the past 7 days.\n\n{prompt}"
    if additional_context:
        user_message += f"\n\n## Additional Context\n{additional_context}"

    print(f"Calling {model} with web search enabled...")

    response = client.messages.create(
        model=model,
        max_tokens=16000,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=[{"role": "user", "content": user_message}],
    )

    # Extract text blocks (skip tool use and tool result blocks)
    parts = []
    for block in response.content:
        if block.type == "text":
            parts.append(block.text)

    return "\n".join(parts)


def format_report(body: str, model: str) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    header = (
        f"**Generated:** {now}  \n"
        f"**Model:** `{model}` | **Web search:** enabled\n\n---\n\n"
    )
    footer = (
        "\n\n---\n\n"
        "*Automated by [fog-beacon](https://github.com/DeDuva/fog-beacon) — "
        "weekly industry research powered by Claude AI with web search.*"
    )
    return header + body + footer


def main() -> int:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        return 1

    model = os.environ.get("MODEL", "claude-sonnet-4-5-20250929")
    additional_context = os.environ.get("ADDITIONAL_CONTEXT", "")

    prompt = load_prompt()
    print(f"Loaded prompt ({len(prompt)} chars)")

    body = generate_report(prompt, model, additional_context)
    print(f"Generated report ({len(body)} chars)")

    report = format_report(body, model)

    OUTPUT_DIR.mkdir(exist_ok=True)
    output_file = OUTPUT_DIR / "report.md"
    output_file.write_text(report, encoding="utf-8")
    print(f"Saved to {output_file}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
