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
            a_pos=nums.index(a)                                 #posição na lista nums de a
            b_pos=nums.index(b)                                 #posição na lista nums de b
            indexes=[a_pos, b_pos]                              #as duas posições juntas em uma lista [a, b]
            reversed_indexes=indexes[::-1]                      #posições revertidas usando técnica de slicing, na qual N posição se torna a primeira (0) tal que [b, a] se torne [a, b]
            ocurance.append(indexes)                            #adiciona [a, b] na lista de possiveis opções

            if ocurance.count(reversed_indexes) >= 1:           #usando count([a,b]) para ver a quantidade de vezes que [a, b] ocorre na lista de possibilidades, 0 para se nao ocorre, 1 ou + caso já exista.
                ocurance.remove(indexes)                        #caso já existir [a, b], [b, a] seré removido da lista. Já que [a, b] = [b, a] no contexto do código.
                
print(f"{nums} is the input list")
print(f"{ocurance} are the sum options wich outputs target")
