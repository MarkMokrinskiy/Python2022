import hashlib

f = open('input.txt')
S0 = f.readline()
f.close
i = 0

while True:

    S = S0 + str(i)
    result = hashlib.md5(S.encode())
    H = str(result.hexdigest())
    if not (H[0] == "0" and H[1] == "0" and H[2] == "0" and H[3] == "0" and H[4] == "0"):
        i += 1
    else:
        break

f = open('output1.txt', 'w+')
print(str(i), file = f)
f.close
