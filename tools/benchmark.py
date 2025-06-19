import importlib
import time
import json
import argparse
from pathlib import Path


WARMUPS = 3  # It's better to have more iterations but we're short in time.


def benchmark_function(module_name, function_name, output_file, *args, **kwargs):
    # Dynamically import module
    module = importlib.import_module(module_name)
    func = getattr(module, function_name)

    print("Warming up...", end="", flush=True)
    for i in range(WARMUPS):
        print(f" {WARMUPS - i}...", end="", flush=True)
        func(*args, **kwargs)
    print(" done.", flush=True)

    # Benchmark
    print("Running benchmark...", flush=True)
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    duration = end - start

    # Save result
    data = {"module": module_name, "function": function_name, "execution_time_seconds": duration}
    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Benchmarked {module_name}.{function_name} in {duration:.6f} seconds.")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Benchmark a function and save result.")
    parser.add_argument("module", help="Module name (without .py)")
    parser.add_argument("function", help="Function name")
    parser.add_argument("output", help="Output JSON file")

    args = parser.parse_args()
    benchmark_function(args.module, args.function, args.output)
