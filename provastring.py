#!/usr/bin/env python
import string, re, timeit

# Precomputed values (for str_join_set and translate)

letter_set = frozenset(string.ascii_lowercase + string.ascii_uppercase)
tab = string.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                       string.ascii_lowercase * 2)
deletions = ''.join(ch for ch in map(chr,range(256)) if ch not in letter_set)

s="A235th@#$&( er Ra{}|?>ndom"

def test_original(s):
    tmpStr = s.lower().strip()
    retStrList = []
    for x in tmpStr:
        if x in string.ascii_lowercase:
            retStrList.append(x)

    return ''.join(retStrList)


def test_regex(s):
    return re.sub('[^a-z]', '', s.lower())

def test_regex_closure(s):
  nonascii = re.compile('[^a-z]')
  def replacer(s):
    return nonascii.sub('', s.lower().strip())
  return replacer(s)


def test_str_join(s):
    return ''.join(c for c in s.lower() if c in string.ascii_lowercase)

def test_str_join_set(s):
    return ''.join(c for c in s.lower() if c in letter_set)

def test_filter_set(s):
    return filter(letter_set.__contains__, s.lower())

def test_filter_isalpha(s):
    return filter(str.isalpha, s).lower()

def test_filter_lambda(s):
    return filter(lambda x: x in string.ascii_lowercase, s.lower())

def test_translate(s):
    return string.translate(s, tab, deletions)

for test in sorted(globals()):
    if test.startswith("test_"):
        print "%30s : %s" % (test, timeit.Timer("f(s)", 
              "from __main__ import %s as f, s" % test).timeit(200000))

