# Breakout Activity 2: Build a Multi-Stage Pipeline

## Objective
Create a comprehensive CI/CD pipeline with multiple stages, including testing, building, and deployment.

## Duration
20 minutes

## Background
Your team wants to enhance the CI/CD pipeline with multiple stages that mirror a real-world production environment. You'll add linting, security checks, and deployment stages.

## Tasks

### Task 1: Add Linting Stage
Add a linting job to catch code quality issues before tests run.

**Steps:**
1. Install flake8 if not already installed
2. Add a lint job to your workflow
3. Configure it to run in parallel with tests

**Example:**
```yaml
lint:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install linter
      run: pip install flake8
    - name: Run linter
      run: flake8 app/ tests/ --max-line-length=120
```

### Task 2: Add Build Stage
Create a build job that runs after tests pass.

**Requirements:**
- Should only run if test job succeeds
- Should create a "build artifact" (for this exercise, just create a file)
- Upload the artifact using GitHub Actions

**Hint:** Use `needs: test` to create job dependencies

### Task 3: Add Deployment Stages
Create two deployment jobs:
1. **Deploy to Staging** - runs automatically on main branch
2. **Deploy to Production** - requires manual approval

**Steps:**
1. Create a staging deployment job
2. Create a production deployment job
3. Add environment protection rules

### Task 4: Add Notifications
Add a notification step that runs when deployment succeeds.

---

## Pipeline Architecture

Your final pipeline should look like this:

```
       ┌─────────┐
       │  Lint   │
       └────┬────┘
            │
       ┌────▼────┐
       │  Test   │
       └────┬────┘
            │
       ┌────▼────┐
       │  Build  │
       └────┬────┘
            │
       ┌────▼────────┐
       │   Staging   │
       └────┬────────┘
            │
       ┌────▼─────────┐
       │  Production  │
       │  (Manual)    │
       └──────────────┘
```

---

## Detailed Requirements

### Linting Requirements
- Run flake8 on all Python files
- Set max line length to 120
- Exclude common directories (.git, __pycache__, etc.)
- Job should fail if linting errors found

### Build Requirements
- Create a timestamp file as a build artifact
- Package the application files
- Upload artifact for use in deployment stages
- Display build information (date, commit hash, etc.)

### Staging Deployment Requirements
- Only runs on main branch
- Downloads build artifact
- Simulates deployment (use echo statements)
- Runs smoke tests
- Reports deployment status

### Production Deployment Requirements
- Only runs on main branch
- Requires manual approval (use environments)
- Downloads build artifact
- Simulates production deployment
- Includes rollback plan in comments

---

## Discussion Questions

1. **What are the benefits of parallel vs sequential jobs?**
   - When should you run jobs in parallel?
   - When do you need sequential execution?

2. **Why separate staging and production deployments?**
   - What testing happens in staging?
   - What risks does this mitigate?

3. **How would you handle a failed deployment?**
   - Rollback strategies?
   - Notification systems?

4. **What real-world deployment strategies exist?**
   - Blue-Green deployment
   - Canary releases
   - Rolling updates

---

## Bonus Challenges

### Challenge 1: Add Matrix Testing
Test against multiple Python versions:
```yaml
strategy:
  matrix:
    python-version: ['3.8', '3.9', '3.10', '3.11']
```

### Challenge 2: Add Security Scanning
Integrate a security scanner like `bandit`:
```bash
pip install bandit
bandit -r app/
```

### Challenge 3: Add Performance Testing
Create a simple performance test that measures execution time of calculator operations.

### Challenge 4: Implement Caching
Add caching to speed up dependency installation:
```yaml
- uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
```

### Challenge 5: Add Status Badges
Add a status badge to your README showing CI status:
```markdown
![CI Status](https://github.com/YOUR_USERNAME/YOUR_REPO/workflows/CI%20Pipeline/badge.svg)
```

---

## Success Criteria

✅ Lint job runs and passes  
✅ Test job runs and passes  
✅ Build job creates and uploads artifacts  
✅ Staging deployment runs automatically on main  
✅ Production deployment requires manual approval  
✅ All jobs have appropriate dependencies  
✅ Pipeline fails fast when errors occur  

---

## Starter Code

### Sample Build Job
```yaml
build:
  needs: [test, lint]
  runs-on: ubuntu-latest
  
  steps:
    - uses: actions/checkout@v3
    
    - name: Create build artifact
      run: |
        mkdir -p build
        cp -r app/* build/
        echo "Build: $(date)" > build/build-info.txt
        echo "Commit: ${{ github.sha }}" >> build/build-info.txt
        
    - name: Upload artifact
      uses: actions/upload-artifact@v3
      with:
        name: app-build
        path: build/
```

### Sample Deployment Job
```yaml
deploy-staging:
  needs: build
  runs-on: ubuntu-latest
  if: github.ref == 'refs/heads/main'
  environment:
    name: staging
    url: https://staging.example.com
  
  steps:
    - name: Download build artifact
      uses: actions/download-artifact@v3
      with:
        name: app-build
        path: ./build
        
    - name: Deploy to staging
      run: |
        echo "Deploying to staging environment..."
        # Add your deployment commands here
        
    - name: Run smoke tests
      run: |
        echo "Running smoke tests..."
        # Add smoke test commands
```

---

## Resources

- [GitHub Actions: Dependencies](https://docs.github.com/en/actions/using-jobs/using-jobs-in-a-workflow)
- [GitHub Actions: Artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts)
- [GitHub Actions: Environments](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment)
- [GitHub Actions: Matrix Strategy](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs)

---

**Time Check:** Make sure to leave 5 minutes at the end to discuss your pipeline with the group!

