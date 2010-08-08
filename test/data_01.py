from datetime import date, datetime
node1 = dict(
    Heading = "A node with a lot of attributes",
    Scheduled = date(2010, 8, 6),
    Deadline = date(2010, 8, 10),
    Closed = datetime(2010, 8, 8, 18, 0),
    Clock = [
        (datetime(2010, 8, 8, 17, 40), datetime(2010, 8, 8, 17, 50), 10),
        (datetime(2010, 8, 8, 17, 00), datetime(2010, 8, 8, 17, 30), 30),
        ],
    Properties = dict(Effort=70),
    DateList = [date(2010, 8, 16)],
    RangeList = [
        (date(2010, 8, 7), date(2010, 8, 8)),
        (datetime(2010, 8, 9, 0, 30), datetime(2010, 8, 10, 13, 20)),
        ],
    Body = """\
  - <2010-08-16 Mon> DateList
  - <2010-08-07 Sat>--<2010-08-08 Sun>
  - <2010-08-09 Mon 00:30>--<2010-08-10 Tue 13:20> RangeList
"""
    )
node2 = dict(
    Heading = "A node without any attributed",
    Scheduled = "",
    Deadline = "",
    Closed = "",
    Clock = [],
    Properties = {},
    DateList = [],
    RangeList = [],
    Body = ""
    )

data = [node1, node2, node1]
