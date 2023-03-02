'''
Реализуйте итератор колоды карт (52 штуки) CardDeck
Каждая карта представлена в виде строки типа "2 Пик". При вызове функции next()
Будет возвращаться следующая карта. "3 Пик "...
По окончании перебора всех элементов выводится сообщения "Колода закончилась"
'''


class CardDeck:

    def __init__(self):
        self.Deck = 52
        self.card = 0
        self.colors = ['Пик', 'Черви', 'Буби', 'Крести']
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз']

    def __next__(self):
        if self.card < self.Deck:
            color = self.colors[self.card // len(self.cards)]
            card = self.cards[self.card % len(self.cards)]
            self.card += 1
            return f'{card} {color}'
        else:
            print('Колода закончилась')
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    deck = CardDeck()
    for cart in deck:
        print(cart)


