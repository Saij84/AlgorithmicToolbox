# python3
import sys


def compute_min_refills(distance, tank, stops):
    num_refills = 0
    current_refills = 0
    stops = [200, 375, 550, 750]
    num_stops = len(stops)-1

    while current_refills <= num_stops:
        print(num_refills)
        print("tdist:", stops[num_refills] + tank)
        last_refill = current_refills

        while current_refills < num_stops and (stops[current_refills+1] - stops[last_refill]) <= tank:
            current_refills += 1

        if current_refills == last_refill:
            return -1

        if current_refills <= num_stops:
            num_refills += num_refills

    return num_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
