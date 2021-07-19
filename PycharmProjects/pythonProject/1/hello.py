print ("asdzxxcv")

def her(s):
        print('heroine is '+s+'')


her('drug'), her('gift'), her('death')


def percents(x, y):
    '''What percantage of x is y'''
    one_percent=x/100
    result=y/one_percent
    return result


def print_percents(x, y):
    '''Prints result of percents func'''
    print(str(y) + ' is ' + str(percents(x,y)) + '% of ' + str(x))


print_percents(10, 25)