#!/usr/bin/python  
# -*- coding:utf8 -*-  

'''
coding date:2018-08-12
modify date:2018-09-13
author:TTang
'''

import colorsys

def get_color(image):

    # initialize parameters
    max_score = None
    dominant_color = None

    # convert image into RGBA mode
    image = image.convert('RGBA')
    image.thumbnail((20, 20))

    # get the value of R,G,B,A chanel
    for count, (r, g, b, a) in image.getcolors(image.size[0] * image.size[1]):
        if a == 0:
            continue

        # convert RGB mode into HSV mode
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]

        # compute saturation
        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
        y = (y - 16.0) / (235 - 16)

        # get final RGB according to saturation
        if y > 0.9:
            continue
        score = (saturation + 0.1) * count

        if score > max_score:
            max_score = score
            dominant_color = (r, g, b)

    return dominant_color