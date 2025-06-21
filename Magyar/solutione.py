def main():
    with open("szamok.txt", "r") as f:
        line = f.readlines() 
        left_list = []
        right_list = []
        for l in line:
            nums = [int(n) for n in l.split()]
            left_list.append(nums[0])
            right_list.append(nums[1])
    left_list.sort()
    right_list.sort()
    total_diff=0
    for i in range(0,100):
        total_diff += abs(right_list[1] - left_list[0])
    print(total_diff)


if __name__=="__main__":
    main()