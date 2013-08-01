Inliner inlines Python function calls.

    from inliner import inline

    @inline
    def add_stuff(x, y):
        return x + y

    def add_lots_of_numbers():
        results = []
        for i in xrange(10):
             results.append(add_stuff(i, i+1))

In the above code the add_lots_of_numbers function is converted into this:

    def add_lots_of_numbers():
        results = []
        for i in xrange(10):
             results.append(i + i + 1)