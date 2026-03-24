# Contributing Guide

This document explains how to contribute to this project in a clean and consistent way.

## Development Workflow

Follow this process for every task:

1. Pick a task from Trello
2. Move it to **In Progress**
3. Create a feature branch
4. Make your changes
5. Commit your work
6. Push your branch
7. Open a Pull Request
8. Wait for CI checks
9. Merge if everything passes
10. Move task to **Done**

## Branching Rules

- Never work directly on `main`
- Always create a feature branch

Format:

feature/TRELLO-###-description

Example:

feature/TRELLO-003-add-tests

## Commit Format

All commits must follow:

[TRELLO-###] Short message

Example:

[TRELLO-002] Fix endpoint

This helps track work back to Trello tasks.

## Pull Request Process

- Create PR from feature branch → main
- Include Trello ID in the title
- Add a short description of changes
- Wait for CI checks to pass

Rules:

- No direct push to main
- No merge if CI fails

## CI/CD Process

GitHub Actions automatically runs on every push and PR.

Steps:

1. Install dependencies
2. Run linting (flake8)
3. Run tests (pytest)

If any step fails:

- The build turns red
- The PR is blocked
- You must fix the issue before merging

## Coding Standards

- Follow basic Python best practices
- Keep code simple and readable
- Avoid unnecessary complexity
- Ensure all tests pass

## Handling Failures

If your build fails:

1. Open GitHub Actions logs
2. Identify the error
3. Fix the issue locally
4. Commit and push again

Repeat until the build passes.

## Task Tracking

All work must be linked to a Trello card.

- Use the card ID in:
    - Branch name
    - Commit message
    - Pull Request title

This ensures traceability.
