from dataclasses import dataclass
from enum import StrEnum, auto
from typing import List
from collections import defaultdict


class PieceType(StrEnum):
    KING = "k"
    QUEEN = "q"
    ROOK = "r"
    KNIGHT = "n"
    BISHOP = "b"
    PAWN = "p"


class PlayerType(StrEnum):
    WHITE = auto()
    BLACK = auto()


@dataclass
class Piece:
    player: PlayerType
    type: PieceType
    rank: int
    file: int

    def __str__(self):
        if self.player == PlayerType.WHITE:
            return self.type.upper()
        else:
            return self.type.lower()


@dataclass
class GameState:
    moves: int
    pieces: List[Piece]

    def __str__(self):
        output = ""
        tiles = defaultdict(lambda: defaultdict(lambda: "."))

        for piece in self.pieces:
            tiles[piece.rank][piece.file] = str(piece)

        for rank in range(8, 0, -1):
            for file in range(1, 9):
                output += tiles[rank][file]
            output += "\n"
        return output


INITIAL_GAME_STATE = GameState(
    moves=0,
    pieces=[
        Piece(
            player=PlayerType.WHITE,
            type=PieceType.ROOK,
            rank=1,
            file=1,
        ),
        Piece(
            player=PlayerType.WHITE,
            type=PieceType.KNIGHT,
            rank=1,
            file=2,
        ),
        Piece(
            player=PlayerType.WHITE,
            type=PieceType.BISHOP,
            rank=1,
            file=3,
        ),
        Piece(
            player=PlayerType.WHITE,
            type=PieceType.QUEEN,
            rank=1,
            file=4,
        ),
        Piece(
            player=PlayerType.WHITE,
            type=PieceType.KING,
            rank=1,
            file=5,
        ),
        Piece(
            player=PlayerType.WHITE,
            type=PieceType.BISHOP,
            rank=1,
            file=6,
        ),
        Piece(
            player=PlayerType.WHITE,
            type=PieceType.KNIGHT,
            rank=1,
            file=7,
        ),
        Piece(
            player=PlayerType.WHITE,
            type=PieceType.ROOK,
            rank=1,
            file=8,
        ),
        Piece(
            player=PlayerType.WHITE,
            type=PieceType.PAWN,
            rank=2,
            file=1,
        ),
        Piece(
            player=PlayerType.WHITE,
            type=PieceType.PAWN,
            rank=2,
            file=2,
        ),
        Piece(
            player=PlayerType.WHITE,
            type=PieceType.PAWN,
            rank=2,
            file=3,
        ),
        Piece(
            player=PlayerType.WHITE,
            type=PieceType.PAWN,
            rank=2,
            file=4,
        ),
        Piece(
            player=PlayerType.WHITE,
            type=PieceType.PAWN,
            rank=2,
            file=5,
        ),
        Piece(
            player=PlayerType.WHITE,
            type=PieceType.PAWN,
            rank=2,
            file=6,
        ),
        Piece(
            player=PlayerType.WHITE,
            type=PieceType.PAWN,
            rank=2,
            file=7,
        ),
        Piece(
            player=PlayerType.WHITE,
            type=PieceType.PAWN,
            rank=2,
            file=8,
        ),
        Piece(
            player=PlayerType.BLACK,
            type=PieceType.PAWN,
            rank=8,
            file=1,
        ),
        Piece(
            player=PlayerType.BLACK,
            type=PieceType.KNIGHT,
            rank=8,
            file=2,
        ),
        Piece(
            player=PlayerType.BLACK,
            type=PieceType.BISHOP,
            rank=8,
            file=3,
        ),
        Piece(
            player=PlayerType.BLACK,
            type=PieceType.QUEEN,
            rank=8,
            file=4,
        ),
        Piece(
            player=PlayerType.BLACK,
            type=PieceType.KING,
            rank=8,
            file=5,
        ),
        Piece(
            player=PlayerType.BLACK,
            type=PieceType.BISHOP,
            rank=8,
            file=6,
        ),
        Piece(
            player=PlayerType.BLACK,
            type=PieceType.KNIGHT,
            rank=8,
            file=7,
        ),
        Piece(
            player=PlayerType.BLACK,
            type=PieceType.ROOK,
            rank=8,
            file=8,
        ),
        Piece(
            player=PlayerType.BLACK,
            type=PieceType.PAWN,
            rank=7,
            file=1,
        ),
        Piece(
            player=PlayerType.BLACK,
            type=PieceType.PAWN,
            rank=7,
            file=2,
        ),
        Piece(
            player=PlayerType.BLACK,
            type=PieceType.PAWN,
            rank=7,
            file=3,
        ),
        Piece(
            player=PlayerType.BLACK,
            type=PieceType.PAWN,
            rank=7,
            file=4,
        ),
        Piece(
            player=PlayerType.BLACK,
            type=PieceType.PAWN,
            rank=7,
            file=5,
        ),
        Piece(
            player=PlayerType.BLACK,
            type=PieceType.PAWN,
            rank=7,
            file=6,
        ),
        Piece(
            player=PlayerType.BLACK,
            type=PieceType.PAWN,
            rank=7,
            file=7,
        ),
        Piece(
            player=PlayerType.BLACK,
            type=PieceType.PAWN,
            rank=7,
            file=8,
        ),
    ],
)
