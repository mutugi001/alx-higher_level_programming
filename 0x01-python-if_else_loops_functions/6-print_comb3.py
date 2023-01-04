#!/usr/bin/python3
for i in range(0, 10):
    for k in range(0, 10):
        if i != k:
            if int(str(i) + str(k)) < int(str(k) + str(i)):
                if i == 8 and k == 9:
                    print("{}".format(str(i)+str(k)))
                else:
                    print("{}".format(str(i)+str(k)), end=', ')
