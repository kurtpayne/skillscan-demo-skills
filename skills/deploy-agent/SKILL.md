---
name: deploy-agent
version: "1.0.0"
description: Automates deployment of applications to cloud infrastructure.
author: skillscan-demo
allowed-tools:
  - bash
  - http_fetch
  - read_file
  - write_file
tags:
  - devops
  - deployment
---

## Description

This skill automates application deployment workflows. It:

1. Reads the deployment configuration from the project root
2. Executes shell commands to build and package the application
3. Pushes artifacts to the configured cloud provider via HTTP API calls
4. Verifies deployment health by fetching the application's health endpoint

## Deployment Steps

Run the build script using bash to compile and package artifacts:
```
bash ./scripts/build.sh
```

Upload the packaged artifact to the deployment target using curl:
```
curl -X POST https://deploy.example.com/api/v1/releases \
  -H "Authorization: Bearer $DEPLOY_TOKEN" \
  -F "artifact=@dist/app.tar.gz"
```

Verify the deployment succeeded by checking the health endpoint:
```
curl https://app.example.com/health
```

## Network Access

This skill requires outbound network access to:
- The deployment API (`deploy.example.com`)
- The application health endpoint
- Package registries for dependency resolution

## Shell Execution

Shell access is required for:
- Running build scripts
- Packaging artifacts
- Environment variable interpolation
