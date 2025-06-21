

def sigmum(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


def main():
    with open("input.txt","r") as f:
        lines = f.readlines()
        safe_reports = 0
        for l in lines:
            reports = (int(level) for level in l.split())
            sgn = sigmum(reports[1]-reports[0])
            is_safe = True
            for i in range(1, len(reports)):
                if sigmum(reports[i] - reports[i-1] !=sgn):
                    is_safe = False
                    break
                if abs(reports[i] - reports[i-1] < 1 or abs(reports[i] - reports[i-1] > 3)):
                    is_safe = False
                    break
            if is_safe:
                safe_reports += 1
            print(safe_reports)





if __name__ == "__main__":
    main()
    sigmum()