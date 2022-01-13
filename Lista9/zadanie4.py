import numpy as np
import matplotlib.pyplot as plt

langs = ["Python","C","Java","C++","C#","Visual Basic","JavaScript","Assembly Language","SQL","Swift"]
ratings = [13.58,12.44,10.66,8.29,5.68,4.74,2.09,1.85,1.80,1.41]


fig, ax = plt.subplots()

hbars = ax.barh(np.arange(len(langs)), ratings, align='center')
ax.set_yticks(np.arange(len(langs)), labels=langs)
ax.set_xlabel('Oceny')
ax.set_title('10 najpopularniejszych języków programowania')

plt.show()