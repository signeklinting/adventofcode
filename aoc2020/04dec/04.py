def read_passports(filepath):
	
	with open(filepath, 'r+') as f:
		content = f.read()
	content = content.replace('\n\n', '__').replace('\n', ' ').split('__')

	passports = {}

	for i in range(len(content)):
		fields = content[i].split(' ')
		passport = {}
		
		for field in fields:
			if field != '':
				key, value = field.strip(' ').split(':')
				passport[key] = value
		passports[i] = passport
	return passports


def valid_passport(passport):

	fields_mandatory = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

	for f in fields_mandatory:
		if f in passport.keys():
			continue
		else:
			return False
	return True


def check_values(passport):
    
    if int(passport['byr']) not in range(1920, 2003):
        return False
    
    if int(passport['iyr']) not in range(2010, 2021):
        return False
    
    if int(passport['eyr']) not in range(2020, 2031):
        return False

    if passport['hgt'][-2:] not in ['cm', 'in']:
        return False
    elif passport['hgt'][-2:] ==  'cm':
        if int(passport['hgt'][0:-2]) not in range(150, 194):
            return False
    else:
        if int(passport['hgt'][0:-2]) not in range(59, 77):
            return False

    if len(passport['hcl']) != 7:
        return False
    elif passport['hcl'][0] != '#':
        return False
    else:
        if not all([c in 'abcdef0123456789' for c in passport['hcl'][1:]]):
            return False


    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if len(passport['pid']) != 9:
        return False
    elif not all([c in '0123456789' for c in passport['pid']]):
        return False

    return True

#passports = read_passports('04.sample')
passports = read_passports('04.in')

count_valid_fields = 0
count_valid_values = 0
for i, p in passports.items():
	if valid_passport(p):
		count_valid_fields += 1
		if check_values(p):
			count_valid_values += 1
print(count_valid_fields)
print(count_valid_values)
