# -*- coding: utf-8 -*-
"""Holds function that read context from tab separated txt file"""

import csv
import fca

def read_txt(path):
    """Read context from path, which is tab separated txt file

    Format
    ======

    First line is tab separated attributes' names
    Next an empty line
    Then tab separated 1 and 0, each line corresponds to one object.

    Examples
    ========

    Load example file from tests directory

    >>> c = read_txt('tests/context.txt')
    >>> len(c)
    4
    >>> len(c[0])
    4
    >>> for o in c:
    ...     print o
    ...
    [True, False, False, True]
    [True, False, True, False]
    [False, True, True, False]
    [False, True, True, True]
    >>> print c.objects
    ['g1', 'g2', 'g3', 'g4']
    >>> print c.attributes
    ['a', 'b', 'c', 'd']

    """
    input_file = open(path, "rb")
    rdr = csv.reader(input_file, delimiter="\t")
    rec = rdr.next() # read attributes names

    attributes = []
    for attr in rec:
        attributes.append(str(attr).strip())
    
    rdr.next() # empty line
    
    table = []
    for rec in rdr:
        line = []
        for num in rec:
            if num == "0":
                line.append(False)
            elif num == "1":
                line.append(True)
        table.append(line)
    input_file.close()
    # i + 1 ? 
    objects = ["".join(["g", str(i + 1)]) for i in range(len(table))]

    # TODO: It's hack
    # Strange things happen with csv in case of non standard characters
    if len(attributes) != len(table[0]):
        input_file = open(path, "rb")
        attributes = input_file.readline().split("\t")[:-1]
        input_file.close()

    return fca.Context(table, objects, attributes)


def read_mv_txt(path):
    """Read many-valued context from path, which is tab separated txt file

    Format
    ======

    First line is tab separated attributes' names
    Next an empty line
    Then tab separated values, each line corresponds to one object.

    Examples
    ========

    Load example file from tests directory

    >>> c = read_mv_txt('tests/table.txt')
    >>> len(c)
    3
    >>> len(c[0])
    3
    >>> for o in c:
    ...     print o
    ...
    ['5', '6', '7']
    ['7', '2', '9']
    ['7', '3', '4']
    >>> print c.objects
    ['g1', 'g2', 'g3']
    >>> print c.attributes
    ['attr1', 'attr2', 'attr3']

    """
    input_file = open(path, "rb")
    rdr = csv.reader(input_file, delimiter="\t")
    rec = rdr.next() # read attributes names

    attributes = []
    for attr in rec:
        attributes.append(str(attr).strip())
    
    rdr.next() # empty line
    
    table = []
    for rec in rdr:
        line = []
        for num in rec:
            line.append(num)
        table.append(line)
    input_file.close()
    # i + 1 ? 
    objects = ["".join(["g", str(i + 1)]) for i in range(len(table))]

    # TODO: It's hack
    # Strange things happen with csv in case some of "non standard" characters
    if len(attributes) != len(table[0]):
        input_file = open(path, "rb")
        attributes = input_file.readline().split("\t")[:-1]
        input_file.close()

    return fca.ManyValuedContext(table, objects, attributes)
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()