def group_by_surname(list_of_enrollees: list) -> int:
    g1 = 0
    g2 = 0
    g3 = 0
    g4 = 0
    for enrollee in list_of_enrollees:
        surname = enrollee.split()[1]
        first_letter = surname[0]

        if 'A' <= first_letter <= 'I':
            g1 += 1
        elif 'J' <= first_letter <= 'P':
            g2 += 1
        elif 'Q' <= first_letter <= 'T':
            g3 += 1
        elif 'U' <= first_letter <= 'Z':
            g4 += 1
    return g1, g2, g3, g4
