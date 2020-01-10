def list_benefits():
    return ["One", "Two", "Three", "Four"]


def build_sentence(args):
    return "%s is argument of function" % args


def print_pattern():
    for k in range(5):
        print("*"*k)


tempList = list_benefits()

for i in range(len(tempList)):
    print(build_sentence("Function calling"))

print_pattern()


