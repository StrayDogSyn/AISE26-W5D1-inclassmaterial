# W5D1 - CI/CD Fundamentals: GitHub Actions, Automated Testing, Deployment

<!-- ci-trigger: noop update to README to trigger GitHub Actions workflows -->

**Format:** Virtual In-Class + Individual Assignment  
**Language:** Python  
**Skills:** CI/CD, GitHub Actions, Automated Testing, YAML, Deployment Pipelines  
**Duration:** 3 hours (6:30 PM – 9:30 PM)

## Overview

Imagine this: It's Friday at 5 PM. You finally merge your feature branch to main, head home, and 10 minutes later… production goes down. No one ran tests, no one deployed to staging first, and now your team is paged all weekend.

This is exactly the pain CI/CD is meant to solve. Continuous Integration automatically runs your tests on every commit or pull request, so you know right away if something broke. Continuous Delivery and Deployment ensure your code gets to staging or production safely, without last-minute fire drills.

In this session, you'll learn how to implement automated testing and deployment pipelines using GitHub Actions. Say goodbye to "it worked on my machine" and Friday 5 PM production disasters—automation is here to save the day.

## Learning Objectives

By completing this assignment, you will:

- Explain the purpose of CI/CD pipelines in modern development teams
- Differentiate Continuous Integration, Continuous Delivery, and Continuous Deployment
- Write a GitHub Actions workflow (`.github/workflows/ci.yml`) that runs tests on push and pull request
- Trigger, observe, and troubleshoot a failing CI workflow
- Extend a workflow with a dependent "deploy" job that only runs after tests pass
- Configure branch protection rules to enforce CI checks
- Resolve common CI/CD failure causes (failing tests, YAML syntax errors)

## Prerequisites

Before starting this lesson, ensure you have:

- Completed W4D4 (Logging & Monitoring)
- Python 3.9+ installed on your machine
- A GitHub account
- Git installed and configured
- VS Code or your preferred code editor
- pytest installed: `pip install pytest`

## Assignment Overview

Transform a basic Python calculator application into a professionally configured repository with automated CI/CD pipelines. You'll start with intentionally failing tests, fix them, add automated testing across multiple Python versions, and implement gated deployments that only run when tests pass.

Your final repository will include:

- Working GitHub Actions workflow that runs on every push and pull request
- Test suite that passes in CI
- Python version matrix testing (3.10 and 3.11)
- Deployment job that only runs after successful tests
- Branch protection rules requiring CI to pass before merging
- Professional documentation

## In-Class Activities

### Part 1: Your First CI Workflow (6:30-7:35 PM)

**What You'll Do:**

- Create a GitHub repository with a basic Python calculator app
- Set up a GitHub Actions workflow (`.github/workflows/ci.yml`)
- Observe an intentionally failing CI run
- Fix the failing test and watch CI turn green
- Understand how the `needs:` keyword gates deployment after tests pass

**Deliverable:**

- Screenshots of both failing (red ❌) and passing (green ✅) CI runs

### Part 2: Pull Requests & Test Matrix (7:45-8:35 PM)

**What You'll Do:**

- Create a feature branch and open a pull request
- Watch CI run automatically on your PR
- Add a Python version matrix to test across Python 3.10 and 3.11
- Observe parallel test execution
- Confirm deployment waits for all matrix jobs to succeed

**Deliverable:**

- Working pull request with matrix testing across multiple Python versions

### Part 3: Branch Protection & Debugging (8:35-9:05 PM)

**What You'll Do:**

- Configure branch protection rules on the `main` branch
- Require status checks to pass before merging
- Practice debugging common CI failures (YAML indentation, test failures, branch mismatches)
- Document your resolution approach

**Deliverable:**

- Protected `main` branch with required CI checks
- Experience troubleshooting realistic CI/CD issues

## Deliverables & Submission

Submit to Canvas Module W5D1:

1. **Repository Link** - Your forked/created repository with working CI/CD
2. **Screenshots**
   - Failing CI run (red ❌)
   - Passing CI run (green ✅, including deploy job)
3. **README Reflection** - 2-3 sentences on what you learned about CI/CD
4. **Working Workflow** - `.github/workflows/ci.yml` with gated deploy job

### Grading Criteria (10 points)

- Workflow triggers on push/PR: 2 points
- Tests run in CI: 2 points
- Failing run screenshot: 2 points
- Passing run screenshot: 2 points
- Deploy gated by tests (`needs:`): 1 point
- Clear README reflection: 1 point
- **Bonus:** Python version matrix (3.10 & 3.11): +2 points

## Setup Instructions

### Option 1: Work Directly in GitHub (Recommended for Beginners)

1. Fork this repository to your GitHub account
2. Navigate to the Actions tab to see CI/CD in action
3. Follow along with the instructor during the live session
4. Edit files directly in GitHub's web interface to trigger workflows

### Option 2: Local Development Setup

#### For Mac/Linux

```bash
# Clone the repository
git clone https://github.com/TylarCam/AISE26-W5D1-inclassmaterial.git
cd AISE26-W5D1-inclassmaterial

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# Run tests locally
pytest -q
```

#### For Windows (PowerShell)

```powershell
# Clone the repository
git clone https://github.com/TylarCam/AISE26-W5D1-inclassmaterial.git
cd AISE26-W5D1-inclassmaterial

# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# If you get an execution policy error, run as Admin:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# Run tests locally
pytest -q
```

## Repository Structure

