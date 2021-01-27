def reverse_number(number):
    resutl = 0
    number_copy = number
    while number_copy / 10 != 0 :
        resutl = resutl * 10 + number_copy % 10
        number_copy = number_copy // 10
    return resutl

def find_age(number):
    count = 0
    flag = False
    for age_mom_at_born in range(18,80):
        for age in range(age_mom_at_born,100):
            if reverse_number(age) == age - age_mom_at_born:
                count += 1
                if count == number :
                    print("Or")
                    print("your'age current : ",age - age_mom_at_born)
                    print("your mom's age current: ",age)
                    count = 0
                    flag = True
                    break
        count = 0
    if flag == False:
        print("You enter wrong!!!")
            
        #     flag = False
            
def function_input():
    while True:
        string = input("How many times has it happened?(<9)\n(Enter any letter to quick) ")
        if len(string) == 1 and '0' <=string <= '8':
            find_age(int(string))
        else:
            break

function_input()
