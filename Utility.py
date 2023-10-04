
# Utility function to trim away unnecessary information in the string
# will return a list with both teams

# TODO implement a split for 'VS' (games that are played internationally)
# DAL @ SF, DAL VS SF (international game)
def split_away_home(game):
    t_game = game.split('-', 1)[0]
    s_game = t_game.split('@')
    return s_game
