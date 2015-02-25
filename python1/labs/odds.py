#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse
import random
from datetime import datetime
from math import factorial


DRAWS_PER_YEAR = 104
DEFAULT_MAX_BALL_NUM = 50
DEFAULT_YEARS = 1
DEFAULT_NUM_PICKS = 6


def calc_odds(max_ball_num, num_picks):
    ''' Calculates odds the simple way. '''

    odds = 1
    for x in xrange(num_picks):
        odds *= (max_ball_num - x) / (num_picks - x)
    return odds

def calc_odds2(max_ball_num, num_picks):
    ''' Calculates odds the official wikipedia way. '''

    return factorial(max_ball_num) / (factorial(num_picks) * (factorial(max_ball_num-num_picks)))

def generate_results(max_ball_num, drawings, picks):
    ''' Generate random results for each drawing and compare them to the picks '''

    begin = datetime.now()
    results = {x:0 for x in xrange(len(picks) + 1)}
    for x in xrange(drawings):
        draw = [random.randrange(1,50) for x in xrange(len(picks) + 1)]
        count = 0
        for x in picks:
            if x in draw:
                count += 1
        results[count] += 1
    end = datetime.now()

    return results, (end - begin).total_seconds()

def print_results(drawings, max_ball_num, picks, quick_pick):
    ''' Prints out the lottery results and calculates odds '''

    results, elapsed = generate_results(args.max_ball_num,
                                        drawings,
                                        picks)
                                            

    results_formatted = str()
    for x in xrange(len(picks) + 1):
        results_formatted += "{0:>4d}{1}{2:>3d}{3}{4:>7.3f}\n".format(x,
                                                                    " " * 9,
                                                                    results[x],
                                                                    " " * 7,
                                                                    results[x]/float(drawings) * 100)

    output = """

Results for {0} drawings - {1} out of {2}
Selected Numbers = {3}
Odds of matching all numbers: 1 in {4}

# Matches    Count     Percentage
=========    =====     ==========
{5}

Ran {0} simultations in {6} seconds
For a twice-a-week lotto system, that would be the equivalent
of {7} years worth of drawings.
""".format(drawings,
           len(picks),
           max_ball_num,
           picks,
           calc_odds2(max_ball_num, len(picks)),
           results_formatted,
           elapsed,
           drawings/104.)

    print output

    return 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lottery Odds Generator')
    parser.add_argument("-b", "--max_ball_num",
                        help='Max number of an individual ball',
                        default=DEFAULT_MAX_BALL_NUM)
    parser.add_argument("-d", "--drawings",
                        help='Number of drawings being performed',
                        type=int,
                        default=104)
    parser.add_argument("-n", "--num_picks",
                        help="Number of balls pick in a single drawing",
                        type=int,
                        default=DEFAULT_NUM_PICKS)
    parser.add_argument("-p", "--picks",
                        help="A list of picked numbers (comma seperated, no spaces)")
    parser.add_argument("-q", "--quick_pick",
                        help="Whether or not to randomly generate picks",
                        type=bool,
                        default=True)
    parser.add_argument("-y", "--years",
                        help='Number of years to calculate for.',
                        default=DEFAULT_YEARS)
 
    args = parser.parse_args()

    if args.quick_pick == True:
        picks = [random.randrange(1,50) for x in xrange(args.num_picks)]
    else:
        picks = args.picks

    print_results(drawings=args.drawings,
                  max_ball_num=args.max_ball_num,
                  picks=picks,
                  quick_pick=args.quick_pick)
