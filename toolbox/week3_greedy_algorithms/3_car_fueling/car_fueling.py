# python3
import sys


def compute_min_refills(distance, tank, num_stops, stops):
    num_refills = 0
    current_refills = 0


    while current_refills <= num_stops-1:
        last_refill = current_refills

        while (current_refills < num_stops-1 and (stops[current_refills+1] - stops[last_refill]) <= tank):
            if tank <= current_refills:
                return current_refills

            tank -= current_refills+1
            current_refills += 1

        if current_refills == last_refill:
            return -1

        if current_refills <= num_stops-1:
            num_refills += num_refills
    return num_refills

if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, n, stops))
