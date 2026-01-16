#!/usr/bin/env python3
"""
uuidgen4.py — generate UUIDs and optionally measure performance.

Usage examples:
  - Generate 24 Microsoft-style UUIDs (default):
      python uuidgen4.py

  - Generate 100 plain lowercase UUIDs:
      python uuidgen4.py -n 100 --format plain --lowercase

  - Generate 50 and output benchmark info:
      python uuidgen4.py -n 50 --benchmark

  - Output JSON (uuids + metrics):
      python uuidgen4.py -n 10 --json --benchmark
"""

from __future__ import annotations
import argparse
import json
import logging
import sys
import time
import tracemalloc
import uuid
from typing import Iterable, Iterator, List, Tuple


def generate_uuids(count: int = 24, ms_format: bool = True, uppercase: bool = True) -> Iterator[str]:
    """
    Yield `count` UUIDs.

    - ms_format True: yield in Microsoft format "{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}"
    - uppercase True: characters will be uppercased
    """
    for _ in range(count):
        u = str(uuid.uuid4())
        if uppercase:
            u = u.upper()
        if ms_format:
            yield "{" + u + "}"
        else:
            yield u


def measure_performance(
    generator_func,
    *gen_args,
    benchmark: bool = True,
) -> Tuple[List[str], float, float]:
    """
    Run the generator_func (which should return an iterable of strings) and optionally
    measure elapsed time (seconds) and peak memory (MB).

    Returns (outputs, elapsed_seconds, peak_memory_mb)
    If benchmark is False, elapsed_seconds and peak_memory_mb will be 0.0.
    """
    outputs: List[str] = []

    if benchmark:
        tracemalloc.start()
        start = time.perf_counter()
        for s in generator_func(*gen_args):
            outputs.append(s)
        elapsed = time.perf_counter() - start
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        peak_mb = peak / 1024 ** 2
    else:
        # No benchmarking — just produce outputs
        start = time.perf_counter()
        for s in generator_func(*gen_args):
            outputs.append(s)
        elapsed = time.perf_counter() - start
        peak_mb = 0.0

    return outputs, elapsed, peak_mb


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate UUIDs and optionally measure performance.")
    parser.add_argument("-n", "--count", type=int, default=24, help="Number of UUIDs to generate (default: 24)")
    parser.add_argument("--format", choices=("ms", "plain"), default="ms", help="Output format: 'ms' (with braces) or 'plain'")
    parser.add_argument("--lowercase", action="store_true", help="Output UUIDs in lowercase (default: uppercase)")
    parser.add_argument("--no-benchmark", dest="benchmark", action="store_false", help="Don't measure time/memory usage")
    parser.add_argument("--json", action="store_true", help="Output results as JSON (includes uuids and optional metrics)")
    parser.add_argument("-v", "--verbose", action="count", default=0, help="Increase verbosity (use -v, -vv)")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    # Configure logging
    level = logging.WARNING
    if args.verbose >= 2:
        level = logging.DEBUG
    elif args.verbose == 1:
        level = logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")

    ms_format = args.format == "ms"
    uppercase = not args.lowercase

    logging.debug("Arguments: %s", args)

    outputs, elapsed, peak_mb = measure_performance(
        generate_uuids,
        args.count,
        ms_format,
        uppercase,
        benchmark=args.benchmark,
    )

    # Output
    if args.json:
        payload = {
            "uuids": outputs,
            "metrics": {"elapsed_seconds": round(elapsed, 8), "peak_memory_mb": round(peak_mb, 8)},
        }
        json.dump(payload, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        for u in outputs:
            print(u)
        if args.benchmark:
            print()
            print("----------------------------------------------------------------")
            print(f"It took {elapsed:.8f} seconds and {peak_mb:.8f} MB (peak) to execute this program")
            print("----------------------------------------------------------------")
            print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

