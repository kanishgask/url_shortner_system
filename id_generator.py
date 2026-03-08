class IDGenerator:

    def __init__(self):
        self.current_id = 0

    def generate_id(self):
        self.current_id += 1
        return self.current_id


# Demo
if __name__ == "__main__":
    gen = IDGenerator()

    print(gen.generate_id())
    print(gen.generate_id())
