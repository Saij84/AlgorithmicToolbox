# python3
import sys


def compute_min_refills(distance, tank, num_stops, stops):
    num_refills = 0
    current_refills = 0

    if num_stops == 2 and distance < tank:
        return 0


    while current_refills <= num_stops:
        last_refill = current_refills
        if stops[last_refill] + tank >= distance:
            return num_refills

        print(stops[current_refills+1] - stops[last_refill])

        while current_refills < num_stops and (stops[current_refills+1] - stops[last_refill]) <= tank:
            #print(stops[current_refills+1] - stops[last_refill])
            current_refills += 1

        if current_refills == last_refill:
            return -1

        if current_refills <= num_stops:
            num_refills += 1
    return num_refills

if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, n, stops))
