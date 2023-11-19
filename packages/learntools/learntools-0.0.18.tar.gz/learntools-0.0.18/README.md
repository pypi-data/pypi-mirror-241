# LearnTools

### Stucture
 - Network
    - network (class to hold network) (need to add more insightful prints)
    - layer_dense (dense layer from layer class)
    - layer_one_to_one
    - layer_dropout
    - activation_function (custom activation function class)
    - relu / softmax / sigmoid (standard activation functions)

    - layer_conv WIP
    - layer_norm WIP (or perhaps a function to normalise data)
 - Learning
    - random_learning 
    - random_momentumn_learning

    - random_evolution_learning WIP
    - random_stochastic_learning (batch random) WIP
    - gradient descent WIP
    - stochastic gradient descent WIP
     WIP

### Improvements
 - Making printing nicer
 - Make learning a class instead of a function
    - Loss is maintained as a attribute
    - alongisde other useful data
 - Add a layer without a bias
 - Add just a bias layer
 - Learning function that remove least important weights

# Getting started
run the command *pip install learntools*\
for network use *from learntools import Network*\
for learning use *from learntools import Learning*

### Note to Self
 - Setup Venv
    - install wheel, twine
 - To upload package
 - build dist:
    - rmdir /s /q build dist learntools.egg-info
    - python setup.py sdist bdist_wheel
 - upload dist:
    - twine upload dist/*

 - To Build Documentation: https://realpython.com/python-project-documentation-with-mkdocs/#:~:text=Build%20Your%20Python%20Project%20Documentation%20With%20MkDocs%201,Step%203%3A%20Write%20and%20Format%20Your%20Docstrings%20