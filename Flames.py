def remove_common_letters(name1, name2):
    name1_list = list(name1)
    name2_list = list(name2)
    for letter in name1:
        if letter in name2_list:
            name1_list.remove(letter)
            name2_list.remove(letter)
    return len(name1_list + name2_list)

def flames_game(name1, name2):
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemies", "Siblings"]
    count = remove_common_letters(name1, name2)
    
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]

    return flames[0]

# Input names
name1 = input("Enter the boy name: ").lower().replace(" ", "")
name2 = input("Enter the girl name: ").lower().replace(" ", "")

# Play the game
relationship = flames_game(name1, name2)
print(f"The relationship status is: {relationship}")
