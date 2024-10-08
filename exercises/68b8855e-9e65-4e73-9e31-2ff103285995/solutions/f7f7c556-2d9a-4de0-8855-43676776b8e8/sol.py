scores = {'Harry': 0, 'Cedric': 0, 'Krum': 0}

# Update scores
scores['Harry'] += 10
scores['Cedric'] += 5
scores['Krum'] += 7

sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for contestant, score in sorted_scores:
    print(f'{contestant}: {score}')