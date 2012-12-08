node1 = dict(
    Heading = "A node with a link",
    Body = "[[http://google.com][Google]]\n")

node2 = dict(
    Heading = "A node with [[http://google.com][a link]]",
    Body = "")

node3 = dict(
    Heading = "A node with a raw link http://google.com",
    Body = "")

node4 = dict(
    Heading = "A node with [some brackets]",
    Body = "")

node5 = dict(
    Heading = "A node without TODO keyword",
    Body = "")

node6 = dict(
    Heading = "A node with a colon: and some text",
    Body = "")

data = [node1, node2, node3, node4, node5, node6]
