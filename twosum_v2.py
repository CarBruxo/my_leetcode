nums = [2,7,3,4,6,11,15]
target = 9
ocurance = []

#abaixo, cortar os números > target
nums2=[]
for i in nums:
    if i <= target:
        nums2.append(i)

#somar as possibilidades de
for a in nums2:
    for b in nums2:
        c = a + b
        if c == target:
            a_pos=nums.index(a)
            b_pos=nums.index(b)
            indexes=[a_pos, b_pos]
            reversed_indexes=indexes[::-1]
            ocurance.append(indexes)

            if ocurance.count(reversed_indexes) >= 1:
                ocurance.remove(indexes)
print(f"{nums} is the input list")
print(f"{ocurance} are the sum options wich outputs target")