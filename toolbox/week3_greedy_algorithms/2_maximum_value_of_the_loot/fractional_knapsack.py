# Uses python3
import sys

# Sort values based on value/weight
def sort_decending(weights, values):
    weight_val_list = zip(weights, values)

    sorted_dict = {}
    for w, v in weight_val_list:
        sorted_dict.update({v/w: (w, v)})

    sorted_weights_values = [sorted_dict[key] for key in sorted(sorted_dict, reverse=True)]  # value, descending order

    return sorted_weights_values

def get_optimal_value(capacity, weights, values):
    value = 0.

    sorted_weights_values = sort_decending(weights, values)

    for items in sorted_weights_values:
        if capacity == 0:
            return value

        if capacity >= items[0] and capacity != 0:
            capacity = capacity - items[0]
            value += items[1]
        else:
            value += items[1]/(items[0]/capacity)
            capacity = 0
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
