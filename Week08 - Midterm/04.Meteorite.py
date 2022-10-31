'''Meteorite hit your property? Better Call Saul!!!'''

def metero(weight, spread, safeweight):
    '''Saul Goodman, Justice for you!'''
    count, times = 0, 0
    while weight >= safeweight:
        count += spread ** times
        weight = weight / spread
        times += 1
    print(int(count))

metero(float(input()), float(input()), float(input()))
