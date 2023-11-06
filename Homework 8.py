from random import randint, shuffle
from string import ascii_lowercase

my_list1 = ["qwe", "abc", 1234, "Hello"]  # ewq, abc, 4321, Hello
my_list2 = ["ABC", "cuba", "abc", "def"]  # ABC, abc
my_list4 = [1234, "hi", "welcome", 1]  # hi, welcome
my_string5 = "Hello World!"  # H, e, " ", W, r, d, !
my_string_1 = "aaaasdf1"  # 6) a, s, d, f
my_string_2 = "asdfff2"  # 7) s, d


# 1
def process_strings(my_list):
    new_list = []

    for count, list_word in enumerate(my_list):
        if count % 2:
            new_list.append(list_word)
        else:
            conversion = str(list_word)
            flip = conversion[::-1]
            new_list.append(flip)

    return new_list


print(process_strings(my_list1))


# 2
def find_first_a(my_list):
    new_list = []

    for i in my_list:
        lower_case = i.lower()
        first_letter = lower_case[0]
        if first_letter == "a":
            new_list.append(i)

    return new_list


print(find_first_a(my_list2))


# 3
def find_letter_a(my_list):
    new_list = []

    for i in my_list:
        lower_case = i.lower()
        find_letter = lower_case.find("a")
        find_a = lower_case[find_letter]
        if find_a == "a":
            new_list.append(i)

    return new_list


print(find_letter_a(my_list2))


# 4
def find_str(my_list):
    new_list = []

    for i in my_list:
        if isinstance(i, str):
            new_list.append(i)

    return new_list


print(find_str(my_list4))


# 5
def just_one_time(my_string):
    my_list = []

    for i in my_string:
        if my_string.count(i) == 1:
            my_list.append(i)

    return my_list


print(just_one_time(my_string5))


# 6
def at_least_once(set_1, set_2):
    set1 = set(set_1)
    set2 = set(set_2)
    my_list = list(set1.intersection(set2))

    return my_list


print(at_least_once(my_string_1, my_string_2))


# 7.1
def only_once(set_1, set_2):
    result_list = []
    set1 = set(set_1)
    set2 = set(set_2)

    my_list = list(set1.intersection(set2))

    for i in my_list:
        if my_string_1.count(i) == 1 and my_string_2.count(i) == 1:
            result_list.append(i)

    return result_list


print(only_once(my_string_1, my_string_2))

# 7.2
"""
Оскільки ми вже використовували функцію щоб знайти літери які зустрічаються хоча б 1 раз,
Я використовую цю функцію щоб знайти і символи які зустрічаються тільки 1 раз.
"""
result_list = []
for index in at_least_once(my_string_1, my_string_2):
    if my_string_1.count(index) == 1 and my_string_2.count(index) == 1:
        result_list.append(index)


print(result_list)

# 8
names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
length_names = len(names)
length_domains = len(domains)


def random_number(first_number, second_number):
    num = randint(first_number, second_number)

    return num


def random_alphabet(first_number, second_number):
    abc_list = list(ascii_lowercase)
    shuffle(abc_list)

    string_length = randint(first_number, second_number)  # length, from (first_number) to (second_number)
    random_abc = (abc_list[:string_length - 1])

    into_str = "".join(random_abc)

    return into_str


print(f"{names[random_number(0, (length_names-1))]}."
      f"{random_number(100, 999)}@"
      f"{random_alphabet(5, 7)}."
      f"{domains[random_number(0, (length_domains-1))]}"
      )
