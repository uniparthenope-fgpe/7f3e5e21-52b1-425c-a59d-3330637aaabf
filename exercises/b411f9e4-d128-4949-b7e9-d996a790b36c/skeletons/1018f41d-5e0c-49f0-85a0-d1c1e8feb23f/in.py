ingredients = ['eye of newt', 'dragon blood', 'basilisk fang']
required = ['eye of newt', 'dragon blood', 'unicorn hair']
for item in required:
    if item not in ingredients:
        print('Missing:', item)
    ____