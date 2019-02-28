# Uses python3
import sys
from collections import namedtuple
from operator import itemgetter

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    sorted_segments = sorted(segments, key=itemgetter(1))
    n = len(segments)-1
    print("n", n)
    i = 0

    while i <= n:
        print(sorted_segments[i].end, sorted_segments[i+1].end)
        l, r = sorted_segments[i].end, sorted_segments[i+1].end

        points = [l, r]
        i += 1

        while i <= n and sorted_segments[i].end <= r:
            i += 1
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
