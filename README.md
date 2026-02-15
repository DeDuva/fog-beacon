# fog-beacon

Automated weekly industry research reports using Claude AI with web search.

Reports are posted as **GitHub Discussions** (for team commentary) and archived to **GitHub Pages** (for browsing).

## What It Does

Every Monday at 8 AM UTC, a GitHub Actions workflow:
1. Sends a research prompt to Claude with web search enabled
2. Claude searches the web for current developments across AI coding agents, platform engineering, and infrastructure trends
3. The report is posted as a **GitHub Discussion** for team discussion
4. The report is committed to `docs/reports/` and published to **GitHub Pages**

## Where to Find Reports

- **Discuss:** [Discussions tab](../../discussions) — comment and react on reports
- **Browse:** GitHub Pages site — `https://<owner>.github.io/fog-beacon/`
- **Download:** Actions tab → workflow run → Artifacts (retained 90 days)

## Setup

### 1. Add your Anthropic API key

Go to **Settings → Secrets and variables → Actions → New repository secret**:
- Name: `ANTHROPIC_API_KEY`
- Value: your key from [console.anthropic.com](https://console.anthropic.com/)

### 2. Enable GitHub Pages

Go to **Settings → Pages → Build and deployment**:
- Source: **Deploy from a branch**
- Branch: `main`, folder: `/docs`

### 3. Create issue labels

```bash
gh label create automated-report --color 0075ca --description "Auto-generated research report"
gh label create weekly --color e4e669 --description "Weekly scheduled report"
gh label create error --color d73a4a --description "Workflow error"
```

### 4. Run manually (first test)

```bash
gh workflow run "Weekly Industry Research Report"
```

Or go to **Actions → Weekly Industry Research Report → Run workflow**.

## Configuration

### Change schedule

Edit `.github/workflows/weekly-report.yml`:
```yaml
schedule:
  - cron: '0 8 * * 1'  # Monday 8 AM UTC
```

### Change model

When triggering manually, select between `claude-sonnet-4-5-20250929` (faster, cheaper) and `claude-opus-4-6` (deeper analysis).

### Customize the prompt

Edit `prompts/weekly-research.md` to adjust research focus areas, competitors to track, or output format.

## Cost

- **Sonnet 4.5 + web search:** ~$0.50–2.00 per report
- **Opus + web search:** ~$5–15 per report
- **GitHub Actions:** free for private repos (2000 min/month)

## Project Structure

```
.github/workflows/weekly-report.yml  — GitHub Actions workflow
scripts/generate_report.py           — Python script calling Claude API
scripts/requirements.txt             — Python dependencies
prompts/weekly-research.md           — Research prompt template
docs/_config.yml                     — Jekyll config for GitHub Pages
docs/index.md                        — Auto-generated report index
docs/reports/                        — Archived weekly reports
```
