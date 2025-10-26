import time


def run_load_test(duration: int) -> None:
    """
    Run a simple load test for the given duration in seconds.
    """
    start = time.time()
    while time.time() - start < duration:
        pass


def main() -> None:
    run_load_test(1)


if __name__ == "__main__":
    main()
