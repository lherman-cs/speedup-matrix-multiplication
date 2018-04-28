#!/usr/bin/env python3

import subprocess
from os.path import exists

PROG = "./matmul_opt"


def run(n):
    args = [PROG, str(n), str(n), str(n)]
    proc = subprocess.Popen(args, stdout=subprocess.PIPE)

    (outs, _) = proc.communicate()

    return float(outs.decode())


def benchmark(params, repeat=3):
    for param in params:
        avg = 0
        print("n = {}: ".format(param), end='', flush=True)
        for _ in range(repeat):
            avg += run(param)
        avg /= repeat

        print("{:.4f} s".format(avg))


def compile():
    proc = subprocess.Popen(["make"])
    proc.communicate()


def main():
    compile()
    benchmark([1000, 2000, 3000, 4000, 5000])


if __name__ == "__main__":
    main()
