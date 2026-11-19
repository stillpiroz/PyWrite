# Contributing

Contributions are welcome and greatly appreciated! There are several ways to contribute to PyWrite.

## Report Bugs

Report bugs on the [GitHub Issues](https://github.com/stillpiroz/PyWrite/issues) page.

When reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might help with troubleshooting.
- Detailed steps to reproduce the bug.
- Expected behavior and actual behavior.

## Suggest Features

If you have an idea for a new feature or an improvement to an existing one, feel free to open an issue on the [GitHub Issues](https://github.com/stillpiroz/PyWrite/issues) page.

When suggesting a feature, please include:

- A clear description of the proposed feature.
- The problem or use case it would address.
- Any additional details that might help explain your idea.

## Development Setup

Ready to contribute? Follow these steps to set up PyWrite for local development.

1. Fork the PyWrite repository.

2. Clone your fork locally:

   ```bash
   git clone git@github.com:your_name_here/PyWrite.git
   cd PyWrite
   git remote add upstream git@github.com:stillpiroz/PyWrite.git
   ```

3. Create a branch for your changes:

   ```bash
   git checkout -b name-of-your-bugfix-or-feature
   ```

4. Install the project dependencies:

   ```bash
   uv sync
   ```

5. Make your changes locally.

6. Run the tests to make sure your changes pass:

   ```bash
   uv run pytest
   ```

7. Commit your changes (see [Writing Commit Messages](#writing-commit-messages)).

8. Submit a pull request through GitHub.

## Documentation

- Keep documentation clear, concise, and up to date.
- Update relevant documentation when changing existing features or adding new ones.

## Writing Commit Messages

PyWrite requires all commits to follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

Every commit message must start with a type and a short description.

Example:

```text
docs: this is only for example
```

For commits containing multiple changes, you can use a commit body with bullet points. Preferably, keep it to three items or fewer. Four items are acceptable when necessary.

Example:

```text
docs: update project documentation

- Add contribution guidelines
- Update development instructions
- Improve documentation structure
```

Alternatively, you can use a descriptive paragraph instead of bullet points:

```text
docs: update project documentation

Improve the documentation by adding contribution guidelines and development instructions.
```

For a real example, see [this commit](https://github.com/stillpiroz/PyWrite/commit/84bf35e6ab39a2d279101ae0828278e16652e6be).

## Code Style

All code contributions must follow PEP 8.

- Write docstrings for every module and class.
- Functions must have docstrings unless they are methods inside a class and their purpose is self-explanatory.
- Add comments where necessary to explain non-obvious logic.
- Keep comments accurate and up to date.

Good comment:

```python
# Preserve the original order when priorities are equal.
items.sort(key=lambda item: item.priority)
```

Bad comment:

```python
# Sort items alphabetically.
items.sort(reverse=True)
```

## AI Usage Policy

Before contributing, read the [AI Usage Policy](AI_USAGE_POLICY.md) in the project root.

This policy applies to all contributions, including code, documentation, and other project-related work.