```text
AISE26-W5D1-inclassmaterial/
├── .github/
│   └── workflows/
│       └── ci.yml                    # GitHub Actions workflow
├── app/
│   └── calculator.py                 # Sample Python application
├── tests/
│   ├── test_calculator_pass.py       # Passing test suite
│   └── test_calculator_fail.py       # Initially failing tests (you'll fix these!)
├── lesson-materials/
│   ├── slides.pdf                    # Session slides
│   └── ci-cd-pipeline-diagram.png    # Visual reference
├── live-coding/
│   ├── 01-minimal-workflow.yml       # Basic workflow example
│   ├── 02-add-tests.py               # Test examples
│   └── 03-deploy-job.yml             # Deployment configuration
├── breakout-activities/
│   ├── breakout-1-handout.md         # First breakout activity
│   ├── breakout-1-solution.md        # TTA solution
│   ├── breakout-2-handout.md         # Second breakout activity
│   └── breakout-2-solution.md        # TTA solution
├── requirements.txt                  # Python dependencies
└── README.md                         # You are here!
```

## Understanding the Workflow

Our CI/CD pipeline (`.github/workflows/ci.yml`) performs the following steps:

1. **Triggers** on every push to `main` and on pull requests
2. **Runs tests** across multiple Python versions (3.10 and 3.11)
3. **Caches dependencies** to speed up future runs
4. **Gates deployment** - deploy job only runs if tests pass
5. **Simulates deployment** to a staging environment

### Key Workflow Components

**Jobs:**

- `build-and-test`: Checks out code, sets up Python, installs dependencies, runs tests
- `deploy`: Only runs after `build-and-test` succeeds (controlled by `needs:`)

**Matrix Strategy:**

- Tests run in parallel across Python 3.10 and 3.11
- Ensures compatibility across versions
- Deploy waits for all matrix jobs to complete successfully

**Cache:**

- Caches pip dependencies to speed up subsequent runs
- Reduces build time significantly

## Troubleshooting

### Actions Didn't Run?

- Check that `on:` branches match your branch name
- Make sure you pushed your commits
- Verify GitHub Actions is enabled (Settings → Actions → Allow all actions)

### YAML Error?

- Spaces matter! Use 2 spaces for indentation, never tabs
- Check for missing colons or mismatched quotes
- Validate YAML syntax at [yamllint.com](http://www.yamllint.com/)

### Tests Can't Import `app`?

- Ensure folder is named `app/` (not `src/` or `application/`)
- File must be named `calculator.py`
- Tests should use `from app.calculator import ...`

### Windows PowerShell Execution Policy Error?

```powershell
# Run PowerShell as Administrator, then:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### CI Green But Deploy Skipped?

- Confirm `needs: build-and-test` is present in deploy job
- Check any `if:` conditions on the deploy job
- Ensure it's a push to `main` (not just a PR)

### Common CI Failure Patterns

**YAML Indentation Error:**

- Remove or add spaces to break the workflow
- Fix by restoring proper 2-space indentation

**Branch Mismatch:**

- Workflow specifies `main` but you're pushing to `master`
- Update `on.push.branches` to match your branch name

**Test Failure:**

- Assertion error in test code
- Fix the test or the application code to make tests pass

## Key Concepts

- **Continuous Integration (CI):** Merging code frequently with automated builds/tests
- **Continuous Delivery (CD):** Ensuring code is always deployable (may require manual approval)
- **Continuous Deployment:** Fully automated deploys after CI passes
- **Workflow:** YAML file describing jobs that run on GitHub Actions
- **Job:** A group of steps executed on a runner
- **Runner:** VM/container that executes workflow steps
- **Trigger:** Event that starts a workflow (push, pull_request, schedule)
- **Matrix:** Running the same job across multiple configurations (e.g., Python versions)
- **Artifact:** Files produced during a workflow run
- **Idempotent Build:** A build that produces the same result every time

## Resources

### Pre-Class Materials

- [What is CI/CD? (GitHub Guide)](https://github.com/resources/articles/devops/ci-cd) (10 min read)
- [Introduction to GitHub Actions](https://www.youtube.com/watch?v=S97uzhRQKEI) (45 min video)
- [Continuous Delivery vs Deployment](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment) (5 min read)

### Documentation

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax Reference](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [pytest Documentation](https://docs.pytest.org/)

### Industry Context

This is how every major tech company prevents production outages. GitHub Actions is widely adopted across startups (Stripe, Vercel) and enterprises (Microsoft, Netflix, NASA). Automated testing and deployment pipelines are considered essential professional development practices.

## Best Practices

1. **Keep workflows fast** - Cache dependencies, parallelize jobs
2. **Write atomic commits** - Small, focused changes are easier to debug
3. **Meaningful commit messages** - Future you will thank present you
4. **Always run tests before merging** - Protect your `main` branch
5. **Monitor your CI/CD** - Set up Slack/email notifications for failures
6. **Use matrix testing** - Verify compatibility across versions and environments
7. **Gate deployments** - Never deploy without passing tests

## Getting Help

- **During Class:** Ask questions in Zoom chat or raise your hand
- **After Class:** Post in the Canvas discussion board or Slack channel
- **GitHub Issues:** Open an issue in this repository for bugs or suggestions
- **Office Hours:** Check Canvas for TTA office hours schedule

## License

This repository is for educational purposes as part of the fellowship program. All code examples are MIT licensed unless otherwise specified.
