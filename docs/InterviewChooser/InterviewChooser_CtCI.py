import random

probs = [(1,9),
(2,8),
(3,6),
(4,12),
(5,8),
(6,10),
(7,9),
(8,14),
(9,8),
(10,11),
(11,6),
(12,11),
(13,8),
(14,7),
(15,7)]
''',
(16,26),
(17,26)]'''

random.shuffle(probs)

for chapter in probs:  
  print("%s%s%s" % (chapter[0], ".", random.randint(1, chapter[1])) )