def get_sizes():
    sizes = input().split()

    return int(sizes[0]), int(sizes[1])

def get_transition():
    transition = input()

    return transition.split()

def get_string():
    string = input()

    return string.split()

def update_current_letters(current_letters, transitions, ch):
        current_letters.update(ch)

        for next_ch in transitions.get(ch, []):
            if next_ch not in current_letters:
                current_letters.update(next_ch)
                update_current_letters(current_letters, transitions, next_ch)

def check_strings(transitions, strings):
    for string in strings:
        initial_string = string[0]
        final_string   = string[1]

        if (len(initial_string) != len(final_string)):
            print("nao")
            continue

        reacheable_letters = {}
        check = True

        for i in range(0, len(initial_string)):
            initial_letter = initial_string[i]
            final_letter   = final_string[i]

            current_letters = reacheable_letters.get(initial_letter)
            
            if current_letters == None:
                current_letters = set(initial_letter)
                reacheable_letters.update({initial_letter:current_letters})

                for ch in transitions.get(initial_letter, []):
                    update_current_letters(current_letters, transitions, ch)
                    reacheable_letters.update({initial_letter:current_letters})

            current_letters = reacheable_letters.get(initial_letter)

            if final_letter not in current_letters:
                print("nao")
                check = False
                break

        if check == True:
            print("sim")

def convert_strings():
    n, m        = get_sizes()
    transitions = {}
    strings     = []

    for i in range(0, n):
        transition = get_transition()

        letters = transitions.get(transition[0], [])
        letters.append(transition[1])
        transitions.update({transition[0]:letters})

    for j in range(0, m):
        string = get_string()
        strings.append(string)

    check_strings(transitions, strings)
