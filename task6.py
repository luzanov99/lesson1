#task6_1
def get_summ(one, two, delimiter='&'):
    one=str(one)
    two=str(two)
    result=(one, two)
    return delimiter.join(result).upper()

print(get_summ("Learn","Python"))


