class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def ing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway = Song(["There's a lady who's sure",
                "all that glitters is gold", 
                 "and she's buying a stairway to heaven"])        
stairway.ing_me_a_song()


