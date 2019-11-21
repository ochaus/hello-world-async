import sys
import time
from multiprocessing import Process

combinations = 6  # number of 'Hello' and 'World' combinations to be printed
interval = 10  # printing interval in seconds


# Write 'Hello' into the Stdout buffer.
# Buffered output is used instead of immediate print to ensure 'Hello'
# and 'World' are printed in pairs, with a new line after each pair.
def write_hello():
    sys.stdout.write('Hello ')


# Write 'World' into the Stdout buffer.
def write_world():
    sys.stdout.write('World ')


# Run write_hello() and write_world() simultaneously in separate processes
# for 'combinations' times every 'interval' seconds,
# flushing the buffer after each iteration
if __name__ == '__main__':
    for i in range(combinations):
        proc_hello = Process(target=write_hello)
        proc_hello.start()
        proc_world = Process(target=write_world)
        proc_world.start()
        proc_hello.join()
        proc_world.join()

        sys.stdout.write('\n')
        sys.stdout.flush()
        time.sleep(interval)
