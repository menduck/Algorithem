import sys
import itertools
N,M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
sort_cards = sorted(cards, reverse=True)
three_card = list(itertools.combinations(sort_cards,3))
three_sum_conbination = list(map(sum,three_card))
under_M_list = list(filter(lambda x:x <=M, three_sum_conbination))
print(max(under_M_list))