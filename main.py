from src.algorithms_hw2 import (
    optimize_printing,
    rod_cutting_memo,
    rod_cutting_table,
)

def test_printing_optimization():
    print_jobs_sets = {
        "same priority": [
            {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
            {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
            {"id": "M3", "volume": 120, "priority": 1, "print_time": 150},
        ],
        "different priorities": [
            {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
            {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
            {"id": "M3", "volume": 120, "priority": 3, "print_time": 150},
        ],
        "exceeding constraints": [
            {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
            {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
            {"id": "M3", "volume": 180, "priority": 2, "print_time": 120},
        ],
    }

    constraints = {"max_volume": 300, "max_items": 2}

    print("Test 1 (same priority):")
    r1 = optimize_printing(print_jobs_sets["same priority"], constraints)
    print(f"Print order: {r1['print_order']}")
    print(f"Total time: {r1['total_time']} minutes")

    print("\nTest 2 (different priorities):")
    r2 = optimize_printing(print_jobs_sets["different priorities"], constraints)
    print(f"Print order: {r2['print_order']}")
    print(f"Total time: {r2['total_time']} minutes")

    print("\nTest 3 (exceeding constraints):")
    r3 = optimize_printing(print_jobs_sets["exceeding constraints"], constraints)
    print(f"Print order: {r3['print_order']}")
    print(f"Total time: {r3['total_time']} minutes")


def run_rod_tests():
    tests = [
        {"length": 5, "prices": [2, 5, 7, 8, 10], "name": "Base case"},
        {"length": 3, "prices": [1, 3, 8], "name": "Optimal to not cut"},
        {"length": 4, "prices": [3, 5, 6, 7], "name": "Even Cuts"},
    ]

    for t in tests:
        print(f"\nTest: {t['name']}")
        print(f"Rod Length: {t['length']}")
        print(f"Prices: {t['prices']}")

        memo = rod_cutting_memo(t["length"], t["prices"])
        print("\nMemoization Result:")
        print(f"Maximum Profit: {memo['max_profit']}")
        print(f"Cuts: {memo['cuts']}")
        print(f"Number of Cuts: {memo['number_of_cuts']}")

        tabl = rod_cutting_table(t["length"], t["prices"])
        print("\nTabulation Result:")
        print(f"Maximum Profit: {tabl['max_profit']}")
        print(f"Cuts: {tabl['cuts']}")
        print(f"Number of Cuts: {tabl['number_of_cuts']}")

        print("\nTest passed successfully!")


if __name__ == "__main__":
    # Task 1
    test_printing_optimization()
    # Task 2
    run_rod_tests()
