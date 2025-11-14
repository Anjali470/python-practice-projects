def find_largest(lst):
    return max(lst)

def find_smallest(lst):
    return min(lst)

def find_average(lst):
    return sum(lst) / len(lst)

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def reverse_list(lst):
    return list(reversed(lst))

def sort_ascending(lst):
    return sorted(lst)

def find_second_largest(lst):
    return sort_ascending(remove_duplicates(lst))[-2]

def main():
    lst = list(map(int, input("Enter your numbers seperated by space: ").split()))

    print("Your list is: ", lst)
    print("Largest in your list: ", find_largest(lst))
    print("Smallest in your list: ", find_smallest(lst))
    print("Average of the numbers in the list: ", find_average(lst))
    print("List without duplicates: ", remove_duplicates(lst))
    print("Reversed list: ", reverse_list(lst))
    print("Ascending order of the list: ", sort_ascending(lst))
    print("Second largest: ", find_second_largest(lst))

if __name__ == "__main__":
    main()