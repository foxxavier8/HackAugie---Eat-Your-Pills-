class LcdApi:
    def __init__(self, num_lines, num_columns):
        self.num_lines = num_lines
        self.num_columns = num_columns
        self.cursor_x = 0
        self.cursor_y = 0

    def clear(self):
        raise NotImplementedError

    def move_to(self, cursor_x, cursor_y):
        self.cursor_x = cursor_x
        self.cursor_y = cursor_y

    def putchar(self, char):
        raise NotImplementedError

    def putstr(self, string):
        for char in string:
            self.putchar(char)