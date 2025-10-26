import cProfile
import io
import pstats


def run_target():
    import app

    if hasattr(app, "main"):
        app.main()


if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()
    run_target()
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("cumtime")
    ps.print_stats(50)
    print(s.getvalue())
