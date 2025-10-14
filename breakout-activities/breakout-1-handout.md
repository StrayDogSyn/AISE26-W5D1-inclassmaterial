# Breakout Activity 1: Fix the Failing Tests

## Objective
Get hands-on experience with the CI/CD workflow by fixing failing tests and seeing them pass in GitHub Actions.

## Duration
15 minutes

## Background
Your team has discovered that some tests are failing in the `test_calculator_fail.py` file. The calculator module needs to be updated to handle these edge cases properly.

## Tasks

### Task 1: Run the Failing Tests Locally
1. Run the failing test suite locally:
   ```bash
   pytest tests/test_calculator_fail.py -v
   ```
2. Review the test failures and understand what's expected

### Task 2: Analyze the Problems
Look at the failing tests and identify:
- What functionality is being tested?
- Why are the tests failing?
- What changes are needed to the calculator?

### Task 3: Update the Workflow
1. Open `.github/workflows/ci.yml`
2. Add the failing tests to the workflow:
   ```yaml
   - name: Run all tests
     run: |
       pytest tests/test_calculator_pass.py tests/test_calculator_fail.py -v
   ```

### Task 4: Create a Pull Request
1. Create a new branch: `git checkout -b fix-calculator-tests`
2. Commit your changes
3. Push to GitHub
4. Create a pull request
5. Watch the CI pipeline run!

## Discussion Questions

1. **What happened when you pushed your changes?**
   - Did the CI pipeline start automatically?
   - Where can you see the test results?

2. **Why is it important to run tests in CI?**
   - What if someone forgot to run tests locally?
   - How does this help the team?

3. **What would you do if tests passed locally but failed in CI?**
   - Environment differences?
   - Dependencies?

## Bonus Challenges

### Challenge 1: Add a New Function
Uncomment the tests in `test_calculator_fail.py` for `square_root` and `absolute` functions, then implement these functions in the calculator module.

### Challenge 2: Improve Test Coverage
Write additional tests for edge cases:
- What happens with very large numbers?
- What about negative numbers in power function?
- Test decimal precision

### Challenge 3: Add Code Coverage Reporting
Add a code coverage step to your CI workflow:
```yaml
- name: Run tests with coverage
  run: |
    pip install pytest-cov
    pytest --cov=app tests/ --cov-report=term-missing
```

## Success Criteria
✅ All tests in `test_calculator_fail.py` pass  
✅ CI pipeline runs successfully on GitHub  
✅ Pull request shows green check marks  
✅ You understand how the CI/CD workflow triggered  

## Resources
- [pytest documentation](https://docs.pytest.org/)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- Calculator module: `app/calculator.py`

---

**Need Help?** Ask your instructor or collaborate with your group!

