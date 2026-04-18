---
name: code-reviewer
version: "1.0.0"
description: Reviews code for style, bugs, and best practices.
author: skillscan-demo
allowed-tools:
  - read_file
  - write_file
tags:
  - development
  - code-quality
---

## Description

Analyze source code files for common issues including:
- Style violations and formatting inconsistencies
- Potential bugs and logic errors
- Opportunities for refactoring

## Usage

Point the skill at a source file or directory. It reads each file,
analyzes the code, and writes a review report with line-level comments.
