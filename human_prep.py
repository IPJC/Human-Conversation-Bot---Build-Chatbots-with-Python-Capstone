from itertools import zip_longest
import re

data_path = "human_chat.txt"

# Defining lines as a list of each line
with open(data_path, 'r', encoding='utf-8') as f:
  lines = f.read().split('\n')

lines = [re.sub(r"Human\s\d:", "", line).strip() for line in lines]
lines = [re.sub(r"<REDACTED_TERM>", "", line).strip() for line in lines]

# group lines by response pair

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)
pairs = list(grouper(lines, 2))
#print(pairs)
