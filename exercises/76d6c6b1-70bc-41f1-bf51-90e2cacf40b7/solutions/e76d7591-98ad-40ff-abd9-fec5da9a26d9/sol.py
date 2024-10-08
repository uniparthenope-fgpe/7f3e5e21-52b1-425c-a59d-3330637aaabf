siths = {'Darth Vader': 'Dark Side', 'Darth Maul': 'Sith'}

try:
    print(siths['Darth Sidious'])
except KeyError:
    print('Sith not found!')
    # Handle the exception here