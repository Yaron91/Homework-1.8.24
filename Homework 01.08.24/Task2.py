games: list [str] = ["Grand Theft Auto V", "Fortnite", "Overwatch", "Dark Souls", "The Elder Scrolls V:Skyrim"]
#a.
print ("a.", list(filter(lambda game: len(game) > 8,games)))
#b.
print ("b.", list(filter(lambda game: game.upper().startswith("F") , games)))
#c.
print ("c.", list (filter(lambda game: len(game.split()) > 1, games))) #can also use count(' ')
#d.
print ("d.", list(filter(lambda game: game.upper().count("V") >= 1, games)))
#e.
speical_chars ="!@#$%^&*(),.?\":{}|<>"
print ("e.", list(filter(lambda game: any(char in speical_chars for char in game), games)))
#f.
games_with_years: list [str] = ["Grand Theft Auto V, 2013", "Fortnite, 2017", "Overwatch, 2016", "Dark Souls, 2011", "The Elder Scrolls V:Skyrim, 2011"]
print ("f.", list(filter(lambda game:  int(game.split(', ')[1]) > 2014 , games_with_years)))