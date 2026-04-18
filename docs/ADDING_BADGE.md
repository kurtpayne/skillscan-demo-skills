# Adding a SkillScan Badge to Your Skill Repo

This guide walks you through adding a SkillScan security badge to your
AI agent skill repository. The badge updates automatically on every push.

## Prerequisites

- A GitHub repository containing one or more skill files (SKILL.md)
- GitHub Actions enabled on the repository

## Step 1: Install SkillScan locally (optional)

Test your skill locally before setting up CI:

```bash
pip install skillscan-security
skillscan scan ./your-skill-directory/
```

Verify it produces the expected verdict (PASS, WARN, or BLOCK).

## Step 2: Add the CI workflow

Create `.github/workflows/skillscan.yml` in your repository:

```yaml
name: SkillScan

on:
  push:
    branches: [main]
    paths: ['skills/**']
  pull_request:
    paths: ['skills/**']

permissions:
  contents: write
  security-events: write
  id-token: write
  attestations: write

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
        with:
          python-version: "3.12"

      - name: Install SkillScan
        run: pip install skillscan-security

      - name: Scan all skills
        run: |
          skillscan scan skills/ --summary --format json --out scan-report.json || true
          skillscan scan skills/ --format sarif --out results.sarif || true

      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v4
        if: always()
        with:
          sarif_file: results.sarif

      - name: Attest report
        if: github.ref == 'refs/heads/main'
        uses: actions/attest-build-provenance@v2
        with:
          subject-path: scan-report.json

      - name: Generate badge
        if: always()
        run: |
          VERDICT=$(python3 -c "import json; print(json.load(open('scan-report.json')).get('verdict','unknown'))" 2>/dev/null || echo "unknown")
          case "$VERDICT" in
            allow) COLOR="brightgreen"; MSG="PASS" ;;
            warn)  COLOR="yellow";      MSG="WARN" ;;
            block) COLOR="red";         MSG="BLOCK" ;;
            *)     COLOR="lightgrey";   MSG="ERROR" ;;
          esac
          VERSION=$(skillscan version --json | python3 -c "import json,sys; print(json.load(sys.stdin)['version'])")
          DATE=$(date -u +%Y-%m-%d)
          printf '{"schemaVersion":1,"label":"SkillScan v%s","message":"%s (%s)","color":"%s"}\n' "$VERSION" "$MSG" "$DATE" "$COLOR" > skillscan-badge.json

      - name: Commit badge
        if: always() && github.ref == 'refs/heads/main'
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add skillscan-badge.json
          git diff --staged --quiet || git commit -m "chore: update SkillScan badge" && git push
```

Adjust the `paths` trigger to match where your skill files live.

## Step 3: Add the badge to your README

Add this line to the top of your `README.md`, replacing `YOUR/REPO` with
your GitHub `owner/repo`:

```markdown
[![SkillScan](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/YOUR/REPO/main/skillscan-badge.json)](https://github.com/YOUR/REPO/actions/workflows/skillscan.yml)
```

## Step 4: Push

Push your changes. The first CI run will:

1. Scan all skills in the configured directory
2. Upload results as SARIF to GitHub Security tab
3. Generate `skillscan-badge.json` and commit it to your repo
4. The badge in your README will update automatically

## Step 5: Attestation (optional)

The workflow above includes an attestation step that provides
cryptographic proof of the scan. Anyone can verify it:

```bash
gh attestation verify reports/scan-report.json --owner YOUR_ORG
```

## Badge states

| Badge | Meaning |
|-------|---------|
| ![PASS](https://img.shields.io/badge/SkillScan-PASS-brightgreen) | All skills passed with no security findings |
| ![WARN](https://img.shields.io/badge/SkillScan-WARN-yellow) | Skills have warnings but no blocking findings |
| ![BLOCK](https://img.shields.io/badge/SkillScan-BLOCK-red) | One or more skills have blocking security findings |

## Troubleshooting

**Badge shows "pending":** The CI workflow hasn't run yet. Push a change
to a file matching the `paths` trigger, or run the workflow manually.

**Badge shows "ERROR":** The scan failed to produce a report. Check the
GitHub Actions logs for details.

**SARIF upload fails:** Ensure `security-events: write` is in your
workflow permissions.
