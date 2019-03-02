def age_comparing():

    age = int(input('Input your age: '))
    if age <= 0:
        raise Exception('Age must be positive')
    if 0 < age <= 7:
        return "You have to go children garden."
    elif 7 < age <= 17:
        return "You have to go school."
    elif 17 < age <= 80:
        return "You have to work or finding job"
    return "People don't live so much."

# Second func

def compare_string(str1: str, str2: str) -> bool:
    if isinstance(str1, str) and isinstance(str2, str):
        if str2 == 'learn' and len(str1) != len(str2):
            return 3
        elif str1 == str2:
            return 1
        elif len(str1) >= len(str2):
            return 2
    else:
        return 0

    return "Default value"


print(age_comparing())
print(compare_string('friend', 'friends')) # Default value
print(compare_string('friend', 'friend')) # 1
print(compare_string('friends', 'friend')) # 2
print(compare_string('friend', 'learn')) # 3
print(compare_string('545', 5)) # 0
