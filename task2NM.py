# 1. Listin bütün elementləri cəmini(hasilini) hesablayın



# numbers = [1, 2, 3, 4, 5]



# sum_of_numbers = 0
# product_of_numbers = 1

# for number in numbers:
#     sum_of_numbers += number
#     product_of_numbers *= number


# print(sum_of_numbers)
# print(product_of_numbers)


# 2. Verilən list elementlərini sağdan sola çap edin



# numbers = [1, 2, 3, 4, 5]

# numbers.reverse()

# print(numbers)





# 3. İki fərqli list yaradın və listləri merge edin(zip metodu)

# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]

# merged_list = list(zip(list1, list2))


# print(merged_list)

# merged_list = [list(x) for x in merged_list]


# print(merged_list)




# 4. Listin içində bir neçə list olsun, 3ci elementinin 2ci indeksinə dəyər əlavə edin

# lists001 = [['a', 2, 4], ['b', 6, 9], ['c', 7, 9]]

# lists001[2][1] += 1


# print(lists001)

# 5. List yaradın , listin hər hansı dəyərinin indeksini tapın və həmin indeksə başqa dəyər əlavə edin


# my_list = [1, 2, 3, 4, 5]

# index_of_three = my_list.index(3)

# my_list[index_of_three] += 2

# print(my_list)




# 6. Verilmiş listin ədədi ortasını tapın


# my_list = [1, 3, 5, 7, 9]

# my_list.sort()


# if len(my_list) % 2 == 1:
#     median = my_list[len(my_list) // 2]
# else:
#     m1 = my_list[len(my_list) // 2 - 1]
#     m2 = my_list[len(my_list) // 2]
#     median = (m1 + m2) / 2

# print(median)





# 7. İnputdan gələn iki rəqəm aralığında yerləşən rəqəmlərin cüt və ya tək olduğunu(əlavə olaraq cüt rəqəmlərin sayını hesablayın) tapıın


# start = int(input("Birinci rəqəm: "))
# end = int(input("İkinci rəqəm: "))

# if start > end:
#     start, end = end, start


# even_count = 0
# even_sum = 0

# for num in range(start, end + 1):
#     if num % 2 == 0:
#         print(num, "Çüt")
#         even_count += 1
#         even_sum += num
#     else:
#         print(num,"Tək")


# print(even_count)
# print(even_sum)



# 8. Təkrar elemetlərdən ibarət list yaradın, sonra bu listdən təkrarlanmayan list yaradın


# my_list = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]


# unikal_set = set(my_list)

# unikal_list = list(unikal_set)
# print(unikal_list)



# 9. 3 rəqəmdən  ibarət list yaradın və bu listin rəqəmlərindən yarana biləcək kombinasiyaları çap edin


# from itertools import permutations

# numbers = [1, 2, 3]

# permutations_list = list(permutations(numbers))

# print("kombinasiyalar:")
# for combination in permutations_list:
#     print(combination)






# choice = input("Seçim edin: ")
# if choice == '1' and '1' in a:
#     new_name = input("Əlavə etmək istədiyiniz adı daxil edin: ")
#     add_name(new_name)
# elif choice == '2' and '2' in a:
#     delete_name = input("Silinəcək adı daxil edin: ")
#     delete_name(delete_name)
# elif choice not in ('1', '2'):
#     print("Elan daxil etmədiniz.")
# else:
#     print("Bu reklam bazası yoxdur.")






# 10.

# message = input("Daxil Edin:  ")

# num = int(input("Say: "))

# for i in range(1, num + 1):
#     print(i, message)
