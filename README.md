# GOIT ALGO2 HW-02 — Greedy Algorithms & Dynamic Programming

## Overview
This repository contains two independent tasks:

- **Task 1 (Greedy):** Optimize a 3D printer queue subject to priorities and printer constraints.
- **Task 2 (Dynamic Programming):** Solve the Rod Cutting problem using **memoization** (top-down) and **tabulation** (bottom-up).

Both tasks follow the acceptance criteria from the assignment.

---

## Task 1 — 3D Printer Queue (Greedy)

## Function
```python
optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict
# Returns: {"print_order": ["M1", "M2", ...], "total_time": int}


# Inputs
print_jobs = [
  {"id": "M1", "volume": 100.0, "priority": 1, "print_time": 120},
  {"id": "M2", "volume": 150.0, "priority": 2, "print_time": 90},
  {"id": "M3", "volume": 120.0, "priority": 3, "print_time": 150},
]

constraints = {
  "max_volume": 300.0,
  "max_items": 2
}

Priorities

1 = highest (Coursework/Theses)
2 = Lab Work
3 = Personal Projects

Greedy Batching Strategy

Start each batch with the next unscheduled highest-priority job (ties by id).

Fill the batch with jobs that fit (max_volume, max_items), preferring:

jobs that do not increase the batch time (max(print_time) in the batch),

then the smallest time increase,

then higher priority (lower number),

then smaller print_time,

then lexicographically smaller id.

Batch time = max(print_time) in the batch. Total time = sum of batch times.

print_order lists jobs in final scheduled (batch) order.

Data Classes Used

PrintJob, PrinterConstraints (via @dataclass).

Complexity

Time: up to O(n²), Space: O(n).

Task 2 — Rod Cutting (Dynamic Programming)
Functions
rod_cutting_memo(length: int, prices: List[int]) -> Dict
rod_cutting_table(length: int, prices: List[int]) -> Dict
# Both return:
# {
#   "max_profit": int,
#   "cuts": List[int],        # e.g., [2, 2, 1] means pieces 2, 2, 1
#   "number_of_cuts": int     # len(cuts) - 1
# }

Input Rules

length > 0

len(prices) == length

All prices[i] > 0

prices[i] is the price of a rod of length i+1.

Tie-Breaking

Memoization (top-down): tries piece sizes 1..L and keeps the first optimal → often [1, 2, 2] for length 5.

Tabulation (bottom-up): on ties prefer more pieces, then larger first cut → often [2, 2, 1] for length 5.

Complexity

Memoization: O(n²) time, O(n) space
Tabulation: O(n²) time, O(n) space

Project Structure
goit-algo2-hw-02/
├─ src/
│  └─ algorithms_hw2.py         # Task 1 + Task 2 implementations
├─ tests/
│  └─ test_hw2.py               # Pytest tests (optional but recommended)
├─ main.py                      # Demo runner printing expected outputs
├─ pytest.ini                   # Ensures imports work from src/
└─ README.md

Setup & Run
1) Create and activate a virtual environment (recommended)

Windows (PowerShell)

py -3.12 -m venv .venv
. .\.venv\Scripts\Activate.ps1


macOS / Linux

python3 -m venv .venv
source .venv/bin/activate

2) Run the demo
python main.py


You should see the same outputs as in the assignment’s Expected Result section.

3) Run automated tests (pytest)

Install pytest (once):

python -m pip install -U pip pytest


Run tests:

pytest -q


If you get ModuleNotFoundError: src, run once:

# Windows PowerShell
$env:PYTHONPATH = "$PWD"
python -m pytest -q

Example Output (Expected)
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
Rod Length: 5
Prices: [2, 5, 7, 8, 10]

Memoization Result:
Maximum Profit: 12
Cuts: [1, 2, 2]
Number of Cuts: 2

Tabulation Result:
Maximum Profit: 12
Cuts: [2, 2, 1]
Number of Cuts: 2

Test passed successfully!

Test: Optimal to not cut
Rod Length: 3
Prices: [1, 3, 8]

Memoization Result:
Maximum Profit: 8
Cuts: [3]
Number of Cuts: 0

Tabulation Result:
Maximum Profit: 8
Cuts: [3]
Number of Cuts: 0

Test passed successfully!

Test: Even Cuts
Rod Length: 4
Prices: [3, 5, 6, 7]

Memoization Result:
Maximum Profit: 12
Cuts: [1, 1, 1, 1]
Number of Cuts: 3

Tabulation Result:
Maximum Profit: 12
Cuts: [1, 1, 1, 1]
Number of Cuts: 3

Test passed successfully!

Submission

Create public repository goit-algo2-hw-02.

Push the project files.

Zip the working files as HW2_FullName.zip (exclude .venv/, __pycache__/, .pytest_cache/).

Attach the ZIP and the repository link in LMS.

Acceptance Criteria Checklist

✅ Groups models without exceeding constraints (max_volume, max_items).

✅ Higher priorities are processed first.

✅ Batch time = max job time in the group; total time = sum of batch times.

✅ Handles scenarios: same priority, mixed priorities, exceeding constraints.

✅ Uses @dataclass for data structures in Task 1.


