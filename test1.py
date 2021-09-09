# print("I'm Here Now ...")


# degree = int(input("Please Enter Your Water Degree ! \n> ")) 
# if degree > 100:
#    print("\nStem")
# elif(degree < 0):
#    print("\nIce")
# else:
#     print("\nWater")
    
    
# 1 2 3 4 5
# 2
# 3
# 4
# 5

# for row in range(1,6):
#     for col in range(1,6):
#             print(row*col , end=' ' )
#     print(' ')


p, d = input().split()
p = int(p)
d = int(d)

while True:
    if(d%p <= p/2):
        print(d)
        break
    else:
        d = d + d



