nums = [2,7,3,4,6,11,15]
target = 9

ocurance = []

'''for i in nums:
    z=+i
    if z <= target:
        print(z)
        pos=nums.index(i)
        ocurance.append(pos)
print(ocurance)'''
#cortar os números > target
nums2=[]
for i in nums:
    if i <= target:
        nums2.append(i)
print(nums2)

#somar as possibilidades de
for a in nums2:
    for b in nums2:
        if a == b: 
            print(f'passed')
            pass
        else:
            #a+=b
            #if a >= target: 
            #   print(a) 
            try:
                if a >= target:
                    print(f'{a} + {b} is greater than {target}')
            except:
                a+=b