# app/utils.py

import os
from google.cloud import vision

client = vision.ImageAnnotatorClient()

def classify_image(img_path):
    with open(img_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    objects = client.object_localization(image=image).localized_object_annotations
    detected_objects = {obj.name.lower(): obj.score for obj in objects}

    labels = client.label_detection(image=image).label_annotations
    detected_labels = {label.description.lower(): label.score for label in labels}

    refined_results = detected_objects.copy()
    refined_results.update(detected_labels)

    # Limited set of animals to classify, could be extended.
    specific_animal_labels = [
        'dog', 'cat', 'lion', 'tiger', 'elephant', 'giraffe', 'zebra', 
        'kangaroo', 'koala', 'panda', 'bear', 'wolf', 'fox', 'rabbit', 
        'deer', 'horse', 'cow', 'sheep', 'goat', 'camel', 'dolphin', 
        'whale', 'shark', 'octopus', 'penguin', 'eagle', 'parrot', 
        'flamingo', 'peacock', 'sparrow', 'owl', 'hawk', 'snake', 
        'lizard', 'chameleon', 'frog', 'toad', 'butterfly', 'bee', 
        'ant', 'spider','squirrel', 'fish', 'salmon', 'trout', 'piranha', 
        'tuna', 'goldfish', 'carp', 'bird'
    ]

    for animal in specific_animal_labels:
        if animal in refined_results:
            return animal, refined_results[animal]

    return None, None
