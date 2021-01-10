
def valid_password(password_row):
    
    rule, password = password_row.split(': ')
    count, letter = rule.split(' ')
    count = [int(i) for i in count.split('-')]

    if password.count(letter) in range(count[0], count[1]+1):
        return True
    
    return False


def other_valid_password(password_row):
    
    rule, password = password_row.split(': ')
    count, letter = rule.split(' ')
    count = [int(i) for i in count.split('-')]

    if (password[count[0]-1]==letter) ^ (password[count[1]-1]==letter):
        return True
    return False


if __name__ == "__main__":
    with open('02.in') as f:
        lines = [l.strip('\n') for l in f.readlines()]

    n = 0

    for line in lines:
        if valid_password(line):
            n+=1
    print(n)

    n_new = 0
    for line in lines:
        if other_valid_password(line):
            n_new+=1
    print(n_new)