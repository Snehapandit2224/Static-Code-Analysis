1. Which issues were the easiest to fix, and which were the hardest? Why?

Easiest: The formatting and style issues reported by Flake8 (such as missing blank lines, unused imports, and long lines) were the easiest to fix since they only required small structural or spacing adjustments.

Hardest: The hardest issues were the security-related ones, particularly replacing the unsafe eval() call and restructuring code to eliminate the global variable. These required logical changes and careful testing to ensure functionality remained correct.

2. Did the static analysis tools report any false positives? If so, describe one example.

None of the tools reported clear false positives. However, Pylint’s “logging-fstring-interpolation” warnings initially seemed unnecessary because the code used f-strings intentionally for readability. Later, I realized this wasn’t a false positive—Pylint’s advice was valid for performance reasons, as logging should defer string formatting until needed.

3. How would you integrate static analysis tools into your actual software development workflow?

I would integrate Pylint, Flake8, and Bandit into a Continuous Integration (CI) pipeline (e.g., GitHub Actions or GitLab CI) so that every commit triggers an automated lint and security scan.

During local development, I’d run these tools pre-commit using pre-commit hooks to catch errors early and maintain consistent code quality before pushing to the repository.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The code became more readable and maintainable, following consistent naming conventions and spacing.

Security and robustness improved significantly by removing the eval() function, adding input validation, and using context managers for file handling.

The new logging implementation provides clearer runtime insight, and the addition of docstrings enhances code documentation and usability.

Overall, the code evolved from a functional but unsafe script into a clean, well-structured, and production-ready program.