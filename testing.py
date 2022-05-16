def hello():
    print("outer")

    def hi():
        print("inner")

    return hi


a = hello()
a()
