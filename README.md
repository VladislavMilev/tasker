# Jira Task Creator from Test Cases

This project automates the creation of Jira tasks based on test cases. It streamlines the process by copying data from a reference task and generating a new one with updated information.

## 📋 How It Works

1. Create a **reference task** in Jira.  
   This task will be used to copy predefined fields such as:
   - Estimate  
   - Epic Link  
   - Assignee  
   - ...and more.

2. A new task will be created with:
   - A **custom title**
   - The **URL of the test case** placed in the description

---

## ⚙️ Setup

### 1. Create a `.env` file in the project root with the following variables:

```env
LOGIN_USERNAME=
LOGIN_PASSWORD=
REFERENCE_TASK=
```
---
## 🧪 Test Case Configuration

In the `main.py` file, specify the test cases you want to create tasks for using the `TESTCASE_TO_CREATE` variable.

```python
TESTCASE_TO_CREATE = ["ATC-123", "ATC-456", "ATC-789"]
```

⚠️ Note: Use ticket numbers, not full URLs.
For example, use ATC-123 instead of https://your.jira.com/browse/ATC-123.