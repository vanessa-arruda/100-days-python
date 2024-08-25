from count_true_love import count_true_love


def get_name() -> str:
    return input("Type a name: ").upper()


def love_calculator_score(first_name: str, second_name: str) -> int:

    name1 = count_true_love(first_name)
    name2 = count_true_love(second_name)
    print()
    print(f"Checking {first_name} & {second_name} love score...")

    # store summed values
    combined_values = {}

    for key in name1:
        combined_values[key] = name1[key] + name2[key]

    combined_total_true = (
        combined_values["T"]
        + combined_values["R"]
        + combined_values["U"]
        + combined_values["E"]
    )
    combined_total_love = (
        combined_values["L"]
        + combined_values["O"]
        + combined_values["V"]
        + combined_values["E"]
    )

    print(
        f"""
T occurs: {combined_values['T']} time{'s' if combined_values['T'] != 1 else ''}
R occurs: {combined_values['R']} time{'s' if combined_values['R'] != 1 else ''}
U occurs: {combined_values['U']} time{'s' if combined_values['U'] != 1 else ''}
E occurs: {combined_values['E']} time{'s' if combined_values['E'] != 1 else ''}

Total true: {combined_total_true}

L occurs: {combined_values['L']} time{'s' if combined_values['L'] != 1 else ''}
O occurs: {combined_values['O']} time{'s' if combined_values['O'] != 1 else ''}
V occurs: {combined_values['V']} time{'s' if combined_values['V'] != 1 else ''}
E occurs: {combined_values['E']} time{'s' if combined_values['E'] != 1 else ''}

Total love: {combined_total_love}
        
Love Score = {combined_total_true}{combined_total_love}
        """
    )


print("Love Score Calculator\n")
print("Let's see if the score of the two name combine together!\n")

love_calculator_score(first_name=get_name(), second_name=get_name())
