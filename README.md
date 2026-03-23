## GitOps CI Automation Project

## Overview

This project demonstrates how a small engineering team can work in a structured and reliable way using a GitOps-style workflow.

Instead of pushing code directly and hoping for the best, this setup ensures that:

- Work is tracked clearly
- Code changes are controlled
- Quality checks run automatically before merging

The application itself is a simple Flask API with three endpoints:

- `/health` → checks if the service is running
- `/sum` → adds two numbers
- `/reverse-string` → reverses a string

The real focus of this project is not the application, but the workflow, automation, and collaboration process.

---

## Architecture

This project connects three main tools:

- **Trello** → Task tracking and visibility
- **GitHub** → Source control (single source of truth)
- **GitHub Actions** → Automation (CI pipeline)

### How they work together

1. Tasks are created in Trello
2. Each task has a unique ID (e.g., TRELLO-001)
3. Work is done in GitHub using branches linked to that ID
4. A Pull Request is opened
5. GitHub Actions runs:
    - Linting (flake8)
    - Testing (pytest)
6. Only passing code is merged into `main`

This ensures that the main branch always stays stable.

## Development Workflow

The workflow used in this project is simple and consistent:

1. Pick a task from Trello (Backlog)
2. Move it to **In Progress**
3. Create a branch:feature/TRELLO-###-description
4. Make your changes
5. Commit using:[TRELLO-###] short message
6. Push your branch
7. Open a Pull Request
8. Wait for CI checks to pass
9. Merge to main
10. Move task to **Done**

## Branching Strategy

- `main` → stable and production-ready code only
- `feature/*` → all development work

Example:

feature/TRELLO-002-add-tests

## Commit Convention

All commits must follow this format:

[TRELLO-###] Short description

Example:

[TRELLO-001] Setup project

[TRELLO-002] Add CI pipeline

This makes it easy to trace changes back to tasks.

## Getting Started

### Clone the repository

git clone

### Move into the project folder

cd gitops-ci-project

### Install dependencies

pip install -r requirements.txt

### Run tests

pytest test_app.py -v

All tests must pass before making any changes.

## CI/CD Pipeline

This project uses GitHub Actions to enforce quality automatically.

### When it runs:

- On push to any branch
- On Pull Requests to main

### What it does:

1. Installs dependencies
2. Runs flake8 (linting)
3. Runs pytest (tests)

### Rules:

- If lint fails → build fails ❌
- If tests fail → build fails ❌
- PR cannot be merged until all checks pass

## Testing

The project includes 8 test cases covering:

- API health check
- Sum calculations (including edge cases)
- String reversal functionality

All tests must pass before merging any code.

## Task Management (Trello)

Work is tracked using a Trello board with the following columns:

1. Backlog
2. In Progress
3. Review/QA
4. Done

Each task:

- Has a unique ID
- Moves across the workflow stages
- Is linked to commits and PRs

## Evidence Collected

As part of this project, the following were demonstrated:

- Successful CI runs (green builds)
- Intentional failure (red build)
- Pull Request merge blocking
- Trello workflow movement

## Reflection

### What I learned

This project helped me understand how proper workflows improve software development. I learned how to use Git branches, write meaningful commits, and rely on automation instead of manual checks.

### Why GitOps is important

GitOps ensures that Git is the single source of truth. Every change is tracked, reviewed, and validated before it becomes part of the system.

### Challenges faced

Setting up GitHub Actions and understanding CI behavior was initially challenging. It took some trial and error to get the pipeline working correctly.

### How CI improves quality

CI prevents broken code from being merged by automatically running checks. This reduces bugs and improves confidence in the codebase.

### Real-world application

In a real team, this workflow helps multiple developers collaborate without conflicts. It ensures consistency, accountability, and reliability.

## Conclusion

This project demonstrates how combining task tracking, version control, and automation can create a clean and efficient development workflow. It reflects how modern teams build and maintain reliable systems.
