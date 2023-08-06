=========
glowseeds
=========

A package to find seeds and count their fluorescence in paired brightfield and fluorescence images. Intended to be a wrapped package within an R package

Installation
============

``pip install glowseeds``



Use
===

There are two user functions:

- `glowseeds.pixel_values('image.jpg')`, which returns an array of pixel values of the black and white version of the image.
- `glowseeds.do("bf_image.jpg", "fl_image.jpg", figure_directory="outfigs")`, which returns a pandas array of intensity values for found seeds and outputs found object summary image as a side effect.