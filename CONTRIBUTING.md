# Preamble

This bot is designed to be, first of all, easy to use. When you design a new feature, keep this in mind: no one wants to lose time to understand how this bot works.

# Linting rules

All the code must adhere this rules:
- Class names and variables must be CamelCase
- File names and methods declarations must be snake_case

# Code rules

- Test your code before pushing it or submitting a pull request. A CI system will be implemented as soon as possible
- The use of global variables is heavily discouraged
- Follow the DRY (don't reply yourself) principle: when you're copy-pasting code it means that there is a better way of doing what you're coding
- Write clean e understandable code. Comments and documentation should be always written to help others to understand what you did
- Don't reinvent the wheel: always check if there is some library that is already doing what you're trying to implement
- Use design pattern when possible

# Workflow
- Don't push or force push in master. Create a PR first
- Every new feature or bug fix has to be implemented in a separated branch. When the new feature/bug fix is done, this has to be pull requested against the `master`. A reviewer will check it and, if it's all ok, merge it eventually.
- When the code is stable enough, a new tag (release) has to be created from `master`. The name of the release must follow this pattern: <sad adj + alcoholic drink name>. The release names have to be in alphabetical order.
