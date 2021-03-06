# http://statistics.about.com/od/Applications/a/Example-Of-Bootstrapping.htm
# https://www.thoughtco.com/example-of-bootstrapping-3126155

from statistics import mean
from random import choices

data = 1, 2, 4, 4, 10, 12, 19
means = sorted(mean(choices(data, k=7)) for i in range(210))
print(f'The sample mean of {mean(data):.1f} has a 90% confidence '
      f'interval from {means[1]:.1f} to {means[-2]:.1f}')

print(f'means = {means}')
