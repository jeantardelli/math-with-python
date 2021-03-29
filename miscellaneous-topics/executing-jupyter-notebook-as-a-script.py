#!/bin/bash
"""
Jupyter notebooks are a popular medium for writing Python code for scientific
and data-based applications. A Jupyter notebook is really a sequence of blocks
that are stored in a file in JavaScript Object Notation (JSON) with the ipynb
extension. Each block can be one of several different types, such as code or
markdown. These notebooks are typically accessed through a web application that
interprets the blocks and executes the code in a background kernel that then
returns the results to the web application. This is great if you are working on
a personal PC, but what if you want to run the code contained within a notebook
remotely on a server? In this case, it might not even be possible to access the
web interface provided by the Jupyter notebook software. The papermill package
allows us to parameterize and execute notebooks from the command line.

This module illustrates how to execute a Jupyter notebook from the command line
using papermil.
"""
papermill --kernel python3 miscellaneous-topics/sample.ipynb miscellaneous-topics/output.ipynb
