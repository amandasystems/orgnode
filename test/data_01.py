from datetime import date, datetime
data = [
    dict(Heading = "Heading",
         Scheduled = date(2010, 8, 6),
         Deadline = date(2010, 8, 10),
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
    ]
