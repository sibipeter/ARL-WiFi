import tracemalloc


def profile_memory() -> None:
    """
    Simple memory profiling utility.
    """
    tracemalloc.start()
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics("lineno")

    print("[ Top 10 memory-consuming lines ]")
    for stat in top_stats[:10]:
        print(stat)
