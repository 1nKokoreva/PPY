# __str__ - reprezentacja napisowa listy – wszystkie elementy listy
# get(self, e) – zwraca element,
# delete(self,e) – usuwa wskazany element,
# append (self, e, func=None) – dodaje elementy do listy w sposób posortowany.
# func – jaki będzie warunek sortownia – określi funkcja, jeżeli None – zwykłe porównanie 2 obiektów za pomocą >=
from typing import List
class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.nextE
        return ' | '.join(result)

    def get(self, e):
        current = self.head
        while current:
            if current.data == e:
                return current
            current = current.nextE
        return None

    def delete(self, e):
        current = self.head
        prev = None
        while current:
            if current.data == e:
                if prev:
                    prev.nextE = current.nextE
                    if not current.nextE:
                        self.tail = prev
                else:
                    self.head = current.nextE
                    if not current.nextE:
                        self.tail = None
                self.size -= 1
                return
            prev = current
            current = current.nextE
        raise ValueError('***Error null')

    def append(self, e, func=None):
        if not self.head:
            self.head = Element(e)
            self.tail = self.head
        else:
            if not func:
                func = lambda a, b: a >= b
            current = self.head
            prev = None
            while current and not func(current.data, e):
                prev = current
                current = current.nextE
            new_element = Element(e, current)
            if prev:
                prev.nextE = new_element
            else:
                self.head = new_element
            if not current:
                self.tail = new_element
        self.size += 1

