"""
Advent of Code 2020
Day: 19
Puzzle: 1
Language: Python
"""

def construct_options(rules):
	options = list()
	target = rules["0"]
	while target:
		option = list()
		current = target.pop(0)
		if rules[current] == "a" or rules[current] == "b":
			option.append(rules[current])
	return options


def parse_rules(rules):
	rules_dict = dict()
	for rule in rules:
		num, content = rule.split(":")
		if "|" in content:
			first_rule, second_rule = content.split("|")
			rules_dict[num] = [first_rule.strip().split(), second_rule.strip().split()]
		else:
			rules_dict[num] = content.strip().split()
	return rules_dict

def main():
	# get rules as tuples ((x, y), (m, n)) and string together?
	infile_path = "../../../data/2020_day_19.txt"
	with open(infile_path, "r") as infile:
		rules = list()
		data = list()
		for line in infile:
			if line.startswith("a") or line.startswith("b"):
				data.append(line.strip())
			elif ":" in line:
				rules.append(line.strip())

	rules_dict = parse_rules(rules)
	print(rules_dict["0"])
	print(rules_dict["8"])
	print(rules_dict["42"])
	options = construct_options(rules_dict)


if __name__ == '__main__':
	main()