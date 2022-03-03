def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    
    from collections import Counter
    return Counter(list(str(num1))) == Counter(list(str(num2)))
    

    # num1 = str(num1)
    # num2 = str(num2)

    # if set(num1) == set(num2):
    #     for num in set(num1):
    #         return {num : list(num1).count(num)} == {num : list(num2).count(num)}
    # return False