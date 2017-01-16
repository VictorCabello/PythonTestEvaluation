# coding=UTF-8
import csv
import string


FILE_INDEX = 0
RANK_INDEX = 1


class Piece(object):
    """
    A simple representation of a chess piece.
    """
    def __init__(self, initial_position, color,  board):
        self.board = board
        self.set_possition(initial_position)

    def set_possition(self, position):
        board = self.board
        square_is_not_empty = not board.square_is_empty(position)
        if square_is_not_empty:
            raise Exception(
                "TODO: use better exception when the square is not empty")
        self.position = position
        board.files[position
                    [FILE_INDEX]][position[RANK_INDEX]] = self

    def move_to(self, position):
        valid_moves = self.get_valid_moves()
        if position not in valid_moves:
            raise Exception(
                "TODO: use better exception when an invalid movement " +
                "is performed")
        self.set_possition(position)
:
    def get_valid_moves(self):
        raise NotImplementedError('This piece does not have movement rules')

    def __repr__(self):
        return self.char_repr


class King(Piece):
    """
    Representation of a King
    """
    def __init__(self, initial_position, color,  board):
        super(King, self).__init__(initial_position, color, board)
        self.char_repr = '♔' if color == 'white' else '♚'

    def get_valid_moves(self):
        position = self.position
        file = self.position[FILE_INDEX]
        file = string.lowercase.index(file)
        rank = int(position[RANK_INDEX])
        rank_len = 4
        valid_moves = []
        for n_file in range(file - 1, file + 1):
            if n_file > 0 and n_file < len(self.board):
                for n_rank in range(rank - 1, rank + 1):
                    if n_rank > 0 and n_rank < rank_len:
                        valid_moves.append((n_file, n_rank))
        raise NotImplementedError("test %s " % valid_moves)


class Qeen(Piece):
    """
    Representation of a Qeen
    """
    def __init__(self, initial_position, color,  board):
        super(Qeen, self).__init__(initial_position, color, board)
        self.char_repr = '♕' if color == 'white' else '♛'


class Knight(Piece):
    """
    Representation of a Knight
    """
    def __init__(self, initial_position, color,  board):
        super(Knight, self).__init__(initial_position, color, board)
        self.char_repr = '♘' if color == 'white' else '♞'


class Pawn(Piece):
    """
    Representation of a Pawn
    """
    def __init__(self, initial_position, color,  board):
        super(Pawn, self).__init__(initial_position, color, board)
        self.char_repr = '♙' if color == 'white' else '♟'


class Rock(Piece):
    """
    Representation of a Pawn
    """
    def __init__(self, initial_position, color,  board):
        super(Rock, self).__init__(initial_position, color, board)
        self.char_repr = '♖' if color == 'white' else '♜'


class Bishop(Piece):
    """
    Representation of a Bishop
    """
    def __init__(self, initial_position, color,  board):
        super(Bishop, self).__init__(initial_position, color, board)
        self.char_repr = '♗' if color == 'white' else '♝'


class ChessBoard(object):
    """
    A simple representation of a chess board.
    """
    def __init__(self):
        self.files = {}
        self.prepare_files()
        self.colors = ('white', 'black')

    def prepare_files(self):
        # Prepare files and ranks
        # + 1 to include h and 8
        for x_file in range(ord('a'), ord('h') + 1):
            x_file = chr(x_file)
            self.files[x_file] = {'%d' % i: None for i in range(2, 9 + 2)}

    def start_match(self, config_file_path):
        with open(config_file_path, 'r') as config_file:
            config_reader = csv.reader(config_file)
            header = config_reader.next()
            piece = header.index('Piece')
            _file = header.index('File')
            rank = header.index('Rank')
            color = header.index('Color')
            for row in config_reader:
                to_eval = "{piece}" .format(
                    piece=row[piece])
                class_ = eval(to_eval)
                class_((row[_file], row[rank]), row[color], self)
        config_file.close()

    def start_normal_match(self):
        self.start_match('config/normal_match.csv')

    def square_is_empty(self, position):
        _file = position[FILE_INDEX]
        rank = position[RANK_INDEX]
        return bool(self.files[_file][rank] is None)

    def __getitem__(self, row):
        return self.files[row]

    def __repr__(self):
        _return = ""
        _ranks = range(1, 8 + 1)
        _ranks = reversed(_ranks)
        for _rank in [str(i) for i in _ranks]:
            for _files in zip(*self.files):
                for _piece in [self.files[_file][_rank]
                               for _file in _files]:
                    _return += ' %s ' % _piece\
                               if _piece is not None else '...'
                _return += '\n'

        return _retur
