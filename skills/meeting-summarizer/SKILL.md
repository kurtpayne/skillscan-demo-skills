---
name: meeting-summarizer
version: "1.0.0"
description: Summarizes meeting transcripts into action items and key decisions.
author: skillscan-demo
allowed-tools:
  - read_file
  - write_file
tags:
  - productivity
  - meetings
---

## Description

Read a meeting transcript and produce a structured summary with:
- Key decisions made
- Action items with owners
- Follow-up questions

## Usage

Provide a meeting transcript as input. The skill reads the file,
processes the content, and writes a summary to the output directory.
