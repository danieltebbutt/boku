
class board:
    # top-left to top-right, working down
    tiles = [ [],[],[],[],[],[],[],[],[],[],[] ]
           
    def __init__(self):
        for ii in range(0, 6):
            for jj in range(0, ii+5):
                self.tiles[ii].append(0)
            for jj in range(ii+5, 10):
                self.tiles[ii].append(-1)
        for ii in range(6, 11):
            for jj in range(0, ii-5):
                self.tiles[ii].append(-1)
            for jj in range(7-ii, 10):
                self.tiles[ii].append(0)
        return

    def display_line(self, line):
        if line < 6:
            for jj in range(0, 5-line):
                print "",
        else:
            for jj in range(0, line-5):
                print "",
        for ii in range(0, 10):
            if self.tiles[line][ii] == 0:
                print ".",
            if self.tiles[line][ii] == 1:
                print "W",
            if self.tiles[line][ii] == 2:
                print "B",
        print
        
    def display(self):
        for ii in range(0, 10):
            self.display_line(ii)
        
    def score(self):
        rows = []
        for ii in range(0, 11):
            for jj in range(0, 5):
                rows.append((self.tiles[ii][jj],
                             self.tiles[ii][jj+1],
                             self.tiles[ii][jj+2],
                             self.tiles[ii][jj+3],
                             self.tiles[ii][jj+4]))
        
        for row in rows:
            if row == (1, 1, 1, 1, 1):
                return 1000
            if row == (2, 2, 2, 2, 2):
                return -1000
        
        return 0
    
    def move(self, move):
        assert(self.tiles[move.row - 1][move.index - 1] == 0)
        self.tiles[move.row - 1][move.index - 1] = move.token
        