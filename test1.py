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


# p, d = input().split()
# p = int(p)
# d = int(d)

# while True:
#     if(d%p <= p/2):
#         print(d)
#         break
#     else:
#         d = d + d


import unittest
import re


# اعتبارسنجی آدرس ایمیل

# یک آدرس ایمیل معتبر به شکل username@domain.tld است، به‌طوری که:

#     نام کاربری تنها از کاراکتر انگلیسی، عدد، آندرلاین و نقطه تشکیل شده است.
#     دامنه تنها از کاراکتر انگلیسی یا عدد تشکیل شده است.
#     tld یک واژه‌ی سه‌حرفی از کاراکترهای انگلیسی است.
#     کاراکترهای انگلیسی می‌توانند کوچک یا بزرگ باشد.


import re


def validate_email(email):
    if(re.search('^\w+([\.-]?\w+)*@[\w]+\.[\D]{3}$', email)):
        return True
    else:
        return False


def validate_phone(number):
    if(re.search('^09\d{9}$|^\+98\d{10}$|^0098\d{10}$', number)):
        return True
    else:
        return False


print(validate_email('exampl#e@gmail.comm'))



# class ScoreListTest(unittest.TestCase):

#     def test_validate_email(self):
#         self.assertTrue(validate_email('test.test91@yahoo.com'))
#         self.assertFalse(validate_email('exampl#e@gmail.comm'))

#     def test_validate_phone(self):
#         self.assertTrue(validate_phone('09116547899'))
#         self.assertFalse(validate_phone('091165478999'))





