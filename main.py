def solve_case():
    x = int(input())
    ys = list(map(int, input().split()))
    if len(ys) != x:
        return -1
    return sum(map(lambda y: y ** 4, filter(lambda y: y <= 0, ys)))


def main():
    n = int(input())
    results = list(map(lambda _: solve_case(), range(n)))
    print("\n".join(map(str, results)))


if __name__ == "__main__":
    main()
#---------------------------------------------------------------------
