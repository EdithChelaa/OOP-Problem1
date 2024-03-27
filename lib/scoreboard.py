def calculate_score(participants):
    scores = []
    
    for participant in participants:
        score = participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2
        scores.append((participant['name'], score))
    
    scores.sort(key=get_key_to_sort)
    
    return scores

# function to get sort key
def get_key_to_sort(participant):
    return (-participant[1], participant[0])

participants = [
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
    ]

scoreboard = calculate_score(participants)
for name, score in scoreboard:
    print(f"{name}: {score}")
