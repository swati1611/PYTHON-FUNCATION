def list1(numbers):
    pc=0
    nc=0
    for i in numbers:
        if i>0:
            pc=pc+1
        else:
            nc=nc+1
    print("possitive number",pc)
    print("negative number",nc)
list1([2,-7,64,12,-8])