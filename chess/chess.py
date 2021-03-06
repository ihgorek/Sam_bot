from PIL import Image,ImageDraw


class ChessGame(object):
    '''
    шахматы
    TODO
    1. Научиться рисовать шахматы
    2. Найти все фигуры(их картинки)
    3. Продумать логику(научиться рисовать поле и фигуры по ходам)
    4. Передавать сессии в строке, где определнная последовательность будет означать определнную сессию игры.
    '''
    def __init__(self):
        with Image.open('board.jpg') as self.board:
            self.draw = ImageDraw.Draw(self.board)
            self.width = self.board.size[0] # ширина доски
            self.height = self.board.size[1] # длина доски
            self.pix = self.board.load() 
            self.coord = [] # координаты(точки) для фигур
            

    # под конец self.board.save('ans.jpg','JPEG')
    # del self.draw
