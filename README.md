# perfbasics
Materials for my "Writing Faster Code: Profiling and Performance Basics" talk in 0xDeusto, 2025-06-24.

## Setup

I recommend using virtual environments if possible, but it's not compulsory.

Install the dependencies with:

```shell
pip install -r requirements.txt
```

## Running Benchmarks

Run a benchmark in a file with:

```shell
python benchmark.py <module> <function> out/<output>.json
```

Where:
- `<module>` is the name of the module containing the function to benchmark.
- `<function>` is the name of the function to benchmark.
- `<output>.json` is the name of the JSON file where the benchmark results will be saved.

For example,

```
python3 -m tools.benchmark lab.matrices iterate_by_row out/row.json
```

Or

```
python3 -m tools.benchmark lab.matrices iterate_by_column out/column.json
```

Then compare the results with

```shell
python3 -m tools.compare row.json column.json
```

It will show a table in the terminal as well as opening a graph comparing the results.

## Profiling

TODO mikel

## Exercises

TODO mikel
