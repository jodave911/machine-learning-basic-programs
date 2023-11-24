import pydotplus
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.tree import export_text
from sklearn.tree import export_graphviz
from io import StringIO
import pandas as pd
# Load the diabetes dataset from scikit-learn
data = pd.read_csv('diabetes.csv')
#diabetes = datasets.load()
X = data.drop('Outcome', axis=1)
y = data['Outcome']


# Create a decision tree classifier
clf = DecisionTreeClassifier()
clf = clf.fit(X, y)

from sklearn.tree import export_graphviz
import pydotplus
from IPython.display import Image

# Export the decision tree as a DOT file
dot_data = export_graphviz(clf, out_file=None, 
                           feature_names=X.columns,  
                           class_names=['No Diabetes', 'Diabetes'],
                           filled=True, rounded=True, special_characters=True)

# Create an image from the DOT data and save it as a PNG file
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png('diabetes.png')
