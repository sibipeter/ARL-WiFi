import tracemalloc


def run_target():
    import app

    if hasattr(app, "main"):
        app.main()


if __name__ == "__main__":
    tracemalloc.start(25)
    run_target()
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics("lineno")
    for stat in top_stats[:50]:
        print(stat)
