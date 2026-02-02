# – Git & GitHub Practical Assignment (with Python Data Quality Tool)

This task is designed **Git & GitHub through real coding work**, not just commands.
Interns will build a **Python-based Data Quality Tool** and manage it using **individual and team Git workflows**.

---

## 🎯 Objective

To learn the practical, industry-style use of Git and GitHub—from individual development to team collaboration.
The goal of this task is to ensure interns can:

Use Git with real Python code

Handle branching, merge conflicts, and pull requests in real development scenarios

Collaborate effectively within a team using workflows commonly followed in software companies
---------------------------------------------------------------------------------------------

🧠 Project Overview (What You Will Build)
Each will work on a Python-based Data Quality Tool that:

Reads data from a CSV file

Runs multiple data quality checks

Generates a structured data quality report

Tool Features (Core Logic)

The tool must include the following features:

Missing values check

Duplicate rows detection

Outlier detection for numeric columns

Basic schema validation

Outputs:

quality_report.json

A clear console summary

⚠️ No Machine Learning is involved in this task.

---

## 📁 Base Project Structure (Required)

```
data_quality_tool/
  data/
    sample.csv
  src/
    loader.py
    checks.py
    reporter.py
  README.md
```

---

## 🔹 Phase 1: Git Basics + Python Tool (Individual)

Tasks

Install and configure Git

Create a GitHub account and a personal repository

Initialize a local repository (git init)

Build a basic version of the Python Data Quality Tool:

Load a CSV file

Perform missing values and duplicate checks

Commit code in small, logical steps, for example:

Commit 1: project structure and README

Commit 2: CSV loading logic

Commit 3: missing and duplicate checks

Push the repository to GitHub

Git Commands Used

init

status

add

commit

log

push

Deliverable

Personal GitHub repository link

Commit history showing multiple meaningful commits

## 🔹 Phase 2: Branching & Conflict Handling (Individual)

Tasks

Create a new branch (e.g., feature-outliers)

In the main branch:

Add a new logic in checks.py (e.g., schema validation)

In the feature branch:

Add outlier detection in the same section of checks.py

Merge the branches to intentionally create a merge conflict

Resolve the conflict manually

Commit the resolved code and merge the branch into main

README Update

Add a short explanation in the README:

What conflict occurred and how it was resolved

Git Concepts Used

branch

checkout / switch

merge

conflict resolution

Deliverable

Same repository containing:

At least 2 branches

A merge commit

Evidence of conflict resolution


A merge conflict occurred because both branches modified the same function in `checks.py`.

The conflict was resolved by manually combining the logic from both branches.

## 🔹 Phase 3: Team Git Workflow + Feature Development (Group of 3)

Setup

One intern creates a group GitHub repository

The other two interns are added as collaborators

Direct pushes to the main branch are not allowed

Feature Branch Responsibilities

Each intern must work on their own feature branch:

Intern A → feature-missing-summary

Column-wise missing percentage calculation

Intern B → feature-outlier-report

Outlier count per numeric column

Intern C → feature-reporting

Improve the JSON report structure

Collaboration Rules

All features must be submitted via Pull Requests

At least one teammate review is required before merging

Clear and meaningful commit messages are mandatory

Git Concepts Used

Feature branches

Pull Requests

Code reviews

Merge via Pull Request only

Deliverable

Group GitHub repository link

Evidence of:

Multiple branches

Pull Requests

Reviews

Merge history
