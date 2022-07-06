import subprocess
import subprocess as sp
# sp.call('ls -l')
# sp.call('\\dev\\bin\\atlas.cmd')
lst = sp.call('dir')
print(lst)
