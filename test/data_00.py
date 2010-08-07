keys1 = ['level', 'heading', 'todo', 'tags', 'tags_inher']
keys2 = ['level', 'heading']

def tags(nums):
    return set(['TAG%d'%i for i in nums])

data = [
    dict(zip(keys1, vals)) for vals in
    [[1, 'Heading (Level 1) 1', 'TODO1', tags([1]), tags(range(1,2))],
     [2, 'Heading (Level 2) 1', 'TODO2', tags([2]), tags(range(1,3))],
     [3, 'Heading (Level 3) 1', 'TODO3', tags([3]), tags(range(1,4))],
     [4, 'Heading (Level 4) 1', 'TODO4', tags([4]), tags(range(1,5))],
     ]
    ] + [
    dict(zip(keys2, vals)) for vals in
    [[2, 'Heading (Level 2) 2'],
     [2, 'Heading (Level 2) 3'],
     [1, 'Heading (Level 1) 2'],
     [2, 'Heading (Level 2) 4'],
     [2, 'Heading (Level 2) 5'],
     [1, 'Heading (Level 1) 3'],
     ]
    ]
