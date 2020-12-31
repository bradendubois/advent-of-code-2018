from sys import stdin
from string import ascii_lowercase, ascii_uppercase

def roots(V, E):
    return set(v for v in V if len([e for e in E if e[1] == v]) == 0)

instructions = stdin.read().split("\n")

V = set()
E = set()

for line in instructions:
    
    l = line.split(" ")
    
    s, t = l[1], l[7]
    
    V.update({s, t})
    E.add((s, t))


# Part One
order = []

V_c = V.copy()
E_c = E.copy()

while len(V_c):

    n = sorted(roots(V_c, E_c))[0]

    V_c.remove(n)
    E_c -= {e for e in E_c if e[0] == n}

    order.append(n)

print("".join(order))


# Part Two
V_c = V.copy()
E_c = E.copy()

workers = 5

assigned = [None] * workers
duration = [0] * workers

seconds = 0

in_progress = set()
done = []

def next_task():
    n = list(set(sorted(roots(V_c, E_c))) - in_progress)
    if len(n):
        return n.pop(0)

while True:

    for worker in range(workers):

        if assigned[worker]:

            duration[worker] -= 1

            if duration[worker] == 0:

                task = assigned[worker]

                in_progress.remove(task)
                done.append(task)
                assigned[worker] = None

                V_c.remove(task)
                E_c -= {e for e in E_c if e[0] == task}

        if not assigned[worker] and (task := next_task()):

            in_progress.add(task)

            assigned[worker] = task
            duration[worker] = ascii_uppercase.index(task) + 61

    if len(V_c) == 0:
        break

    seconds += 1

print(seconds)
