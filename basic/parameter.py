def greet(lang):
    if lang=='es':
        return 'Hola'
    if lang=='fr':
        return 'Bonjour'
    if lang=='en':
        return 'Hello'

print greet('es'), 'Jane'
print greet('en'), 'Josh'
print greet('fr'), 'Sally'