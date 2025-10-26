import concurrent.futures as cf
import time
from statistics import mean, median


def op_register_device(i):
    t0 = time.perf_counter()
    ok = True
    time.sleep(0.01)  # replace with real operation
    return ok, time.perf_counter() - t0


OPS = {
    "register_device": op_register_device,
}


def run_load(op_name, total=1000, workers=8):
    fn = OPS[op_name]
    durations, failures = [], 0
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(fn, i) for i in range(total)]
        for f in cf.as_completed(futures):
            ok, dur = f.result()
            durations.append(dur)
            failures += 0 if ok else 1
    return {
        "op": op_name,
        "total": total,
        "workers": workers,
        "throughput_ops_per_s": total / sum(durations),
        "latency_mean_s": mean(durations),
        "latency_median_s": median(durations),
        "failures": failures,
    }


if __name__ == "__main__":
    metrics = run_load("register_device", total=2000, workers=16)
    print(metrics)
