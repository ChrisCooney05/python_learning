letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1,
          3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letters: points for letters,
                    points in zip(letters, points)}
# print(letter_to_points)
# using list comprehension we can make a dictionairy for the tuples created by the zip command

letter_to_points[' '] = 0
# print(letter_to_points)
# adds an empty space to the dictionairy with a value of 0


def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total


brownie_points = score_word('BROWNIE')
# print(brownie_points)
# .get will find the first argument passed in and return the value, if it does not exist we can return a default value

player_to_words = {
    'player1': ['BLUE', 'TENNIS', 'EXIT'],
    'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
    'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'],
    'Prof Reader': ['ZAP', 'COMA', 'PERIOD']
}

player_to_points = {}

for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points
# print(player_to_points)
# .items() turns both the key and value iterables so we can use the words list or the player name key
# to note we can also use .key() or .value() if we don't need both key and value

player1 = player_to_words.pop('player1', 'No Player')
# print(player1)
# .pop() mutates the dictionary by deleting the first argument and storing the value in the variable
# the second argument is a default value if the key does not exist

player_to_words.update({'aNewPlayerIsHere': [
                       'TEST', 'CAT', 'POKEMON'], 'whatMorePeople': ['HOUSE', 'TABBY', 'WINNER']})
print(player_to_words)
# when we need to add multiple new keys and values we can use the update method, this takes another dictionary and adds it
