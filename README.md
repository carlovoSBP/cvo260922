# Paleofuturistic Python Project

[![Version](https://img.shields.io/badge/version-0.0.0-blue)](https://pypi.org/project/cvo260922/)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue?logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](https://opensource.org/license/apache-2.0)
[![Documentation: Diátaxis](https://img.shields.io/badge/docs-Di%C3%A1taxis-009485?logo=readthedocs&logoColor=white)](https://diataxis.fr/)
[![Build](https://img.shields.io/badge/build-unknown-lightgrey)](https://github.com/features/actions)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://coverage.readthedocs.io/)
[![pyscn quality](https://img.shields.io/badge/pyscn-A-brightgreen)](https://pyscn.ludo-tech.org)

Development flow as Paleofuturistic Python

## Usage

Legacy: `pip install cvo260922`

Preferred: `uv add cvo260922`

## Documentation

Full documentation lives in [`docs/`](docs/index.md) — build and open it with `./workflow.cmd document`, or read it online once GitHub Pages is enabled for the repository (`./workflow.cmd document.deploy-github` publishes it).

## Developing

> Development flow as [Paleofuturistic Python](https://github.com/schubergphilis/paleofuturistic_python)

Prerequisite: [uv](https://docs.astral.sh/uv/). Every development action runs through `./workflow.cmd <task>` — the first run bootstraps the environment automatically.

The one command to remember is `./workflow.cmd preflight`: it lints, type-checks, tests, builds, and checks that the badges above and the coverage bar match what the tools measured. It is exactly what the pre-push hook and CI run, so a green run here means a green pipeline. Add `--write` when it tells you a badge is stale and it updates them. The hooks cover the rest — the staged files on every commit, `preflight` on every push.

The scaffold manual lives in the docs' **Developer** section: start with [First-run setup](docs/developer/tutorials/first-run-setup.md); the full command list is in the [Invoke task catalog](docs/developer/reference/invoke-tasks.md).
