# Output Patterns

Use these patterns when skills need consistent, high-quality output.

## Template Pattern

Provide templates for output format. Match strictness to your needs.

**For strict requirements (API responses, data formats):**

```markdown
## Report structure

ALWAYS use this exact template:

# [Analysis Title]

## Executive summary
[One-paragraph overview of key findings]

## Key findings
- Finding 1 with supporting data
- Finding 2 with supporting data

## Recommendations
1. Specific actionable recommendation
2. Specific actionable recommendation
```

**For flexible guidance (when adaptation is useful):**

```markdown
## Report structure

Sensible default format—use judgment:

# [Analysis Title]
## Executive summary
## Key findings
## Recommendations

Adjust sections as needed for the specific analysis.
```

## Examples Pattern

For skills where output quality depends on seeing examples:

```markdown
## Commit message format

Generate commit messages following these examples:

**Example 1:**
Input: Added user authentication with JWT tokens
Output:
```
feat(auth): implement JWT-based authentication

Add login endpoint and token validation middleware
```

**Example 2:**
Input: Fixed bug where dates displayed incorrectly
Output:
```
fix(reports): correct date formatting in timezone conversion

Use UTC timestamps consistently across report generation
```

Follow: type(scope): brief description, then detailed explanation.
```

Examples help Claude understand desired style better than descriptions alone.
