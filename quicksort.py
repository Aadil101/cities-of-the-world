#quicksort.py
#Aadil Islam
#February 25, 2018

def partition(the_list, p, r, compare_func):

    pivot = the_list[r]

    # these are markers
    i = p - 1
    j = p

    while j < r:

        # check if dealing with ints or strings
        if do_it(compare_func, the_list[j], pivot):

            #switch entries
            temp = the_list[j]
            the_list[j] = the_list[i + 1]
            the_list[i + 1] = temp
            i += 1
        j += 1

    # switch entries
    the_list[r] = the_list[i + 1]
    the_list[i + 1] = pivot

    return i+1

# check if ints or strings
def do_it(compare_func, a, b):

    if compare_func == "int":
        return compare_ints(a,b)
    elif compare_func == "strings":
        return compare_strings(a,b)
    elif compare_func == "city_name":
        return compare_strings(a.name,b.name)
    elif compare_func == "city_population":
        return compare_ints(b.pop,a.pop)
    elif compare_func == "city_latitude":
        return compare_ints(a.lat,b.lat)

def compare_ints(a, b):

    return a <= b

def compare_strings(a, b):

    return a <= b

def quicksort(the_list, p, r, compare_func):

    # check if size of list being checked is big enough
    if r > p:

        # sort each new half of the list beside pivot
        pivot = partition(the_list, p, r, compare_func)
        quicksort(the_list,p,pivot-1,compare_func)
        quicksort(the_list,pivot+1,r,compare_func)

# run quicksort
def sort(the_list, compare_func):

    quicksort(the_list, 0, len(the_list)-1, compare_func)