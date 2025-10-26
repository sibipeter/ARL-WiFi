import cProfile
import pstats


def profile_cpu() -> None:
    """
    Simple CPU profiling utility.
    """
    profiler = cProfile.Profile()
    profiler.enable()

    # Placeholder workload
    for _ in range(1000000):
        pass

    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats("cumtime")
    stats.print_stats(10)
