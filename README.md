# cbgh-lab-open

Sample open-source style project used as a CI research range.

## Layout

- `src/app.py` — tiny application module
- `tests/` — unit tests run in CI
- `buildspec.yml` — AWS CodeBuild definition

## CI

Every pull request runs the test suite on AWS CodeBuild.
