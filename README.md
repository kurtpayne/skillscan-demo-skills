# SkillScan Demo Skills

[![SkillScan](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/kurtpayne/skillscan-demo-skills/main/skillscan-badge.json)](https://github.com/kurtpayne/skillscan-demo-skills/actions/workflows/skillscan.yml)

A collection of example AI agent skills demonstrating
[SkillScan](https://skillscan.sh) security scanning.

## What's here

| Skill | Badge | Verdict | Findings | Description |
|-------|-------|---------|----------|-------------|
| [meeting-summarizer](skills/meeting-summarizer/) | [![SkillScan](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/kurtpayne/skillscan-demo-skills/main/skills/meeting-summarizer/skillscan-badge.json)](https://github.com/kurtpayne/skillscan-demo-skills/actions/workflows/skillscan.yml) | PASS | 0 | Clean productivity skill |
| [code-reviewer](skills/code-reviewer/) | [![SkillScan](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/kurtpayne/skillscan-demo-skills/main/skills/code-reviewer/skillscan-badge.json)](https://github.com/kurtpayne/skillscan-demo-skills/actions/workflows/skillscan.yml) | PASS | 1 | Clean with advisory |
| [weather-lookup](skills/weather-lookup/) | [![SkillScan](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/kurtpayne/skillscan-demo-skills/main/skills/weather-lookup/skillscan-badge.json)](https://github.com/kurtpayne/skillscan-demo-skills/actions/workflows/skillscan.yml) | PASS | 0 | Minimal example |
| [deploy-agent](skills/deploy-agent/) | [![SkillScan](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/kurtpayne/skillscan-demo-skills/main/skills/deploy-agent/skillscan-badge.json)](https://github.com/kurtpayne/skillscan-demo-skills/actions/workflows/skillscan.yml) | WARN | 2 | Risky but declared tools |
| [data-exfiltrator](skills/data-exfiltrator/) | [![SkillScan](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/kurtpayne/skillscan-demo-skills/main/skills/data-exfiltrator/skillscan-badge.json)](https://github.com/kurtpayne/skillscan-demo-skills/actions/workflows/skillscan.yml) | BLOCK | 11 | Intentionally malicious (test) |

## Add SkillScan to your skill repo

See [docs/ADDING_BADGE.md](docs/ADDING_BADGE.md) for a step-by-step guide.

**Quick version:**

1. Copy `.github/workflows/skillscan.yml` to your repo
2. Add the badge to your README:
   ```markdown
   [![SkillScan](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/YOUR/REPO/main/skillscan-badge.json)](https://github.com/YOUR/REPO/actions/workflows/skillscan.yml)
   ```
3. Push. The badge updates automatically on every commit.

## Scan reports

Pre-generated reports are in [reports/](reports/). Run locally:

```bash
pip install skillscan-security
skillscan scan skills/meeting-summarizer/
skillscan scan skills/data-exfiltrator/
```

## Attestation

Scan reports in this repo are attested via GitHub artifact attestation.
Verify with:

```bash
gh attestation verify reports/meeting-summarizer.json --owner kurtpayne
```
