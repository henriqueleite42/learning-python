# Inspired in https://www.instagram.com/p/CC7r6FJAXvk/

from matplotlib import pyplot
import numpy

# Dataset
dataset = ['INSTAGRAM', 'FACEBOOK', 'TWITTER', 'SNAPCHAT', 'LINKEDIN', 'REDDIT']
percentage = [27, 41, 15, 29, 18, 16]

# Create Chart
fig = pyplot.figure(figsize=(10, 7))
pyplot.pie(percentage, labels=dataset)

# Show
pyplot.show()
