from lollercoaster.columns import Column, pattern_types
import random


class ColumnBuilder(object):
    def __init__(self, max_height):
        self.x = 0
        self.max_height = max_height
        self.last_column = None

    def create_initial_column(self):
        self.x = 0
        initial_height = random.randint(0, self.max_height)
        current_type = random.randint(-1, 1)
        self.last_column = Column(initial_height, current_type, self.max_height)
        self.last_column.fill(pattern_types[self.x % 3])
        return self.last_column

    def create_next_column(self):
        self.x += 1
        height = self.last_column.height
        last_type = self.last_column.column_type

        current_type = random.randint(-1, 1)

        if last_type == 1:
            height += 1

        if current_type == -1:
            if height == 0:
                current_type = 0
            height += current_type

        if current_type == 1 and height == self.max_height - 2:
            current_type = 0

        self.last_column = Column(height, current_type, self.max_height)
        self.last_column.fill(pattern_types[self.x % 3])
        return self.last_column


class LollerCoaster(object):
    def __init__(self, column_count, max_height):
        self.column_count = column_count
        self.builder = ColumnBuilder(max_height)
        self.max_height = max_height

        self.columns = [self.builder.create_initial_column()]
        for count in xrange(1, self.column_count):
            self.columns.append(self.builder.create_next_column())

        self.draw_cart()

    def __repr__(self):
        # Fill the rows, starting at the top working down
        output = ""
        for c in range(self.max_height):
            for col in self.columns:
                output += col.retrieve_row(self.max_height - c - 1)
            output += "\n"

        return output

    def cycle(self):
        self.columns = self.columns[1:]
        self.columns.append(self.builder.create_next_column())
        self.draw_cart()
        return self

    def draw_cart(self):
        for col in self.columns:
            col.revert_top()

        lollercoaster = "ROFLOLOLOL"
        for i, c in enumerate(lollercoaster):
            self.columns[i + 30].change_top(c)

