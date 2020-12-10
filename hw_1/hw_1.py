# declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
# afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
my_ordered_list = my_list.copy()
my_ordered_list.sort()
# my_ordered_list.sort()
print(my_ordered_list)
# afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
my_descendent_list = my_list.copy()
my_descendent_list.sort(reverse=True)
print(my_descendent_list)
# afișarea numerelor pare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
print(my_ordered_list[1::2])
# afișarea numerelor impare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
print(my_ordered_list[::2])
# afișarea elementelor multipli ai lui 3.
print(my_ordered_list[2::3])

