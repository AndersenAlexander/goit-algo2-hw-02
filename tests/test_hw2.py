from src.algorithms_hw2 import optimize_printing, rod_cutting_memo, rod_cutting_table

def test_task1_same_priority():
    jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150},
    ]
    constraints = {"max_volume": 300, "max_items": 2}
    r = optimize_printing(jobs, constraints)
    assert r["print_order"] == ["M1", "M2", "M3"]
    assert r["total_time"] == 270

def test_task1_diff_priorities():
    jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150},
    ]
    constraints = {"max_volume": 300, "max_items": 2}
    r = optimize_printing(jobs, constraints)
    assert r["print_order"] == ["M2", "M1", "M3"]
    assert r["total_time"] == 270

def test_task1_exceeding():
    jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120},
    ]
    constraints = {"max_volume": 300, "max_items": 2}
    r = optimize_printing(jobs, constraints)
    assert r["print_order"] == ["M1", "M2", "M3"]
    assert r["total_time"] == 450

def test_rod_base_case():
    length, prices = 5, [2, 5, 7, 8, 10]
    memo = rod_cutting_memo(length, prices)
    table = rod_cutting_table(length, prices)
    assert memo["max_profit"] == 12 and memo["cuts"] == [1, 2, 2] and memo["number_of_cuts"] == 2
    assert table["max_profit"] == 12 and table["cuts"] == [2, 2, 1] and table["number_of_cuts"] == 2

def test_rod_no_cut():
    length, prices = 3, [1, 3, 8]
    memo = rod_cutting_memo(length, prices)
    table = rod_cutting_table(length, prices)
    assert memo == {"max_profit": 8, "cuts": [3], "number_of_cuts": 0}
    assert table == {"max_profit": 8, "cuts": [3], "number_of_cuts": 0}

def test_rod_even_cuts():
    length, prices = 4, [3, 5, 6, 7]
    memo = rod_cutting_memo(length, prices)
    table = rod_cutting_table(length, prices)
    assert memo == {"max_profit": 12, "cuts": [1, 1, 1, 1], "number_of_cuts": 3}
    assert table == {"max_profit": 12, "cuts": [1, 1, 1, 1], "number_of_cuts": 3}
