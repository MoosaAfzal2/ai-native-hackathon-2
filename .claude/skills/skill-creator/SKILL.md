---
name: skill-creator
description: Create, write, author, or design Agent Skills for Claude Code. Use when users want to create a new skill, update an existing skill, write SKILL.md files, design skill structure, troubleshoot skill discovery, or convert prompts/workflows into reusable Skills.
---

# Skill Creator

Create effective Agent Skills that extend Claude's capabilities with specialized knowledge, workflows, and tool integrations.

## Core Principles

### Concise is Key

The context window is a public good. Skills share it with system prompts, conversation history, other skills, and user requests.

**Default assumption: Claude is already very smart.** Only add context Claude doesn't have. Challenge each piece: "Does Claude need this?" and "Does this justify its token cost?"

Prefer concise examples over verbose explanations.

### Set Appropriate Degrees of Freedom

Match specificity to task fragility:

- **High freedom** (text instructions): Multiple valid approaches, context-dependent decisions
- **Medium freedom** (pseudocode/parameterized scripts): Preferred pattern exists, variation acceptable
- **Low freedom** (specific scripts, few parameters): Fragile operations, consistency critical

Think of a narrow bridge with cliffs (low freedom) vs. an open field (high freedom).

## Skill Structure

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name + description)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/     - Executable code for deterministic tasks
    ├── references/  - Documentation loaded as needed
    └── assets/      - Templates, icons, fonts for output
```

### Frontmatter Rules

```yaml
---
name: skill-name
description: What it does + when to use it + trigger words
---
```

**name requirements:**
- Lowercase letters, numbers, hyphens only
- Max 64 characters
- Must match directory name
- ✅ `pdf-processor`, `git-commit-helper`
- ❌ `PDF_Processor`, `Git Commits!`

**description formula:** `[What it does] + [When to use it] + [Key triggers]`

✅ Good:
```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

❌ Too vague:
```yaml
description: Helps with documents
```

**Tips:**
- Include file extensions (.pdf, .xlsx, .json)
- Use common user phrases ("analyze", "extract", "generate")
- Add context clues ("Use when...")
- Max 1024 characters

### Optional frontmatter

```yaml
allowed-tools: Read, Grep, Glob  # Restrict tool access for read-only skills
```

## Creation Process

### Step 1: Understand with Concrete Examples

Ask clarifying questions:
- What specific capability should this Skill provide?
- What would a user say that should trigger this skill?
- What tools or resources does it need?

Keep it focused: One Skill = one capability.
- ✅ "PDF form filling", "Excel data analysis"
- ❌ "Document processing", "Data tools"

### Step 2: Plan Reusable Contents

Analyze each example to identify:
- **scripts/**: Code rewritten repeatedly or needing deterministic reliability
- **references/**: Documentation Claude should reference while working
- **assets/**: Files used in output (templates, boilerplate)

### Step 3: Initialize the Skill

For new skills, run:

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

Creates template with SKILL.md, example directories, and placeholder files.

**Choose location:**
- Personal: `~/.claude/skills/` (individual workflows)
- Project: `.claude/skills/` (team workflows, committed to git)

### Step 4: Edit the Skill

#### Write for Claude, not humans

Include information beneficial and non-obvious to Claude. Consider what procedural knowledge, domain details, or assets would help.

#### SKILL.md Body Structure

```markdown
# Skill Name

Brief overview (one sentence).

## Quick start

Simple example to get started immediately.

## Instructions

Step-by-step guidance:
1. First step with clear action
2. Second step with expected outcome
3. Handle edge cases

## Examples

Concrete usage with code or commands.

## Requirements

Dependencies or prerequisites.
```

#### Use Progressive Disclosure

Keep SKILL.md under 500 lines. Reference detailed content:

```markdown
## Advanced features

- **Form filling**: See [FORMS.md](references/forms.md)
- **API reference**: See [REFERENCE.md](references/reference.md)
```

For design patterns, consult:
- **Multi-step processes**: See [references/workflows.md](references/workflows.md)
- **Output formats**: See [references/output-patterns.md](references/output-patterns.md)

### Step 5: Package the Skill

```bash
scripts/package_skill.py <path/to/skill-folder>
```

Validates and creates distributable `.skill` file.

### Step 6: Iterate

1. Use the skill on real tasks
2. Notice struggles or inefficiencies
3. Update SKILL.md or bundled resources
4. Test again

## What NOT to Include

Never create extraneous files:
- README.md
- INSTALLATION_GUIDE.md
- CHANGELOG.md

Skills are for AI agents, not humans. No auxiliary documentation.

## Common Patterns

### Read-only Skill

```yaml
---
name: code-reader
description: Read and analyze code without making changes. Use for code review, understanding codebases, or documentation.
allowed-tools: Read, Grep, Glob
---
```

### Script-based Skill

```yaml
---
name: data-processor
description: Process CSV and JSON data files with Python scripts. Use when analyzing data files or transforming datasets.
---

# Data Processor

## Instructions

1. Process with:
   ```bash
   python scripts/process.py input.csv --output results.json
   ```

2. Validate:
   ```bash
   python scripts/validate.py results.json
   ```
```

### Multi-file Progressive Disclosure

```yaml
---
name: api-designer
description: Design REST APIs following best practices. Use when creating API endpoints, designing routes, or planning API architecture.
---

# API Designer

Quick start: See [examples.md](references/examples.md)
Detailed reference: See [reference.md](references/reference.md)
```

## Validation Checklist

✅ **Structure**:
- [ ] SKILL.md exists in skill directory
- [ ] Directory name matches frontmatter `name`

✅ **Frontmatter**:
- [ ] `---` on line 1, closing `---` before content
- [ ] Valid YAML (no tabs, correct indentation)
- [ ] `name`: lowercase, hyphens, max 64 chars
- [ ] `description`: specific, < 1024 chars, includes "what" + "when"

✅ **Content**:
- [ ] Instructions are step-by-step
- [ ] Concrete examples provided
- [ ] Edge cases handled
- [ ] Dependencies listed

✅ **Testing**:
- [ ] Skill activates on relevant queries
- [ ] Claude follows instructions correctly

## Troubleshooting

**Skill doesn't activate:**
- Make description more specific with trigger words
- Include file types and operations
- Add "Use when..." clause

**Multiple Skills conflict:**
- Make descriptions more distinct
- Narrow the scope of each Skill

**Skill has errors:**
- Check YAML syntax (no tabs, proper indentation)
- Verify file paths (use forward slashes)
- Ensure scripts have execute permissions
