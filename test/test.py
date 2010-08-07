import os
from glob import glob
from nose.tools import eq_

from Orgnode import Orgnode, makelist, get_daterangelist, get_datetime

TESTDIR = os.path.dirname(__file__)

def value_from_data_key(node, key):
    """
    Helper function for check_data. Get value from Orgnode by key.
    """
    if key == 'Tags_inher':
        return node.Tags(inher=True)
    else:
        return node.__getattribute__(key)()

def check_data(dataname):
    """Helper function for test_data"""
    oname = os.path.join(TESTDIR, dataname + '.org')
    data = __import__(dataname).data
    nodelist = makelist(oname)

    for (i, (node, kwds)) in enumerate(zip(nodelist, data)):
        for key in kwds:
            val = value_from_data_key(node, key)
            eq_(kwds[key], val,
                msg=('check value of %d-th node of key "%s" from "%s". '
                     'Orgnode.%s() = "%s" != "%s".'
                     ) % (i, key, oname, key.title(), val, kwds[key]))

def test_data():
    """
    Compare parsed data from 'data_*.org' using Orgnode and desired data
    which is described in 'data_*.py'.
    """
    for oname in glob(os.path.join(TESTDIR, 'data_*.org')):
        dataname = os.path.basename(oname)[:-4]
        yield (check_data, dataname)


def test_get_daterangelist():
    datefmt0 = "<%(Y)04d-%(M)02d-%(D)02d %(d)s>"
    datefmt1 = "<%(Y)04d-%(M)02d-%(D)02d %(d)s %(h)02d:%(m)02d>"

    dates = [
        dict(Y=2010, M=6, D=21, d='Mon', h=12, m=0),
        dict(Y=2010, M=6, D=21, d='Mon', h=13, m=0),
        dict(Y=2010, M=6, D=21, d='Mon', h=None, m=None),
        ]

    datestr = " ".join([
        datefmt1 % dates[0],
        datefmt1 % dates[1],
        datefmt0 % dates[2],
        ("%s--%s" % (datefmt1 % dates[0], datefmt1 % dates[1]) )
        ])

    desired_datelist = [ get_datetime(d['Y'], d['M'], d['D'], d['h'], d['m'])
                         for d in dates ]
    d0 = dates[0]
    d1 = dates[1]
    desired_rangelist = [
        (get_datetime(d0['Y'], d0['M'], d0['D'], d0['h'], d0['m']),
         get_datetime(d1['Y'], d1['M'], d1['D'], d1['h'], d1['m']))]

    for context in ["%s", " %s", "%s ", "aaa%sbbb"]:
        (datelist, rangelist) =  get_daterangelist(context % datestr)
        for (des, act) in zip(desired_datelist, datelist):
            assert des == act
        for (des, act) in zip(desired_rangelist, rangelist):
            assert des == act
