#!/usr/bin/env python3
import sys
from collections import defaultdict
import bisect

def solve():
    n, p = map(int, sys.stdin.readline().split())

    # board definition (last square = multicolored, index n-1)
    board = [sys.stdin.readline().strip() for _ in range(n-1)]

    # lookup structures
    color_positions = defaultdict(list)
    special_pos = {}
    for i, sq in enumerate(board):
        if sq.startswith("SPECIAL"):
            special_pos[sq] = i
        else:
            color_positions[sq].append(i)
    # final multicolored square has index n-1
    final_square = n - 1

    # every color can also "land" on the final multicolored square
    for col in color_positions:
        color_positions[col].append(final_square)

    # read deck
    c = int(sys.stdin.readline())
    deck = []
    for _ in range(c):
        parts = sys.stdin.readline().split()
        t = int(parts[0])
        val = parts[1]
        deck.append((t, val))

    # simulation
    positions = [-1] * p   # starting before square 0
    turn = 0
    deck_pos = 0

    while True:
        player = turn % p
        card_type, val = deck[deck_pos]
        deck_pos = (deck_pos + 1) % c

        if card_type == 1 or card_type == 2:
            k = card_type
            arr = color_positions[val]
            # find k-th occurrence after current position
            idx = bisect.bisect_right(arr, positions[player])
            if idx + k - 1 < len(arr):
                newpos = arr[idx + k - 1]
            else:
                newpos = final_square
            positions[player] = newpos
        else:  # special
            positions[player] = special_pos[val]

        if positions[player] == final_square:
            print(player + 1)
            return

        turn += 1

if __name__ == "__main__":
    solve()