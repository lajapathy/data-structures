
class MaxSizeList():
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []
    def push(self, value):
        if len(self.list) >= self.max_size:
            raise Exception("Max length exceeded")
        self.list.append(value)
    def get_list(self):
        return self.list

if __name__ == '__main__':
    main()

def main():
    a = MaxSizeList(5)
    print(type(a))
