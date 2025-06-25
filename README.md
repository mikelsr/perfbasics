# perfbasics
Materials for my "Writing Faster Code: Profiling and Performance Basics" talk in 0xDeusto, 2025-06-24.

## Slides

The slides used for the talk are in the [slides.pdf](https://github.com/mikelsr/perfbasics/blob/main/slides.pdf) file.

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
python3 -m tools.compare out/row.json out/column.json
```

It will show a table in the terminal as well as opening a graph comparing the results.

## Profiling

Generate a profile file by running the script with:

```shell
python3 -m cProfile -o out/<name>.prof <program>.py
```

Where:
- `<name>` is the name of the profile file to be generated.
- `<program>` is the name of the program to profile.

For example:

```shell
python3 -m cProfile -o out/from_file.prof lab/matrices_io.py --source=file --path=data/matrix_3000.txt
```

Then open the profile analyzer with:

```shell
snakeviz out/<name>.prof
```

For example:

```shell
snakeviz out/from_file.prof
```

## Lab

Let's try and make the `lab/wordcount.py` file more efficient. It's a program that counts how many times each word appears in some text.

The code is really slow and obtuse. Don't try to understand the algorithm within each function. Instead, profile the file to see which ones are the slowest, understand the input they receive and the output they produce, and find simpler and faster ways of doing the same. You can profile and benchmark it with:

```
python3 -m cProfile -o out/wordcount.prof lab/wordcount.py
```

and

```shell
python3 -m tools.benchmark lab.wordcount main out/wordcount.json
```
