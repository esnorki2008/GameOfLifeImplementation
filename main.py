from enum import Enum


class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y

        self.isAlive = False

        self.left = None
        self.right = None
        self.up = None
        self.down = None

        self.neighbours = 0 


    def set_neighbours(self,count):
        self.neighbours = count

    def disable(self):
        self.isAlive = False

    def enable(self):
        self.isAlive = True

    def text(self):
        if self.isAlive:
            return "X"
        return "-"

class Sim:
    def __init__(self):
        self.board = []
        self.dimension = 20

        for y in range(0,self.dimension):
            for x in range(0,self.dimension):
                cell =  Cell(x,y)
                self.board.append(cell)
               
    

        self.square(10,10)
        self.line(5,5)
        self.line(14,14)
        self.ship(1,1)

    def ship(self,x,y):
        a = self.get_lineal(x+1,y+2,self.dimension)   
        b = self.get_lineal(x,y+1,self.dimension)   
        c = self.get_lineal(x+2,y,self.dimension)   
        d = self.get_lineal(x+2,y+1,self.dimension)   
        e = self.get_lineal(x+2,y+2,self.dimension)   
        a.enable()
        b.enable()
        c.enable()
        d.enable()
        e.enable()

    def square(self,x,y):
        a = self.get_lineal(x,y,self.dimension)   
        b = self.get_lineal(x,y+1,self.dimension)   
        c = self.get_lineal(x+1,y,self.dimension)   
        d = self.get_lineal(x+1,y+1,self.dimension)   
        a.enable()
        b.enable()
        c.enable()
        d.enable()

    def line(self,x,y):
        a = self.get_lineal(x,y,self.dimension)   
        b = self.get_lineal(x+1,y,self.dimension)   
        c = self.get_lineal(x+2,y,self.dimension)   
        a.enable()
        b.enable()
        c.enable()
  

    def get_lineal(self,x,y,dimension):
        if(x < 0 or x >= dimension):
            return None
        if(y < 0 or y >= dimension):
            return None
        lineal = x + y*dimension
        return self.board[lineal]

    def verify_neighbour(self,x,y,dimension):
        retrieved_cell = self.get_lineal(x,y,dimension)
        if retrieved_cell is not None and retrieved_cell.isAlive:
            return 1
        return 0            


    def count_neighbours (self,cell,dimension):
        total_count = 0
        total_count = total_count + self.verify_neighbour(cell.x - 1, cell.y,dimension) 
        total_count = total_count + self.verify_neighbour(cell.x + 1, cell.y,dimension) 
        total_count = total_count + self.verify_neighbour(cell.x, cell.y - 1,dimension) 
        total_count = total_count + self.verify_neighbour(cell.x, cell.y + 1,dimension) 
        total_count = total_count + self.verify_neighbour(cell.x - 1, cell.y - 1,dimension)
        total_count = total_count + self.verify_neighbour(cell.x - 1, cell.y + 1,dimension)
        total_count = total_count + self.verify_neighbour(cell.x + 1, cell.y - 1,dimension)
        total_count = total_count + self.verify_neighbour(cell.x + 1, cell.y + 1,dimension)
        return total_count

    

    def next_iteration(self):
        d = 0
        concat = ""
        print("\n\n\n\n\n\n")
        for cell in  self.board:
            concat = concat + cell.text()
            d = d + 1
            if d >= self.dimension:
                print(concat)
                concat = ""
                d = 0
        

        for cell in  self.board:
            neighbours_count = self.count_neighbours(cell,self.dimension)
            cell.set_neighbours(neighbours_count)
        
        #d = 0
        #concat = ""
        #for cell in  self.board:
        #    concat = concat + str(cell.neighbours)
        #    d = d + 1
        #    if d >= self.dimension:
        #        print(concat)
        #        concat = ""
        #        d = 0


        for cell in  self.board:
            if(cell.neighbours < 2 or cell.neighbours > 3):
                cell.disable()
            else:
                if cell.isAlive and (cell.neighbours == 3 or cell.neighbours == 2):
                    pass
                if not cell.isAlive and cell.neighbours == 3:
                    cell.enable()

    def start(self):
        while True:
            self.next_iteration()
            input()

sm = Sim()
sm.start()