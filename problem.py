def sort_criteria(participant):
    return (-participant['score'], participant['name'])

def create_scoreboard(participants):
    points = {'chickenwings': 5, 'hamburgers': 3, 'hotdogs': 2}

    for participant in participants:
        participant['score'] = sum(participant[item] * points[item] for item in points)

    participants_sorted = sorted(participants, key=sort_criteria)

    result = [{'name': p['name'], 'score': p['score']} for p in participants_sorted]
    
    return result