{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOWl8IV9+a1SKy+FXTznByS"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "Libs"
      ],
      "metadata": {
        "id": "v2Rzpt8nuQdi"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "9WUjA68wuoQ9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7Hax6L5ct9he",
        "outputId": "046aef34-3a03-4e59-99d5-8eb3cc9dcfc7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m60.2/60.2 kB\u001b[0m \u001b[31m1.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m78.6/78.6 kB\u001b[0m \u001b[31m6.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m54.5/54.5 kB\u001b[0m \u001b[31m4.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.7/1.7 MB\u001b[0m \u001b[31m25.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Building wheel for SimpleWebSocketServer (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for typing (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for ushlex (setup.py) ... \u001b[?25l\u001b[?25hdone\n"
          ]
        }
      ],
      "source": [
        "!pip install plotly -q #quiet\n",
        "!pip install matplot -q"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip show matplot"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t72PqUBPusfA",
        "outputId": "e2cae04c-adfa-4dfb-a113-1f80abc53402"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Name: matplot\n",
            "Version: 0.1.9\n",
            "Summary: UNKNOWN\n",
            "Home-page: UNKNOWN\n",
            "Author: UNKNOWN\n",
            "Author-email: UNKNOWN\n",
            "License: UNKNOWN\n",
            "Location: /usr/local/lib/python3.10/dist-packages\n",
            "Requires: matplotlib, pyloco\n",
            "Required-by: \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip uninstall matplot -q"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dRIzVBKjvAtZ",
        "outputId": "3fb413ab-cde7-40f6-9d35-b2a6d775592e"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Proceed (Y/n)? Y\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install matplotlib==3.8.3 -q"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E3sFtUEEvHFq",
        "outputId": "dab7cf22-3974-4fbb-9245-38aaa492a4c2"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.6/11.6 MB\u001b[0m \u001b[31m24.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip show matplotlib"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KrTd4QWXvwj3",
        "outputId": "5dc8c5ce-1eca-4dbd-91b8-15ff5f774c51"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Name: matplotlib\n",
            "Version: 3.8.3\n",
            "Summary: Python plotting package\n",
            "Home-page: https://matplotlib.org\n",
            "Author: John D. Hunter, Michael Droettboom\n",
            "Author-email: matplotlib-users@python.org\n",
            "License: PSF\n",
            "Location: /usr/local/lib/python3.10/dist-packages\n",
            "Requires: contourpy, cycler, fonttools, kiwisolver, numpy, packaging, pillow, pyparsing, python-dateutil\n",
            "Required-by: arviz, datascience, fastai, geemap, imgaug, matplotlib-venn, missingno, mizani, mlxtend, music21, plotnine, prophet, pycocotools, seaborn, wordcloud, yellowbrick\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n"
      ],
      "metadata": {
        "id": "x62awU0cv3J4"
      },
      "execution_count": 11,
      "outputs": []
    }
  ]
}