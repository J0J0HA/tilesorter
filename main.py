from __future__ import annotations
from enum import Enum, auto
from cty import FixedLengthTuple, Array
from copy import deepcopy

k = 2


class HalberAffe(Enum):
    """
    Enum for Affe
    """

    RED_TOP = 0
    YELLOW_TOP = 1
    GREEN_TOP = 2
    BLUE_TOP = 3
    RED_BOTTOM = 4
    YELLOW_BOTTOM = 5
    GREEN_BOTTOM = 6
    BLUE_BOTTOM = 7

    def opposite(self) -> HalberAffe:
        """
        Returns the opposite Affe
        """
        return HalberAffe((self.value + k) % k)


type Tile = tuple[HalberAffe, HalberAffe, HalberAffe, HalberAffe]


def check(tile: Tile, top: Tile | None, left: Tile | None) -> bool:
    return (top is None or tile[0] == top[2].opposite()) and (left is None or tile[1] == left[3].opposite())


def backtrack(
    board: Array[Array[Tile]], tiles: set[Tile], index: int = 0
) -> bool | Array[Array[Tile]]:
    if index >= k * k:
        return board
    for tile in tiles:
        board[index % k][index // k] = tile
        if check(
            tile,
            board[(index % k) - 1][index // k] if index % k > 0 else None,
            board[index % k][index // k - 1] if index // k > 0 else None,
        ):
            rboard = backtrack(deepcopy(board), tuple(btile for btile in tiles if btile is not tile), index + 1)
            if rboard:
                return rboard
    return False


def main():
    tiles: FixedLengthTuple[Tile, 4 | 9 | 16] = (
        (
            HalberAffe.RED_TOP,
            HalberAffe.YELLOW_TOP,
            HalberAffe.GREEN_TOP,
            HalberAffe.BLUE_TOP,
        ),
        (
            HalberAffe.GREEN_BOTTOM,
            HalberAffe.YELLOW_BOTTOM,
            HalberAffe.GREEN_BOTTOM,
            HalberAffe.BLUE_BOTTOM,
        ),
        (
            HalberAffe.GREEN_TOP,
            HalberAffe.BLUE_BOTTOM,
            HalberAffe.RED_TOP,
            HalberAffe.YELLOW_TOP,
        ),
        (
            HalberAffe.RED_BOTTOM,
            HalberAffe.BLUE_TOP,
            HalberAffe.RED_BOTTOM,
            HalberAffe.YELLOW_BOTTOM,
        ),
    )
    annalenabaerboard: Array[Array[Tile]] = Array([Array[Tile](k) for _ in range(k)])
    print(backtrack(annalenabaerboard, tiles))


if __name__ == "__main__":
    main()
