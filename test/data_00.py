def nodedict(i, level, todo='', tags=set([]), tags_inher=set([])):
    return dict(
        heading="Heading %d"%i, level=level, tags=tags, tags_inher=tags_inher)

def tags(nums):
    return set(['TAG%d'%i for i in nums])

data = [
    nodedict(i, *vals) for (i, vals) in enumerate(
        [[1, 'TODO1', tags([1]), tags(range(1,2))],
         [2, 'TODO2', tags([2]), tags(range(1,3))],
         [3, 'TODO3', tags([3]), tags(range(1,4))],
         [4, 'TODO4', tags([4]), tags(range(1,5))],
         [2, '', tags([]), tags([1])],
         [2, '', tags([]), tags([1])],
         [1, '', tags([2]), tags([2])],
         [2, '', tags([2]), tags([2])],
         [3, '', tags([]), tags([2])],
         [5, '', tags([3,4]), tags([2,3,4])],
         [4, '', tags([1]), tags([1,2])],
         [2, '', tags([]), tags([2])],
         [1],
         ])
    ]
