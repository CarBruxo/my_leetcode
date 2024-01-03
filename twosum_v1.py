nums = [2,7,3,4,6,11,15]
target = 9
ocurance = []

#abaixo, cortar os números > target
nums2=[]
for i in nums:
    if i <= target:
        nums2.append(i)
print(f'From the {nums} input list, the following operations will be made to achieve sum value of {target}:')
#somar as possibilidades de
for a in nums2:
    for b in nums2:
        #will try condition a = b equals true
        if a == b:
             print(f"{a} + {b} ignored")
        #if the 2 != 7, for example, runs the code down below.
        else:
            c = a + b
            #if sum of two is greater than the target
            if c > target:
                print(f"sum of {a} + {b} are greater than {target}")
            #if sum of two is valid option
            elif c == target:
                print(f'{a} + {b} is a valid option, passed')
                indexes=[nums.index(a), nums.index(b)]
                ocurance.append(indexes)
            else:
                print(f'{a} + {b} does not meet the {target}')
print(ocurance)