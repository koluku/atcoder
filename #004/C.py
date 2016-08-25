N = int(input())
cards = ['1', '2', '3', '4', '5', '6']

for i in range(N % 30):
    a = cards[i % 5]
    cards[i % 5] = cards[ i % 5 + 1]
    cards[ i % 5 + 1] = a

print(cards[0] + cards[1] + cards[2] + cards[3] + cards[4] + cards[5])
