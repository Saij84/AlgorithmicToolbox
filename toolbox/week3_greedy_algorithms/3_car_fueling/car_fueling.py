# python3
import sys


def compute_min_refills(distance, tank, stops):
    num_refills = 0
    current_refills = 0
    line = [0]
    line.extend(stops)
    line.extend([distance])

    num_stops = len(line)

    if num_stops == 2 and distance < tank:
        return 0


    while current_refills <= num_stops:
        last_refill = current_refills
        if line[last_refill] + tank >= distance:
            return num_refills

        while current_refills < num_stops and (line[current_refills+1] - line[last_refill]) <= tank:
            current_refills += 1

        if current_refills == last_refill:
            return -1

        if current_refills <= num_stops:
            num_refills += 1
    return num_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
