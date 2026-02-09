# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

This is an AI skill management system implementing **Meta-Methodology** - a recursive self-optimizing generative system. The project consists of two main components:

1. **Khazix-Skills** - Current implementation with 3 core skills
2. **Meta-Skills** - Upcoming refactored framework with recursive self-optimization

### Meta-Methodology Core Concepts

The system implements a recursive optimization loop:

- **Bootstrap (创生)**: Generate initial α-Generator and Ω-Optimizer
- **Self-Reflection (自省与进化)**: Ω optimizes α, creating evolved α
- **Generation (创造)**: α generates all target skills
- **Recursive Loop (循环与飞跃)**: Feed results back to continue evolution

---

## Architecture

### Current Structure (Khazix-Skills)

```
Khazix-Skills/
├── github-to-skills/          # Convert GitHub repos
to AI skills
├── skill-manager/             # Skill lifecycle management
└── skill-evolution-manager/   # Skill: improvement via user feedback
```

### Future Structure (Meta-Skills)

```
meta_skills/
├── core/                     # Core framework
│   ├── generator.py          # α-Generator base class
│   ├── optimizer.py          # Ω-Optimizer base class
│   ├── evolution_cycle.py    # Evolution cycle management
│   └── models/              # Data models
│       ├── skill.py       # Skill model
│       ├── evolution_record.py  # EvolutionRecord model
│       └── dependency_graph.py  # DependencyGraph
├── evolution/               # Evolution engine
│   ├── experience_store.py  # JSON-based storage
│   ├── feedback_processor.py
│   ├── session_analyzer.py
│   └── pattern_miner.py
├── loop/                    # Recursive self-optimization
│   ├── bootstrap.py        # Initial creation phase
│   ├── self_reflection.py  # Ω optimizes α phase
│   ├── generation.py       # α generates skills phase
│   └── recursive_loop.py   # Continuous evolution phase
├── cli.py                  # Command-line interface
└── tests/                  # pytest test suite
```

---

## Development Commands

```bash
# Install dependencies
pip install -r meta_skills/requirements.txt
pip install -r meta_skills/dev-requirements.txt

# Linting and formatting
ruff check .              # Run linting
ruff format .             # Auto-format
code

# Testing
pytest                    # Run all tests
pytest --cov=meta_skills --cov-report=term-missing  # With coverage
pytest -m unit            # Unit tests only
pytest -m integration     # Integration tests only
pytest -n auto           # Parallel execution

# Type checking (if needed)
mypy .
```

---

## Key Files

> NOTE: Coding standards and testing requirements are defined in `.claude/rules/`

- `memory-bank/project-spec.md` - Detailed project specifications
- `memory-bank/tech-stack.md` - Technology stack documentation
- `memory-bank/implementation-plan.md` - Implementation plan
- `memory-bank/architecture.md` - Architecture documentation
- `memory-bank/progress.md` - Progress tracking
- `元方法论.txt` - Meta-Methodology philosophy (Chinese)
- `memory-bank/` - Project knowledge base and progress tracking

---

## Memory Bank Convention

When working on this project, always update these files:

1. `memory-bank/progress.md` - Track implementation progress
2. `memory-bank/architecture.md` - Update architecture after major changes
3. `memory-bank/implementation-plan.md` - Reference for implementation phases

---

## Always Rules

> See `.claude/rules/memory-bank.md` for mandatory rules about reading and updating memory-bank files.
