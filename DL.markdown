---
title: |
  **Birla Institute of Technology and Science Pilani**\
  K.K. Birla Goa Campus\
  **AY 2021--22, Semester I**
---

::: {.center}
**Course Handout**
:::

## Course Metadata {#course-metadata .unnumbered}

::: {.center}
  ---------------- -----------------------------------------------------------------------
  Course Name      **Deep Learning**
  Course Code      CS F425
  IC Name          [Tirtharaj Dash](https://www.bits-pilani.ac.in/goa/tirtharaj/profile)
  IC Chamber No.   D-168
  Lecture modes    Board, PPT, Python-Notebooks
  ---------------- -----------------------------------------------------------------------
:::

## Scope and Objective of the course {#scope-and-objective-of-the-course .unnumbered}

Neural Networks has had a long and rich history, and the reincarnated
viewpoint has shifted towards "Deep Neural Networks\" or "Deep
Learning\", primarily due to, (a) availability of the large amount of
data, (b) extensive use of powerful graphics processors, (c)
availability of software libraries to facilitate deep network
implementations, and (d) significant involvement of industrial research
labs in deep learning research.

This course on "Deep Learning" would focus on the conceptual and
mathematical foundation and computational investigations of recent deep
models as part of a series of laboratory experiments and projects. For
instance, we will focus on newer convolutional neural networks such as
VGG Net, ResNet; various sequence models including attention-based
models such as transformers; and also we will touch upon graph
representation learning using graph neural networks.

At the end of this course, students should be able to (0) pose
real-world problems in deep learning, (1) source and prepare datasets,
(2) design suitable deep network architecture, (3) prepare input-output
representation (and encodings), (4) decide and design a suitable loss
function for training a deep network, (5) training and deploying deep
models.

## Book(s) {#books .unnumbered}

Primary textbooks:

1.  A. Zhang, Z.C. Lipton, M. Li, A.J. Smola, [Dive into Deep
    Learning](https://d2l.ai/index.html).

2.  Ian Goodfellow, Yoshua Bengio, Aaron Courville, [Deep
    Learning](http://www.deeplearningbook.org/front_matter.pdf), MIT
    Press.

3.  W.L. Hamilton, [Graph Representation Learning
    Book](https://www.cs.mcgill.ca/~wlh/grl_book/).

4.  Aggarwal, C. C. (2018). Neural networks and deep learning, Springer.

(Books 1--3 are available as free e-books. Book 4 is available in our
library.)\
Other good reference books include:

1.  Graves, A. (2012). Supervised sequence labelling with recurrent
    neural networks.

2.  Francois Chollet, Deep Learning with Python, Manning Publishers.

3.  E. Stevens, L. Antiga, T. Viehmann, Deep Learning with PyTorch,
    Manning Publishers.

We will also look at relevant papers from: [NeurIPS](https://nips.cc/),
[ICLR](https://iclr.cc/), [ICML](https://icml.cc/),
[IJCAI](https://www.ijcai.org/),
[AAAI](https://aaai.org/Conferences/AAAI/aaai.php).

## Course plan (Weeks: 'W', Labs: 'L') {#course-plan-weeks-w-labs-l .unnumbered}

In the following, we assume that the maximum number of available weeks
is **14**. At present, I have not yet created a crisp chapter-wise
reference materials for my lectures; I will be updating this information
soon.

Preliminaries

:   Shallow neural nets, cost function, search space, derivative based
    optimisation, gradient descent and its variants (stochastic,
    mini-batch, batch), effects of search hyperparameters, various
    learning algorithms: $\mathtt{SGD}$, $\mathtt{RMSProp}$,
    $\mathtt{Adam}$. [**\[W: 1--2, L: 1\]**]{style="color: blue"}

Multilayered Neural Nets

:   Multilayer perceptron (intuition and maths), width and depth of
    neural network, activation functions, parameter initialisation
    strategy, cost function, backpropagation using gradient descent
    (importance of chain rule of derivative), hyparparamter tuning,
    regularisation, dropout, dropconnect. [**\[W: 3--5, L:
    2\]**]{style="color: blue"}

Neural Nets for Computer Vision

:   Learning from visual data, convolution operation (intuition and
    maths), pooling, variants of convolution function, dense
    convolutional neural networks (DenseNets), backpropagation in
    convolutional neural networks, state-of-the-art CNN architectures,
    application to image classification and object detection. [**\[W:
    6--8, L: 3\]**]{style="color: blue"}

Neural Nets for Sequence Learning

:   Learning from sequential data, recurrence in input and recurrence in
    hidden layers, backpropagation through time, truncated
    backpropagation, problem of vanishing or exploding gradients in
    backpropagation, Long short-term memory cells, gated recurrent
    units, attention mechanism, Transformers, BERT [**\[W: 9--11, L:
    4--5\]**]{style="color: blue"}

Neural Nets for Representation Learning

:   Idea behind neural networks as representation learning machines,
    autoencoder (intuition and maths), under- and over-complete
    autoencoders, loss functions, learning in autoencoders, de-noising
    autoencoders, deep networks pretraining and autoencoder as a
    pretrained model, graph representation learning with graph neural
    networks. [**\[W: 12--13, L: 6\]**]{style="color: blue"}

Neural Nets for Generative Modeling

:   Intuition behind learning probability distribution in neural
    networks, variational autoencoders (VAE), $\beta$-VAE, restricted
    Boltzmann machine, energy function as joint probability
    distribution, generative adversarial networks (inutition and maths).
    [**\[W: 13--14, L: 7\]**]{style="color: blue"}

## Course Websites {#course-websites .unnumbered}

-   Classroom website: Google Classroom link

-   Lab website:
    [CS-F425_Deep-Learning](https://github.com/tirtharajdash/CS-F425_Deep-Learning).

I will update the lecture materials in both the places. Google classroom
page will be used for official course-related communications including
quizzes, scores and feedback.

## Evaluation Scheme {#evaluation-scheme .unnumbered}

::: {.center}
  **Component**         **Mark**        **Type**
  -------------------- ---------- --------------------
  Midsem Exam              30      Open Book (Online)
  Lab Assignment 1         10             -NA-
  Lab Assignment 2         10             -NA-
  Major Project            20             -NA-
  Comprehensive Exam       30      Open Book (Online)
:::

-   Midsem exam and comprehensive exam will be in the form of Google
    quizzes unless otherwise specified and announced by AUGSD.

-   This course will be taken by Undergrads and Grad students (Masters
    and PhDs).

-   This evaluation scheme will apply to students from all degrees and
    streams, including Masters and PhDs.

## Course Notices {#course-notices .unnumbered}

All announcements will be made on the Google Classroom page.

## Attendence, Make-up and [Malpractice]{style="color: red"} Policies {#attendence-make-up-and-malpractice-policies .unnumbered}

-   Either come to all the lectures or don't come at all! Lectures have
    dependencies, so you miss out on one lecture; you may not understand
    anything in the lecture that follows.

-   Make-up shall be granted only in genuine cases based on individual's
    need and circumstances.

-   No marks for an evaluative component will be awarded without a
    make-up.

-   Malpractice policies are as per institute regulations.

## Chamber Consultation Hour {#chamber-consultation-hour .unnumbered}

I will notify this in the lecture. Note that I prefer email
communication, and [**NO phone call please!**]{style="color: red"}. Also
this means that when I send an email to you I expect a response. If you
wish to talk to me or discuss anything, just drop an email at
[tirtharaj\@goa.bits-pilani.ac.in](tirtharaj@goa.bits-pilani.ac.in) and
I should get back to you.
