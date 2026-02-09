# Memory Bank - 始终规则

IMPORTANT: These rules MUST always be followed before/after code operations.

## Before Writing Code

CRITICAL: Always read the following files BEFORE writing any code:
- `memory-bank/architecture.md` - Include entire database schema
- `memory-bank/implementation-plan.md` - Reference for implementation phases

These files provide essential context about:
- Current architecture and design decisions
- Database schema and data models
- Implementation progress and next steps
- Dependencies between components

## After Major Changes

After adding a major feature or completing a milestone, update:
- `memory-bank/architecture.md` - Document any architectural changes
- `memory-bank/progress.md` - Track implementation progress

Examples of major changes:
- Adding a new core module or component
- Modifying the database schema
- Changing the architecture of existing systems
- Completing a phase from implementation-plan.md

## When Memory Bank Not Exists

If memory-bank directory does not exist yet:
- Proceed with current task
- Note that memory-bank will be created in future phases
- Consider creating initial memory-bank structure when appropriate
