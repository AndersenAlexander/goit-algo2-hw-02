from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional


# ----------------------------
# Task 1 — Greedy: 3D Printer
# ----------------------------

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int


@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Optimises the 3D printing queue according to priorities and printer constraints.

    Greedy strategy:
      • Always start a batch with the highest-priority remaining job.
      • Fill the batch with any other jobs (same or lower priority) that fit
        volume/items constraints, preferring those that don't increase the batch time.
      • If all remaining candidates would increase the batch time, choose the one
        that increases it the least (then prefer higher priority, smaller time, id).

    Notes:
      • This allows mixing lower priorities in an earlier batch WITHOUT delaying
        the higher-priority pivot job.
      • The returned print_order lists jobs in the scheduled (batch) order.
      • Batch time = max(print_time) inside the batch.
      • Total time = sum(batch times).
      • Time: O(n^2) worst-case (n jobs), Space: O(n)

    Args:
        print_jobs: list of dicts: {"id": str, "volume": float, "priority": int, "print_time": int}
        constraints: {"max_volume": float, "max_items": int}

    Returns:
        {"print_order": [ids...], "total_time": int}
    """
    # Parse & validate
    jobs: List[PrintJob] = []
    for j in print_jobs:
        job = PrintJob(
            id=str(j["id"]),
            volume=float(j["volume"]),
            priority=int(j["priority"]),
            print_time=int(j["print_time"]),
        )
        if job.volume <= 0 or job.print_time <= 0:
            raise ValueError("Job volume and print_time must be > 0.")
        jobs.append(job)

    cons = PrinterConstraints(
        max_volume=float(constraints["max_volume"]),
        max_items=int(constraints["max_items"]),
    )
    if cons.max_volume <= 0 or cons.max_items <= 0:
        raise ValueError("Invalid printer constraints.")

    # Deterministic base ordering: by priority asc, then id asc
    jobs_sorted = sorted(jobs, key=lambda x: (x.priority, x.id))
    scheduled = {job.id: False for job in jobs_sorted}

    total_time = 0
    print_order: List[str] = []

    while not all(scheduled.values()):
        # Pivot = next unscheduled job with highest priority (lowest number), id asc
        pivot: Optional[PrintJob] = None
        for job in jobs_sorted:
            if not scheduled[job.id]:
                pivot = job
                break
        assert pivot is not None

        group_ids = [pivot.id]
        group_time = pivot.print_time
        used_volume = pivot.volume
        used_items = 1
        scheduled[pivot.id] = True

        # Fill current batch greedily within constraints
        while used_items < cons.max_items:
            candidates = []
            for job in jobs_sorted:
                if scheduled[job.id]:
                    continue
                if used_volume + job.volume > cons.max_volume:
                    continue
                new_group_time = max(group_time, job.print_time)
                increase = new_group_time - group_time
                # Prefer: (no time increase) → smaller increase → higher priority → smaller time → id
                candidates.append((increase > 0, increase, job.priority, job.print_time, job.id, job))

            if not candidates:
                break

            candidates.sort(key=lambda t: (t[0], t[1], t[2], t[3], t[4]))
            chosen = candidates[0][5]

            group_time = max(group_time, chosen.print_time)
            used_volume += chosen.volume
            used_items += 1
            group_ids.append(chosen.id)
            scheduled[chosen.id] = True

        print_order.extend(group_ids)
        total_time += group_time

    return {"print_order": print_order, "total_time": total_time}


# ---------------------------------------
# Task 2 — DP: Rod Cutting (memo + table)
# ---------------------------------------

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Top-down DP with memoization.
    Tie-breaks keep the *first* optimal choice encountered (piece sizes tried 1..L),
    so for ties it prefers smaller pieces earlier (e.g., [1,2,2] for length 5).

    Returns:
        {"max_profit": int, "cuts": List[int], "number_of_cuts": int}
    """
    if length <= 0:
        raise ValueError("length must be > 0")
    if len(prices) != length:
        raise ValueError("prices length must equal rod length")
    if any(p <= 0 for p in prices):
        raise ValueError("all prices must be > 0")

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def best(L: int) -> Tuple[int, Tuple[int, ...]]:
        if L == 0:
            return 0, tuple()
        best_val = -10**9
        best_cuts: Tuple[int, ...] = tuple()
        # try piece sizes ascending: 1..L (keeps earliest optimal)
        for s in range(1, L + 1):
            val, cuts = best(L - s)
            val += prices[s - 1]
            if val > best_val:  # strict > keeps first tie
                best_val = val
                best_cuts = (s,) + cuts
        return best_val, best_cuts

    max_profit, cuts_tuple = best(length)
    cuts = list(cuts_tuple)
    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": max(0, len(cuts) - 1),
    }


def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Bottom-up DP (tabulation).
    Tie-breaks:
      1) Maximise profit
      2) If profits tie, prefer the option with *more pieces* (so you get [2,2,1] for length 5)
      3) If still tied, prefer larger first cut (stable deterministic result)

    Returns:
        {"max_profit": int, "cuts": List[int], "number_of_cuts": int}
    """
    if length <= 0:
        raise ValueError("length must be > 0")
    if len(prices) != length:
        raise ValueError("prices length must equal rod length")
    if any(p <= 0 for p in prices):
        raise ValueError("all prices must be > 0")

    dp = [0] * (length + 1)          # best profit for length j
    first_cut = [0] * (length + 1)   # first piece to take for length j
    pieces = [0] * (length + 1)      # number of pieces in that optimal solution

    for j in range(1, length + 1):
        best_val = -10**9
        best_s = 0
        best_pieces = -10**9
        for s in range(1, j + 1):
            candidate = prices[s - 1] + dp[j - s]
            pcs = 1 + pieces[j - s]
            if (candidate > best_val or
                (candidate == best_val and pcs > best_pieces) or
                (candidate == best_val and pcs == best_pieces and s > best_s)):
                best_val = candidate
                best_s = s
                best_pieces = pcs
        dp[j] = best_val
        first_cut[j] = best_s
        pieces[j] = best_pieces

    cuts: List[int] = []
    j = length
    while j > 0:
        s = first_cut[j]
        cuts.append(s)
        j -= s

    return {
        "max_profit": dp[length],
        "cuts": cuts,
        "number_of_cuts": max(0, len(cuts) - 1),
    }
