class Player:
 def play(self):
   print("The Player is playing Cricket.")
class Batsmen(Player):
 def play(self):
  print("The Batsmen is batting.")
class Bowler(Player):
 def play(self):
   print("The Bowler is bowling.")
batsmen = Batsmen()
bowler = Bowler()
batsmen.play()
bowler.play()


  