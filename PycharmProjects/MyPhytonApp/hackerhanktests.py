 def simpleArraySum(ar):
     soma = 0
     for a in ar:
         soma = soma + a
     return soma


 res = simpleArraySum([1,2,3,4,10,11])
# print(res)



def compareTriplets(a, b):

    alice = 0
    bob = 0

    resp = list()

    for x,y in zip(a,b):
        if x > y:
            alice = alice + 1
        elif x < y:
            bob = bob +1

    resp.append(alice)
    resp.append(bob)

    print(resp)


def aVeryBigSum(ar):
    try:
        res = 0
        for e in ar:
           res = res + e
        return res
    except:
        print(0)



def diagonalDifference(arr):

    primary_diag = 0
    secondary_diag = 0

    forward = 0
    backward = len(arr)-1
    pos = 0

    for elem in arr:
        primary_diag = primary_diag + elem[forward]
        secondary_diag = secondary_diag + elem[backward]
        forward = forward + 1
        backward = backward -1
    return(abs(primary_diag - secondary_diag))

#print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))

