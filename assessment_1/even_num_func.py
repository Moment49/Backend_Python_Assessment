def even_list(nums_list):
    """A function to retreive only even numbers from a list"""
    # empty list to hold the even numbers
    even_nums_list = []
    for num in nums_list:
        if num % 2 == 0:
           even_nums_list.append(num)
        if num % 2 != 0:
            continue
   

    return even_nums_list


