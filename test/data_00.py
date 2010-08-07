keys1 = ['level', 'heading', 'tags', 'todo']
keys2 = ['level', 'heading']
data = [
    dict(zip(keys1, vals)) for vals in
    [[1, 'Heading (Level 1) 1', ['TAG1'], 'TODO1'],
     [2, 'Heading (Level 2) 1', ['TAG2'], 'TODO2'],
     [3, 'Heading (Level 3) 1', ['TAG3'], 'TODO3'],
     [4, 'Heading (Level 4) 1', ['TAG4'], 'TODO4'],
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
