# This file MUST be configured in order for the code to run properly

# Make sure you put all your input images into an 'assets' folder. 
# Each layer (or category) of images must be put in a folder of its own.

# CONFIG is an array of objects where each object represents a layer
# THESE LAYERS MUST BE ORDERED.

# Each layer needs to specify the following
# 1. id: A number representing a particular layer
# 2. name: The name of the layer. Does not necessarily have to be the same as the directory name containing the layer images.
# 3. directory: The folder inside assets that contain traits for the particular layer
# 4. required: If the particular layer is required (True) or optional (False). The first layer must always be set to true.
# 5. rarity_weights: Denotes the rarity distribution of traits. It can take on three types of values.
#       - None: This makes all the traits defined in the layer equally rare (or common)
#       - "random": Assigns rarity weights at random. 
#       - array: An array of numbers where each number represents a weight. 
#                If required is True, this array must be equal to the number of images in the layer directory. The first number is  the weight of the first image (in alphabetical order) and so on...
#                If required is False, this array must be equal to one plus the number of images in the layer directory. The first number is the weight of having no image at all for this layer. The second number is the weight of the first image and so on...

# Be sure to check out the tutorial in the README for more details.                

CONFIG = [

    {
        'id': 2,
        'name': 'body',
        'directory': '01_Body_Trait',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 3,
        'name': 'hand',
        'directory': '02_Hand_Trait',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 4,
        'name': 'costume',
        'directory': '03_Costume_Trait',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 5,
        'name': 'bottom',
        'directory': '04_Bottom_Trait',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 6,
        'name': 'hand_prop',
        'directory': '05_Hand_Prop_Trait',
        'required': False,
        'rarity_weights': None,
    },
    {
        'id': 7,
        'name': 'head',
        'directory': '06_Head_Trait',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 8,
        'name': 'hair',
        'directory': '07_Hair_Trait',
        'required': True,
        'rarity_weights': None,
    },
        {
        'id': 9,
        'name': 'head_prop',
        'directory': '08_Head_Prop_Trait',
        'required': False,
        'rarity_weights': None,
    },
       {
        'id': 10,
        'name': 'eye',
        'directory': '09_Eye_Trait',
        'required': True,
        'rarity_weights': None,
    },
      {
        'id': 11,
        'name': 'glass',
        'directory': '10_Glasses_Trait',
        'required': False,
        'rarity_weights': None,
    },
      {
        'id': 12,
        'name': 'mouth',
        'directory': '11_Mouth_Trait',
        'required': True,
        'rarity_weights': None,
    },
      {
        'id': 13,
        'name': 'beard',
        'directory': '12_Beard_Trait',
        'required': False,
        'rarity_weights': None,
    },
]
