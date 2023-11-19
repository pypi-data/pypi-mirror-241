def compare(i):
    try:
        p = set([i.strip().split("#")[0] for i in open(f"page{i}.txt", "r").readlines()])
        o = set([i.strip() for i in open(f"o_page{i}.txt", "r").readlines()])
        print([*(o - p)])
    except FileNotFoundError:
        print("done")


if __name__ == '__main__':
    compare(3)
