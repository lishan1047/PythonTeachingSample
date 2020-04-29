'''
This is a sample of sorting.

'''
import pypinyin

class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city
    def __str__(self):
        return "姓名: %s, 城市: %s\n" % (self.name, self.city)
    __repr__ = __str__
    def hanzi_to_pinyin(self, city):
        return pypinyin.pinyin(self.name)
    def __lt__(self, other):
        return pypinyin.pinyin(self.name) < pypinyin.pinyin(other.name)

demo = []
demo.append(Person("赵","成都"))
demo.append(Person("钱","上海"))
demo.append(Person("孙","北京"))
demo.append(Person("李","上海"))
print(demo)
demo.sort()
print("sort:\n", demo)