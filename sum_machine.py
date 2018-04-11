class SumMachine(object):
    def do_your_stuff(self, x, y):
	types = (int, long, float)
	if isinstance(x, types) and isinstance(y, types):
            return x+y
        else:
	    raise ValueError
