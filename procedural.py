import javalang
import clang
import utilities as util
import math

# Calculate kilo lines of code (KLOC)
def calculate_KLOC(tree):
    with open('main.java', 'r') as file:
        lines = file.readlines()

    count = 0
    for line in lines:
        count += 1

    file.close()
    return str(count / 1000)

# Calculate effective lines of code (ELOC)
def calculate_ELOC(tree):
    with open('main.java', 'r') as file:
        lines = file.readlines()

    count = 0
    for line in lines:
        if not line.isspace():
            count += 1
    file.close()
    return str(count)

# Calculate the number of assignments, branches, and conditions (ABC)
def calculate_ABC(tree):
    # Find prefixes and postfixes for A and unary for C
    fix_list = util.search(tree, 'MemberReference', 'postfix_operators') + util.search(tree, 'MemberReference', 'prefix_operators')
    fix_count = 0
    unary_count = 0

    for fix in fix_list:
        if fix == '++' or fix == '--':
            fix_count += 1
        elif fix:
            unary_count += 1

    # Find binary operators for C
    binary_list = util.search(tree, 'BinaryOperation', 'operator')
    binary_count = 0
    for operation in binary_list:
        if '=' in operation or '<' in operation or '>' in operation:
            binary_count += 1

    # Finds else statement count for C (Still double counts if there is else if)
    statement_list = util.custom_filter(tree, 'IfStatement')
    else_count = 0
    for statement in statement_list:
        if statement.attrs[3]:
            print(statement)
            else_count += 1
    print(else_count)

    # Find ABC amounts for metric
    A = len(util.custom_filter(tree, 'VariableDeclarator') + util.custom_filter(tree, 'Assignment')) + fix_count
    B = len(util.custom_filter(tree, 'MethodInvocation') + util.custom_filter(tree, 'ClassCreator'))
    C = len(util.custom_filter(tree, 'TryStatement') + util.custom_filter(tree, 'CatchClause') + util.custom_filter(tree, 'SwitchStatement')) + unary_count + binary_count + else_count
    ABC = math.sqrt(pow(A, 2) + pow(B, 2) + pow(C, 2))

    # Assess quality
    if(ABC <= 10):
        quality = "Best"
    elif(ABC <= 20):
        quality = "Good"
    elif(ABC <= 40):
        quality = "Needs refactoring"
    elif(ABC <= 60):
        quality = "Needs justifying"
    else:
        quality = "Unacceptable"

    return str('{0:.3g} '.format(ABC)) + '{' + 'A: {}, B: {}, C: {}'.format(A, B, C) + '} ' + quality

# Halstead metrics

# Calculate Halstead program length (N)
def calculate_Halstead_program_length(tree):
    return 4

# Calculate Halstead program vocabulary (n)
def calculate_Halstead_program_vocabulary(tree):
    return 5

# Calculate Halstead program volume (V)
def calculate_Halstead_program_volume(tree):
    return 6

# Calculate Halstead program difficulty (D)
def calculate_Halstead_program_difficulty(tree):
    return 7

# Calculate Halstead program level (L)
def calculate_Halstead_program_level(tree):
    return 8

# Calculate Halstead program effort (E)
def calculate_Halstead_program_effort(tree):
    return 9

# Calculate Halstead number of delivered bugs (B)
def calculate_Halstead_number_of_bugs(tree):
    return 10

# Calculate token count (TC)
def calculate_token_count(tree):
    return 11

# Calculate cyclomatic complexity (MCC)
def calculate_MMCC(tree):
    return 12

# Prints all metrics
def print_all(tree):
    print('KLOC: ' + calculate_KLOC(tree) + ' Lines')
    print('ELOC: ' + calculate_ELOC(tree) + ' Lines')
    print('ABC: ' + calculate_ABC(tree))
    print('N: ' + str(calculate_Halstead_program_length(tree)))
    print('n: ' + str(calculate_Halstead_program_vocabulary(tree)))
    print('V: ' + str(calculate_Halstead_program_volume(tree)))
    print('D: ' + str(calculate_Halstead_program_difficulty(tree)))
    print('L: ' + str(calculate_Halstead_program_level(tree)))
    print('E: ' + str(calculate_Halstead_program_effort(tree)))
    print('B: ' + str(calculate_Halstead_number_of_bugs(tree)))
    print('TC: ' + str(calculate_token_count(tree)))
    print('MCC: ' + str(calculate_MMCC(tree)))

def main():
    path = 'main.java'

    concat_line, comment_count = util.read_file(path, 0)
    tree = javalang.parse.parse(concat_line)

    print_all(tree)

if __name__ == "__main__":
    main()
