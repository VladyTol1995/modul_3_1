from itertools import cycle

calls = 0
def caunt_calls():
    global calls
    calls += 1
def string_info (string):
    caunt_calls()
    lenght = len(string)
    upper = string.upper ()
    lower = string.lower ()
    return (lenght, upper, lower)
def is_contains (string, list_to_seach):
    caunt_calls()
    string_lower = string.lower()
    return string_lower in [item.lower() for item in list_to_seach]
print(string_info('Capibara'))
print(string_info('Armagedon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

