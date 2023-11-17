# PACE 2024 Verifier

This package can be used to verify a given solution against a set of crossing counting algorithms.

## Installation

The verifier can be installed from pip:

```console
$ pip install pace2024verifier
```

Feel also free to clone the code from git:

```console
$ git clone ???
```

## Usage

To verify a solution use the following command:

```console
$ pace2024verify <path/to/graph.gr> <path/to/solution.sol>
```

The verifiery has three different methods for verification usable via the switches `--<name>`:
* segtree = Use a segment tree to count the crossings. `[default]`
* interleave = Count the crossings by checking for each pair of edges if they interleave.
* stacklike = Count the crossings by checking how many pairs are out of order in a one-sided book embedding.

There is also a switch to only print the number of crossings `-c/--only-crossings`.
