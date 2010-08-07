from datetime import date, datetime
data = [
    dict(Heading = "Heading",
         Scheduled = date(2010, 8, 6),
         Deadline = date(2010, 8, 10),
         Properties = dict(Effort_ALL='0:10'),
         DateList = [date(2010, 8, 16)],
         RangeList = [
             (date(2010, 8, 7), date(2010, 8, 8)),
             (datetime(2010, 8, 9, 0, 30), datetime(2010, 8, 10, 13, 20)),
             ],
         )
    ]
