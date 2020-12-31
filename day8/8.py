from sys import stdin


def sum_metadata(tree):

    children, metadata = tree.pop(0), tree.pop(0)

    return sum(sum_metadata(tree) for _ in range(children)) + sum(tree.pop(0) for _ in range(metadata))

def sum_value(tree):

    children, metadata = tree.pop(0), tree.pop(0)

    values = [sum_value(tree) for _ in range(children)]
    metadata_values = [tree.pop(0) for _ in range(metadata)]

    if children:
        return sum(values[i-1] for i in metadata_values if 1 <= i <= children)

    return sum(metadata_values)


values = [int(x) for x in stdin.read().split(" ")]


print(sum_metadata(values.copy()))
print(sum_value(values.copy()))
