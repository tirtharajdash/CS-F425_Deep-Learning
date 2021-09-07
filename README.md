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
|Lecture 5: Generalisation | | [What is a dataset?](https://github.com/tirtharajdash/CS-F425_Deep-Learning/blob/main/Extras/YisSampled.pdf) |


These slides and videos are not really optimised for general public; so, please email me directly if you find
any error or mistake in my lecture slides or videos. This will help me correct these the next time. 
Thank you.


## Lab Materials

All our labs will be based on PyTorch. See the official [PyTorch Tutorials](https://pytorch.org/tutorials/).
We will also have 1 lab on basic Python and PyTorch.

Update: According to students' votes, we are fixing the lab timing to be: **Wednesday 6-8 PM**. Please make sure to go through the reading materials (given below) before the lab.

To run/edit the colab notebooks, please create a copy in your drive and work on that copy.

| Lab   | Reading Material | Recording | Exercise Material |
|-------|------------------|-----------|-------------------|
| Lab 0: Basics of Python and PyTorch | [Python Tutorial Series](https://pythonprogramming.net/introduction-learn-python-3-tutorials/) by Sentdex <br> [Python Intro](https://cs231n.github.io/python-numpy-tutorial) by Justin Johnson <br>Section 2.1-2.3 of [d2l.ai](http://d2l.ai/) | [video](https://drive.google.com/file/d/1Be1aqGczs2d8pLkyvPESxyGjYSNonnZK/view?usp=sharing) |  [Notebook1](https://colab.research.google.com/drive/1HvAnGuGy6PaZyBtPNtYGUmvH-6CVDn5H?usp=sharing) <br> [Notebook2](https://colab.research.google.com/drive/1UQYTwZ6_y3ifZBfgIbn0INC87EmjPPtD?usp=sharing) |
| Lab 1 | | |


## Using our course materials

Non-profitable usage of the materials from this course is absolutely free. However,
if you are tech-blogger or a course instructor or a student outside BITS Pilani (Goa Campus) 
and you are using our course materials for any non-profitable purposes, 
please credit this course page by providing a proper reference to this page.
Any profitable usage of these materials needs permission from the owner ([Tirtharaj Dash](https://tirtharajdash.github.io/)).
Refer the license for more details.
