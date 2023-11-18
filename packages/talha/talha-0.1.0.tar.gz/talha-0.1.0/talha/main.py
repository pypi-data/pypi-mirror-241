def fact(num):
    try:
        num=int(num)
    except:
        return "fact accept only numbers<int>"
    else:
        if num < 0:
            return None
        elif num == 0:
            return(1)
        else:
            result = 1
            for i in range(1, num + 1):
                result *= i
            return result

