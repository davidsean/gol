from gol.pygame_loader import pygameLoader


loader = pygameLoader()
loader.gol.board[325:385,225:285] = 1

loader.start()