filepath = 'c:/Users/aurel/OneDrive/Documents/BEcon_6243_Introduction_Programming/course_materials/week_03/ex03_git_collaboration.qmd'
content = open(filepath, 'r', encoding='utf-8').read()

# 1. Colors: Student B boxes -> callout-tip (dark green), keep 3-colon note for summary
content = content.replace(':::: {.callout-note}', ':::: {.callout-tip}')

# 2. Remove emojis from student headers
content = content.replace('## 🅰 Student A', '## Student A')
content = content.replace('## 🅱 Student B', '## Student B')

# 3. Fix overview: typo + de-AI
content = content.replace(
    '**Goal:** By the end of this exercise, you and your partner will share a GitHub repository, each working on your own branch, with a merged pull request in the history. **This is a typical workflow you will use for your group project, and it you can also use it for your other group projects in R or Python or any programming language.**',
    '**Goal:** By the end of this exercise, you and your partner share a GitHub repository, work on separate branches, and merge a pull request. **This is how your group project will work.**'
)

# 4. Remove AI preamble for Phase 2
content = content.replace(
    'In this part, we will set up the environment and generate a dataset using a simple python script. The script `generate_data.py` creates a CSV file with GDP data for a few countries:',
    'Student A sets up the environment. The script `generate_data.py` generates a small GDP dataset:'
)

# 5. Remove "In the repository," prefix
content = content.replace(
    '1. In the repository, create a virtual environment and install `pandas`:',
    '1. Create a virtual environment and install `pandas`:'
)

# 6. Fix the .gitignore instruction (wordy)
content = content.replace(
    '3. Using the terminal or a text editor, create a [.gitignore]{.path} that excludes the virtual environment. In the terminal, you can use `echo` like this:',
    '3. Create a [.gitignore]{.path} that excludes the virtual environment:'
)

# 7. Remove stray ::: (orphaned closing tag after the commit block)
content = content.replace(
    'git push\n\n\n\n:::\n\n::::',
    'git push\n\n::::'
)

# 8. Simplify uv sync note
content = content.replace(
    '> **Note:** `uv sync` recreates the virtual environment from [uv.lock]{.path}, reproducing the exact same environment that was started by Student A. You don\'t need to run `uv init` yourself.',
    '> **Note:** `uv sync` reads [uv.lock]{.path} and sets up the same environment as Student A — no need to run `uv init`.'
)

# 9. Simplify "run script" line
content = content.replace(
    '2. Run the data generation script, either directly with `uv run` or by running it from the script, choosing the right interpreter (like in the first exercise session):',
    '2. Run the script:'
)

# 10. Remove didactic "Remember from the lecture"
content = content.replace(
    '3. [gdp_data.csv]{.path} is now generated locally. Remember from the lecture: generated files should not be tracked. Add it to [.gitignore]{.path} and push:',
    '3. [gdp_data.csv]{.path} is generated locally — don\'t track it. Add it to [.gitignore]{.path} and push:'
)

# 11. Clean up Phase 2 checkpoint
content = content.replace(
    '**Checkpoint:** At this point, both students have [generate_data.py]{.path} and [.gitignore]{.path}. The CSV is generated locally but not tracked by Git. The .gitignore file is in sync.',
    '**Checkpoint:** Both students have [generate_data.py]{.path} and [.gitignore]{.path}. The CSV is local but not tracked.'
)

# 12. Remove verbose Files changed explanation
content = content.replace(
    '1. Open the Pull Request on GitHub and go to the **Files changed** tab. It gives you an overview of all the changes made on the branch that wants to be pulled. Check that only [generate_data.py]{.path} was modified.',
    '1. Open the Pull Request on GitHub → **Files changed** tab. Check that only [generate_data.py]{.path} was modified.'
)

# 13. Final checkpoint: remove corporate closing
content = content.replace(
    '**Checkpoint:** Student B\'s changes are in `main`. Both students are in sync. The full collaborative workflow is complete.',
    '**Checkpoint:** Student B\'s changes are in `main`. Both students are in sync.'
)

# 14. Shorten summary opener
content = content.replace(
    'You have practised the core collaborative Git workflow:',
    'Commands used in this exercise:'
)

# 15. Shorten final callout
content = content.replace(
    'From now on, this is the workflow you will use for your group project: each team member works on their own branch and contributes changes via pull requests.',
    'This is the workflow for your group project.'
)

open(filepath, 'w', encoding='utf-8').write(content)
print('Done.')
