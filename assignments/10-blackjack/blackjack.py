#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-03-21
Purpose: Rock the Casbah
"""

import argparse
import sys
import random
from itertools import product


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='"Blackjack" cardgame',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

    parser.add_argument(
        '-p', '--player_hits', help='A boolean flag', action='store_true')

    parser.add_argument(
        '-d', '--dealer_hits', help='A boolean flag', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    seed = args.seed
    player_hits = args.player_hits
    dealer_hits = args.dealer_hits
    suites = list('♥♠♣♦')
    num = list(str (j) for j in range(2, 11))
    char = list('JQKA')
    deck = sorted(list(product(suites, num + char)))

    card_value = {}
    card_value['A'] = 1
    value = 2
    for i in range(2, 11):
        card_value[str(i)] = value
        value += 1
    for c in 'JQK':
        card_value[c] = 10

    if seed is not None:
        random.seed(seed)
    random.shuffle(deck)

    P_card1 = deck.pop()
    D_card1 = deck.pop()
    P_card2 = deck.pop()
    D_card2 = deck.pop()

    P_hits_value = 0
    if player_hits:
        P_hits_card = deck.pop()
        P_hits_value = card_value[P_hits_card[1]]
    P_cards = P_card1[0] + P_card1[1] + ' ' + P_card2[0] + P_card2[1] + (' ' + P_hits_card[0] + P_hits_card[1] if player_hits else '')

    D_hits_value = 0
    if dealer_hits:
        D_hits_card = deck.pop()
        D_hits_value = card_value[D_hits_card[1]]
    D_cards = D_card1[0] + D_card1[1] + ' ' + D_card2[0] + D_card2[1] + (' ' + D_hits_card[0] + D_hits_card[1] if dealer_hits else '')

    P_value = card_value[P_card1[1]] + card_value[P_card2[1]] + P_hits_value
    D_value = card_value[D_card1[1]] + card_value[D_card2[1]] + D_hits_value

    print('D [{:>2}]: {}'.format(D_value, D_cards))
    print('P [{:>2}]: {}'.format(P_value, P_cards))

    if P_value > 21:
        print('Player busts! You lose, loser!')
        sys.exit(0)

    if D_value > 21:
        print('Dealer busts.')
        sys.exit(0)

    if P_value == 21:
        print('Player wins. You probably cheated.')
        sys.exit(0)

    if D_value == 21:
        print('Dealer wins!')
        sys.exit(0)

    if D_value < 18:
        print('Dealer should hit.')

    if P_value < 18:
        print('Player should hit.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
