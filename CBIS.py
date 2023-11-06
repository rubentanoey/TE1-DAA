# CBIS: Clustered Binary Insertion Sort
# From Shubham Goel and Ravinder Kumar. Brownian Motus and Clustered Binary Insertion Sort methods: An efficient progress over traditional methods. Future Generation Computer Systems,86:266–280, 2018.

def place_inserter(a_list, start, end, current):
    temp = a_list[end]
    for k in range(end, start, -1):
        a_list[k] = a_list[k - 1]
    a_list[start] = current
    return a_list

def binary_loc_finder(a_list, start, end, key):
    if start == end:
        if a_list[start] > key:
            loc = start
        else:
            loc = start + 1
        return loc
    
    if start > end:
        loc = start
        return loc
    
    middle = (start + end) // 2
    
    if a_list[middle] < key:
        return binary_loc_finder(a_list, middle + 1, end, key)
    elif a_list[middle] > key:
        return binary_loc_finder(a_list, start, middle - 1, key)
    else:
        return middle

def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        COP = i
        key = a_list[COP]
        POP = 0

        if key >= a_list[POP]:
            place = binary_loc_finder(a_list, POP + 1, COP - 1, key)
        else:
            place = binary_loc_finder(a_list, 0, POP - 1, key)
        
        position = place
        a_list = place_inserter(a_list, position, COP, key)

        # Print which numbers are being compared to current key
        # if place == 0:
        #     print("Comparing", key, "to", a_list[place + 1])
        # elif place == COP:
        #     print("Comparing", key, "to", a_list[place - 1])
        # else:
        #     print("Comparing", key, "to", a_list[place - 1], "and", a_list[place + 1])
    return a_list




# Example usage:
if __name__ == "__main__":
    a_list = [52, 23, 36, 76, 65]
    sorted_list = insertion_sort(a_list)

    print(sorted_list)