# GOIT ALGO2 HW-02 — Greedy Algorithms & Dynamic Programming

## Overview
This repository contains two independent tasks:

- **Task 1 (Greedy):** Optimize a 3D printer queue subject to priorities and printer constraints.
- **Task 2 (Dynamic Programming):** Solve the Rod Cutting problem using **memoization** (top-down) and **tabulation** (bottom-up).

Both tasks follow the acceptance criteria from the assignment.

---

## Task 1 — 3D Printer Queue (Greedy)

### Function
```python
optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict
# Returns: {"print_order": ["M1", "M2", ...], "total_time": int}
