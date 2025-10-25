# GOIT ALGO2 HW-02 — Greedy Algorithms & Dynamic Programming

## Overview

This repository contains two independent tasks:

- **Task 1 (Greedy):** Optimize a 3D printer queue subject to priorities and printer constraints.
- **Task 2 (Dynamic Programming):** Solve the Rod Cutting problem using **memoization** (top-down) and **tabulation** (bottom-up).

Both tasks match the acceptance criteria from the assignment.

---

## Task 1 — 3D Printer Queue (Greedy)

**Function**

```python
optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict
# Returns: {"print_order": ["M1", "M2", ...], "total_time": int}


## Inputs
print_jobs = [
  {"id": str, "volume": float, "priority": int, "print_time": int}, ...
]
constraints = {
  "max_volume": float,
  "max_items": int
}

## Priorities
1 = highest (Coursework/Theses)

2 = Lab Work

3 = Personal Projects

## Greedy batching strategy

Repeatedly start a new batch with the next unscheduled highest-priority job (ties by id for determinism).

Try to fill the batch with other jobs that fit (max_volume, max_items), preferring:

jobs that do not increase the batch time (where batch time is max(print_time) in the batch),

then the smallest time increase,

then higher priority (lower number),

then smaller print_time,

then lexicographically smaller id.

Batch time = max(print_time) within that batch.
Total time = sum of all batch times.

print_order lists jobs in their final scheduled order (across batches).

## Data classes used: PrintJob, PrinterConstraints
## Complexity: up to O(n²) time, O(n) extra space.



## Task 2 — Rod Cutting (Dynamic Programming)

Functions
rod_cutting_memo(length: int, prices: List[int]) -> Dict
rod_cutting_table(length: int, prices: List[int]) -> Dict
# Both return:
# {
#   "max_profit": int,
#   "cuts": List[int],        # e.g., [2,2,1] means pieces of lengths 2,2,1
#   "number_of_cuts": int     # len(cuts) - 1
# }

## Input rules

length > 0

len(prices) == length

All prices[i] > 0

prices[i] is the price of a rod of length i+1.

Tie-breaking

Memoization (top-down): tries piece sizes 1..L and keeps the first optimal it encounters
→ tends to produce results like [1, 2, 2] for length 5.

Tabulation (bottom-up): if profit ties, prefer more pieces, then larger first cut for determinism
→ tends to produce [2, 2, 1] for length 5.

Complexity:

Memoization: O(n²) time, O(n) space

Tabulation: O(n²) time, O(n) space

## Project Structure

goit-algo2-hw-02/
├─ src/
│  └─ algorithms_hw2.py         # Task 1 + Task 2 implementations
├─ tests/
│  └─ test_hw2.py               # Pytest tests (optional but recommended)
├─ main.py                      # Demo runner that prints expected outputs
├─ pytest.ini                   # Ensures imports work from src/
└─ README.md

## Example Output (matches expected)

Test 1 (same priority):
Print order: ['M1', 'M2', 'M3']
Total time: 270 minutes

Test 2 (different priorities):
Print order: ['M2', 'M1', 'M3']
Total time: 270 minutes

Test 3 (exceeding constraints):
Print order: ['M1', 'M2', 'M3']
Total time: 450 minutes

Test: Base case
...
Memoization Result: max=12, cuts=[1, 2, 2], number_of_cuts=2
Tabulation Result: max=12, cuts=[2, 2, 1], number_of_cuts=2

## Submission

Create public repository goit-algo2-hw-02.

Push the project files.

Zip the working files as HW2_FullName.zip (exclude .venv/, __pycache__/, .pytest_cache/).

Attach the ZIP and the repository link in LMS.

## Notes / Acceptance Criteria Mapping

✅ Groups models without exceeding constraints (max_volume, max_items).

✅ Higher priorities are processed first.

✅ Batch time = max job time in the group; total = sum of batch times.

✅ Handles scenarios: same priority, mixed priorities, exceeding constraints.

✅ Uses @dataclass for data structures in Task 1.



```
