def remove_sort_reverse(my_list):
    my_list.remove("eggplant")
    my_list.sort()
    my_list.reverse()
    return my_list
    

print(remove_sort_reverse(["eggplant", "apple", "zucchini", "rambutan", "grapefruit"]))
