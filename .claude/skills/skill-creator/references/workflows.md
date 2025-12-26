# Workflow Patterns

Use these patterns when skills involve multi-step processes.

## Sequential Workflows

For complex tasks, provide an overview upfront:

```markdown
Filling a PDF form involves these steps:

1. Analyze the form (run analyze_form.py)
2. Create field mapping (edit fields.json)
3. Validate mapping (run validate_fields.py)
4. Fill the form (run fill_form.py)
5. Verify output (run verify_output.py)
```

## Conditional Workflows

Guide through decision points:

```markdown
1. Determine the modification type:
   **Creating new content?** → Follow "Creation workflow" below
   **Editing existing content?** → Follow "Editing workflow" below

2. Creation workflow: [steps]
3. Editing workflow: [steps]
```

## Decision Trees

For skills with multiple paths:

```markdown
## Workflow Decision Tree

┌─ User wants to READ document
│  └─ Extract text with python-docx
│
├─ User wants to CREATE document  
│  └─ Follow creation workflow
│
└─ User wants to EDIT document
   ├─ Simple edits → Direct XML modification
   └─ Tracked changes → See REDLINING.md
```
