#!/usr/bin/env python
# coding: utf-8

import PIL.Image, PIL.ImageDraw, PIL.ImageFont, PIL.ImageEnhance, cStringIO, random

class Captcha:
    
    def set(self, width=50, height=30, fontsize=18, num=6, fontcolor=(0,0,0), bgcolor=(255, 255, 255), type='gif', noise=(10, '#001100')):
        im = PIL.Image.new("RGB", (width, height))
        draw = PIL.ImageDraw.Draw(im)
    
        for x in range(0, width):
            for y in range(0, height):
                draw.point((x, y), bgcolor)
    
        font = PIL.ImageFont.truetype(filename='D:/Fonts/3.ttf', size=fontsize)
        alphabet = '0123456789abcdefghijkmnpqrstuvwxyABCDEFGHJKMNPQRSTUVWXY'
        word = ''
        for i in range(num):
            word = word + alphabet[random.randint(0, len(alphabet) -1)]
        print random.randint(-(height/3), height/3),  height/3
        draw.text((3, random.randint(-(height/2), height/3)), word, font=font, fill=fontcolor)

        rand = random.randint(0, noise[0])
        for i in range(0, noise[0]):
            rand = random.randint(0, noise[0])
            draw.point([-20,20, random.randint(0, width), random.randint(0, height)], fill=noise[1])
        

        f = cStringIO.StringIO()
        im.save(f, type)
        f.seek(0)
        return word, f