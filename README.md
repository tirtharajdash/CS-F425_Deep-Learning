## Welcome to CS F425 at BITS Pilani, Goa Campus!

| Primary Instructor (IC)   | [Tirtharaj Dash](https://www.bits-pilani.ac.in/goa/tirtharaj/profile) |
|---------------------------|---|
| Teaching Assistants (TAs) | [Atharv Sonwane](https://threewisemonkeys-as.github.io/) &nbsp;&nbsp;&nbsp; [Anmol Agarwal](https://www.linkedin.com/in/anmol-agarwal-041098/) &nbsp;&nbsp;&nbsp; [Ameya Laad](http://ameyalaad.github.io/) &nbsp;&nbsp;&nbsp; [Akhilesh Adithya](https://akhileshadithya.github.io/)|

Course handout can be found [here](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/DL_handout.pdf). 


## Scope and Objective of the course

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

## Book(s)

Primary textbooks:

1.  A. Zhang, Z.C. Lipton, M. Li, A.J. Smola, [Dive into Deep
    Learning](https://d2l.ai/index.html).
2.  Ian Goodfellow, Yoshua Bengio, Aaron Courville, [Deep
    Learning](http://www.deeplearningbook.org/front_matter.pdf), MIT
    Press.
3.  Aggarwal, C. C. (2018). Neural networks and deep learning, Springer.
4.  W.L. Hamilton, [Graph Representation Learning
    Book](https://www.cs.mcgill.ca/~wlh/grl_book/).

Other good reference books include:

1.  Graves, A. (2012). [Supervised sequence labelling with recurrent
    neural networks](https://www.cs.toronto.edu/~graves/preprint.pdf).
2.  Francois Chollet, [Deep Learning with
    Python](http://faculty.neu.edu.cn/yury/AAI/Textbook/Deep%20Learning%20with%20Python.pdf),
    Manning Publishers.
3.  E. Stevens, L. Antiga, T. Viehmann, [Deep Learning with
    PyTorch](https://pytorch.org/assets/deep-learning/Deep-Learning-with-PyTorch.pdf),
    Manning Publishers.

Textbook-3 is available in our library. Other books are available as
e-books as href-ed.\
Additioanlly, we may also look at relevant papers from
[NeurIPS](https://nips.cc/), [ICLR](https://iclr.cc/),
[ICML](https://icml.cc/), [IJCAI](https://www.ijcai.org/),
[AAAI](https://aaai.org/Conferences/AAAI/aaai.php). These will be
primarily used during major and minor projects design.


## Theory Materials

References to the relevent study materials are provided in the lecture slides and in some cases,
these are made available separately. 
Duration of each lecture is 50 min, which may get extended by 10-15 min. I am thankful to
my students for tolerating this aspect of my teaching.
The recoded videos of live lectures are accessible to the registered students only.
The slides and videos may not be in sync in some cases; that is, any slide may span
over multiple lecture slots.


| Lecture   | In-class Lecture | Extra Materials |
|-----------|------------------|-----------------|
| Lecture 0: Introducing the course | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture0.pdf), [video](https://drive.google.com/file/d/1QXLGrSHwjWdS4gvDWeYjh9zj5Dihd3it/view?usp=sharing) | |
| Tutorial 1: NN Basics | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Tutorials/NN_basics_Tut1.pdf), [video](https://drive.google.com/file/d/1s7uPfKM53_5PN30IbrK2chLIPqUvp4of/view?usp=sharing) | |
| Tutorial 2: NN Basics | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Tutorials/NN_basics_Tut2.pdf), [video1](https://drive.google.com/file/d/1HXjtGyx_dSlF_XSmxj3xlZBliNeLYmQm/view?usp=sharing), [video2](https://drive.google.com/file/d/1zq0jROhsIK51DQhCP4m3x0x2Uiqn8QJJ/view?usp=sharing) | [A note on Perceptron](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Extras/perceptron.pdf) |
| Tutorial 3: Optimisation Basics | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Tutorials/Opt_Tut1.pdf) |
| Lecture 1: DL Components and a Bayesian view | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture1.pdf), [video](https://drive.google.com/file/d/1lYs0VouCJ-e2BPlDPV8r2O6v-aGTJh1u/view?usp=sharing) |     |
| Lecture 2: Deep Feedforward Nets (MLPs) | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture2.pdf), [video](https://drive.google.com/file/d/10eJe8EjPyaNCYiLHmFFEjQPlT1D9JOby/view?usp=sharing) |     |
| Lecture 3: Backpropagation in MLP(1) | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture3.pdf), [video](https://drive.google.com/file/d/1-Eh_2lAW3m_WICtf4hOrZdiCU3f7KtOK/view?usp=sharing) | [Homework](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Extras/Lecture3_hw.pdf) |
| Lecture 4: Backpropagation in MLP(2) | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture4.pdf), [video](https://drive.google.com/file/d/1HCZ8ir6p_KqsMVePknsmWhFhwkDKPF4l/view?usp=sharing) | [Vectorisation](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Extras/vectorisation.pdf), [codes](https://github.com/tirtharajdash/CS-F425_Deep-Learning/tree/main/Demos/vectorisation) |
| Lecture 5: Generalisation(1) | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture5.pdf), [video](https://drive.google.com/file/d/1yR_s6YjoeFVe8SUQDjJDJmGyM1qnSwqt/view?usp=sharing) | [What is a dataset?](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Extras/YisSampled.pdf) |
| Lecture 6: Generalisation(2) | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture6.pdf), [video](https://drive.google.com/file/d/1VTaFv1TgZeriO9569Iffe-9huKCDFfSN/view?usp=sharing) | |
| Lecture 7: Dropout, Early Stopping | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture7.pdf), [video](https://drive.google.com/file/d/1RzVKVfSRbPThViZxFBpwQHdkXlTtFpTU/view?usp=sharing) | [Dropout Paper](https://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf) |
| Lecture 8: Optimisation and Parameter Initialisation | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture8.pdf), [video](https://drive.google.com/file/d/1xbwu334-iVoIGiy11YXXOyD-ndrfjwWU/view?usp=sharing) | |
| Lecture 9: Adaptive Optimisation Methods | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture9.pdf), [video](https://drive.google.com/file/d/1jAyfnim6WiHJM0kzsNnFS9S-Lxr1H72d/view?usp=sharing) | [Adam Paper](https://arxiv.org/pdf/1412.6980.pdf) |
| Lecture 10: Template Matching and CNNs | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture10.pdf), [video](https://drive.google.com/file/d/1odQ-rnu1pTJ_wmw-6Me2GYVmQCF7UxV_/view?usp=sharing) | [Yann LeCun's CNN Paper](http://yann.lecun.com/exdb/publis/pdf/lecun-99.pdf) |
| Lecture 11: Fully-Connected Layers to Convolutions | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture11.pdf), [video](https://drive.google.com/file/d/1rKlFf-TLDccHEXSxySr-_fDiJReq6HOd/view?usp=sharing) | |
| Lecture 12: CNN Operators (Convolution, Pooling) | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture12.pdf), [video](https://drive.google.com/file/d/1LzKvF1B8XiuFJ7C9kcgM8ZoAAqP5A6_4/view?usp=sharing) | |
| Lecture 13: Gradient Computation in CNNs | [Notes](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture13.pdf), [video](https://drive.google.com/file/d/1ZDRPzNG70scT6pOV5VTa-XMK_gIaLeUP/view?usp=sharing) | |
| Lecture 14: Modern Convolutional Neural Networks | [materials](https://d2l.ai/chapter_convolutional-modern/index.html), [video](https://drive.google.com/file/d/1xTd-igaWdmmdJ5YvSIp9VdOJblWkY2Nr/view?usp=drivesdk) | [AlexNet](https://colab.research.google.com/github/d2l-ai/d2l-pytorch-colab/blob/master/chapter_convolutional-modern/alexnet.ipynb), [VGG](https://colab.research.google.com/github/d2l-ai/d2l-pytorch-colab/blob/master/chapter_convolutional-modern/vgg.ipynb), [NiN](https://colab.research.google.com/github/d2l-ai/d2l-pytorch-colab/blob/master/chapter_convolutional-modern/nin.ipynb), [GoogLeNet](https://colab.research.google.com/github/d2l-ai/d2l-pytorch-colab/blob/master/chapter_convolutional-modern/googlenet.ipynb), [ResNet](https://colab.research.google.com/github/d2l-ai/d2l-pytorch-colab/blob/master/chapter_convolutional-modern/resnet.ipynb)
| Lecture 15: Transfer Learning | [video](https://drive.google.com/file/d/1NfjxSbLdMHGFBC9-din6DBLPB3Phn97K/view?usp=sharing)|[Notebook](https://colab.research.google.com/drive/1D-8H41zXHnsmjeaoOaqcZqIJH08aSbtY?usp=sharing)|
| Lecture 16: Sequence Learning | [materials:8.1-8.3](https://d2l.ai/chapter_recurrent-neural-networks/index.html), [video](https://drive.google.com/file/d/1jgUZhOKi4rV3kAfM47VhGHjPUZoaaoF_/view?usp=sharing) | [board](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture16.pdf) |
| Lecture 17: Recurrent Neural Nets | [video](https://drive.google.com/file/d/1gz4SMrueMBxg-ccP63qi9wN1pV9YBiIg/view?usp=sharing) | [board]() |
| Lecture 18: Backprop Through Time (BPTT) | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture17.pdf), [video](https://drive.google.com/file/d/1uettbMlL2Q9KoS0LmyO6dK4ubiQPtM_1/view?usp=sharing) | |
| Midsem solution discussion | [video](https://drive.google.com/file/d/14m0TA0YVqFAD5DyP5BqleFmoMIr18c47/view?usp=sharing) | |
| Lecture 19: Dealing with Vanishing Gradients in RNN | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture18.pdf), [video](https://drive.google.com/file/d/1Bht-fF8Od2YFBBYwAGzablnONg-p72G5/view?usp=sharing) | |
| Lecture 20: Seq-to-Seq Learning, Attention Mechanism | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture19.pdf), [video](https://drive.google.com/file/d/1rgtQA_7efylMz0ysqGQPk-MDQNusXyp6/view?usp=sharing) | |
| Lecture 21: Attention and Self-attention | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture20.pdf), [video](https://drive.google.com/file/d/1elHRINYDPe3lRH818wL0bPDaGJtdxXSO/view?usp=sharing) | [Attention is all you need.](https://arxiv.org/abs/1706.03762) |
| Lecture 22: Multi-head Attention and Transformer | [slides](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Lectures/Lecture21.pdf), [video](https://drive.google.com/file/d/1K--MH8oxbL4yj7OgjjlIMC-C8S1Wh08f/view?usp=sharing) | [Layer Normalisation](https://arxiv.org/abs/1607.06450) |

These slides and videos are not really optimised for general public; so, please email me directly if you find
any error or mistake in my lecture slides or videos. This will help me correct these the next time. I sincerely
thank the [MathCha Editor](https://www.mathcha.io/editor) which I use extensively to draw most of the diagrams.


## Lab Materials

All our labs will be based on PyTorch. See the official [PyTorch Tutorials](https://pytorch.org/tutorials/).
We will also have 1 lab on basic Python and PyTorch.

Update: According to students' votes, we are fixing the lab timing to be: **Wednesday 6-8 PM**. Please make sure to go through the reading materials (given below) before the lab.

To run/edit the colab notebooks, please create a copy in your drive and work on that copy.

| Lab   | Reading Material | Recording | Exercise Material |
|-------|------------------|-----------|-------------------|
| Lab 0: Basics of Python and PyTorch | [Python Tutorial Series](https://pythonprogramming.net/introduction-learn-python-3-tutorials/) by Sentdex <br> [Python Intro](https://cs231n.github.io/python-numpy-tutorial) by Justin Johnson <br>Section 2.1-2.3 of [d2l.ai](http://d2l.ai/) | [video](https://drive.google.com/file/d/1Be1aqGczs2d8pLkyvPESxyGjYSNonnZK/view?usp=sharing) |  [Notebook1](https://colab.research.google.com/drive/1HvAnGuGy6PaZyBtPNtYGUmvH-6CVDn5H?usp=sharing) <br> [Notebook2](https://colab.research.google.com/drive/1UQYTwZ6_y3ifZBfgIbn0INC87EmjPPtD?usp=sharing) |
| Lab 1: Autograd and MLP | Section 2.4 - 2.5 of [d2l.ai](http://d2l.ai/) <br> [Intro to Autograd](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html#sphx-glr-beginner-blitz-autograd-tutorial-py) | [video](https://drive.google.com/file/d/19YQLqth--2q7xdBER-632GW-kNmT9ayG/view?usp=sharing) | [Notebook](https://colab.research.google.com/drive/15L51sdwIeylKQV-BZm2wCEfR9dJT7-Zi?usp=sharing) |
| Lab 2: Regularisation | Section 4.5.2 - 4.5.3 of [d2l.ai](http://d2l.ai/) | [video](https://drive.google.com/file/d/1F8XRs73Tqsat2rtUyNye6ZY9s6EMpNOt/view?usp=sharing) | [Notebook](https://colab.research.google.com/drive/1X4kl7nGtj_q1rumvZHEsUeSzX1BJ9kJ6?usp=sharing) |
| Lab 3: Hyperparameter Tuning | Section 4.4, 4.6 and 7.5 from [d2l.ai](http://d2l.ai/) <br> [Hyperparameter tuning](https://www.oreilly.com/library/view/evaluating-machine-learning/9781492048756/ch04.html) | [video](https://drive.google.com/file/d/1fIfybjRUXG4btOvBM9E_90Cpx7YLlvjN/view?usp=sharing) | [Notebook 1](https://colab.research.google.com/drive/1S0Y8xiaBaI6p1Y74MiNnCio6IuOE4Eto?usp=sharing) <br> [Notebook 2](https://colab.research.google.com/drive/1UHsM00OTT19FexEHwSkrydo13pfvUKXO?usp=sharing) |
| Lab 4: Intro to CNNs | Section 6 from [d2l.ai](http://d2l.ai/) | [video](https://drive.google.com/file/d/1ScRQRsN3zt_Ye6mMD0uC1SHouQCkJyZJ/view?usp=sharing) |[Notebook](https://colab.research.google.com/drive/10afSD0wjQinhHug8RPlPSvooK8ZGfVgc?usp=sharing) |
| Lab 5: Intro to CNNs (Continued) | Section 6 from [d2l.ai](http://d2l.ai/) | [video](https://drive.google.com/file/d/1xNE06_1z7p1POk7BkG9QhJYMM_H1r9gd/view?usp=sharing) |[Notebook](https://colab.research.google.com/drive/10afSD0wjQinhHug8RPlPSvooK8ZGfVgc?usp=sharing) |
| Lab 6: Intro to RNNs | Section 8 from [d2l.ai](http://d2l.ai/) | [part 1](https://drive.google.com/file/d/1ckNOAf1_GfDcQzI-wwqfu6YLIJjttMN4/view?usp=sharing) [part 2]() |[Intro](https://colab.research.google.com/drive/1r4zC-g578oCFTzu8MNmRUQ6aKKrM56mZ?usp=sharing), [Exercises](https://colab.research.google.com/drive/1r4zC-g578oCFTzu8MNmRUQ6aKKrM56mZ?usp=sharing) |



## Lab Projects

| Lab Project | Details | Submission Date | Submission Link |
|-------------|---------|-----------------|-----------------|
| Project 1: Residual MLPs | [Assignment 1](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Projects/CS_F425_DL_Assignment_1.pdf) | **Sep 25, 11:59 PM IST** | [Google Classroom](https://classroom.google.com/c/MzgzNTE2MTc5NzE5/a/Mzk4ODI1MzU2MTAw/details) |



## Using our course materials

Non-profitable usage of the materials from this course is absolutely free. However,
if you are tech-blogger or a course instructor or a student outside BITS Pilani (Goa Campus) 
and you are using our course materials for any non-profitable purposes, 
please credit this course page by providing a proper reference to this page.
Any profitable usage of these materials needs permission from the owner ([Tirtharaj Dash](https://tirtharajdash.github.io/)).
Refer the license for more details.
