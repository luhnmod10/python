import timeit

BENCHMARK_ITERATIONS = 1000000
NANOS_IN_SECOND = 1000000000

def measure(name, stmt, setup, count):
    timer = timeit.Timer(stmt, setup)
    total_nanos = timer.timeit(count) * NANOS_IN_SECOND
    per_op_nanos = round(total_nanos / count, 1)
    print("%-18s%14s%20s ns/op" % (name, count, per_op_nanos))

measure("luhnmod10.valid", "luhnmod10.valid('4242424242424242')", "import luhnmod10", BENCHMARK_ITERATIONS)
