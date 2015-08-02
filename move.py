import re
class move:

    def __init__(self, token, row = -1, index = -1, string = ""):
        if ":" in string:
            matched = re.compile("([0-9]+),([0-9]+):([0-9]+),([0-9]+)").match(string)
            self.row = int(matched.group(1))
            self.index = int(matched.group(2))
            self.take_row = int(matched.group(3))
            self.take_index = int(matched.group(4))
        elif string != "":        
            matched = re.compile("([0-9]+),([0-9]+)").match(string)
            self.row = int(matched.group(1))
            self.index = int(matched.group(2))
            self.take_row = -1
            self.take_index = -1
        else:
            self.row = row
            self.index = index
        self.token = token        
        return
