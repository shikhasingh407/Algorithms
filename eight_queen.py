from itertools import permutations
# permutations so that no two queens are in the same coordinate

N=8
sol=0
cols = range(N)

# taking care of all the permutations
for combo in permutations(cols):
    # Taking care of positive and negative slope y = mx + c
    if N==len(set(combo[i]+i for i in cols))==len(set(combo[i]-i for i in cols)):
        sol += 1
        print('Solution '+str(sol)+': '+str(combo)+'\n')
        print("\n".join(' o ' * i + ' X ' + ' o ' * (N-i-1) for i in combo) + "\n\n\n\n")

# Not taking mirror into considerations
