from collections import Counter


class Chapter3:
    def __init__(self):
        self.beginning = 372 ** 2
        self.end = 809 ** 2 + 1
        self.all_values = set()
        self.bad_values = set()
        self.values_with_duplicates = set()
        self.final_values = set()

    def get_numbers(self):
        for value in range(self.beginning, self.end):
            self.all_values.add(str(value))

    def search_bad_values(self):
        for value in self.all_values:
            res = all(i <= j for i, j in zip(value, value[1:]))
            if res is False:
                self.bad_values.add(value)

    def difference_between_sets(self):
        self.values_with_duplicates = self.all_values.difference(self.bad_values)

    def find_duplicates(self):
        for value in self.values_with_duplicates:
            single_values = [item for item, count in Counter(value).items() if count > 1]
            if len(single_values) == 2:
                self.final_values.add(value)
            else:
                pass
        # print(self.final_values)
        return len(self.final_values)


if __name__ == '__main__':
    chapter = Chapter3()
    chapter.get_numbers()
    chapter.search_bad_values()
    chapter.difference_between_sets()
    print(chapter.find_duplicates())
