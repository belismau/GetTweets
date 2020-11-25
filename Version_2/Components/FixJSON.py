import os

class FixJSON:
    def __init__(self, filename):
        self.filename = filename
        self.repair()
    
    def change_filename(self, cur, new):
        base = os.path.splitext(self.filename + cur)[0]
        os.rename(self.filename + cur, base + new)
    
    def create_empty_file(self):
        f = open(self.filename + '.txt', 'w')
        f.close()
    
    def add_new_content(self, content):
        f = open(self.filename + '.txt', 'a')
        f.write('[')
        for line in content:
            f.write(line)
        f.write(']')
        f.close()
    
    def add_comma_at_end(self, content):
        nr = 0
        for line in content:
            if line[-1:] == '\n':
                if nr != len(content) - 1:
                    content[nr] = line[:-1] + ',' + line[-1:]
            nr += 1
    
    def add_content_to_list(self):
        f = open(self.filename + '.txt', 'r')
        temp_list = []
        for line in f:
            temp_list.append(line)
        f.close()
        return temp_list

    def repair(self):
        # Change file from json to txt
        self.change_filename('.json', '.txt')

        content = self.add_content_to_list()
        self.add_comma_at_end(content)
        self.create_empty_file()
        self.add_new_content(content)

        # Change file back from txt to json 
        self.change_filename('.txt', '.json')