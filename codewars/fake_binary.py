
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string


def fake_bin(x):
    result = ""
    for index in range(len(x)):
        if int(x[index]) >= 5:
            result += "1"
        else:
            result += "0"
    return result


def fake_bin(x):
    result = "".join(["1" if int(char) >= 5 else "0" for char in x])
    return result
