num = 0


def increment():
    global num
    num += 1


if __name__ == "__main__":
    import concurrent.futures
    import sys

    for si in [0.005, 0.0000005, 0.0000000005]:
        sys.setswitchinterval(si)
        results = []

        for attempt in range(100):
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
                for i in range(100):
                    pool.submit(increment)

            results.append(num)
            num = 0

        correct = [a for a in results if a == 100]
        pct = len(correct) / len(results)
        print(f"{pct:.1%} правильно при sys.setswitchinterval({si:.10f})")
