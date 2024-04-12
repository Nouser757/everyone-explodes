from ktools import Edge

def decimation(edge: Edge):
    # sourcery skip: list-comprehension, merge-list-appends-into-extend, move-assign-in-block
    #stage 1
    a = input("Enter top display > ")
    b = input("Enter bottom display > ")

    c = []

    c.extend(x if int(x) > int(y) else y for x, y in zip(a, b))

    print(f"Stage 1 - {''.join(c)}")

    #stage 2
    a = input("Enter top display > ")
    b = input("Enter bottom display > ")

    c = []

    c.extend(x if int(x) < int(b) else b for x in a)

    print(f"Stage 2 - {''.join(c)}")

    #stage 3
    a = input("Enter top display > ")
    b = input("Enter bottom display > ")

    c = []
    q = []
    w = []

    q.extend(x if int(x) < int(b[1]) else b[1] for x in a)
    w.extend(x if int(x) < int(b[0]) else b[0] for x in a)

    c.append(w[0])
    c.append(w[1] if int(w[1]) > int(q[0]) else q[0])
    c.append(q[1])

    print(f"Stage 3 - {''.join(c)}")