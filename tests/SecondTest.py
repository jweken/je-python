# %% [markdown]
# # What is this
#
# This is a .ipynb file also known as a ## Jupyter file.
# Note: The above ## does only translate to a heading if
# used at the start of a line.
# ___

# %% [markdown]
#
# ## Jupyter files can execute code.
# ### Some Sample Code
#
# How does that work ?

# %%
# you start with a comment
# you type some code
# you execute the code.

import time
import sys


msg = "Hello World"
print(msg)
print()
# print(sys.paths) # this produces an error
for all in sys.path:
    print(all)

# %%
# show some time 'things'


def GetDateTime():
    return time.asctime()


x = GetDateTime()
print(x)
print(time.gmtime())


# %% [markdown]
# ___

# %% [markdown]
# ## Where can I find more Notebooks

# %% [markdown]
# ## Links
#
# * time on [Python.org](<https://docs.python.org/3/library/time.html#module-time>)
