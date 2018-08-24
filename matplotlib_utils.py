#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


def plot_tiles(images, rows=5, cols=5, gray=True):
    pos = 1
    plt.figure()
    for idx in range(rows * cols):
        plt.subplot(rows, cols, pos)
        img = images[idx]
        if gray:
            plt.imshow(img, cmap="gray")
        else:
            plt.imshow(img)
        plt.axis("off")
        pos += 1
    plt.show()
