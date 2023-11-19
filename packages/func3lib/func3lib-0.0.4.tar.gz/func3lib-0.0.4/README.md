# Here is project DE2.1.5

	Module 2: Fundamentals of Data Engineering
	Sprint 1: Advanced Python & Linux Shell Commands
	Part 5: Data Transformation Library
	Version v0.1

## Project requirements

Objectives for this Part
 - Practice using Python and Numpy.
 - Practice building Python libraries.
 - Practice using Poetry.
 - Practice publishing your packages to PyPI.

Requirements
 - Implement the three data transformation functions described in the Context section.
 - Build a Python library containing the three functions.
 - Publish the library to PyPI.
 - Provide suggestions about how your analysis can be improved.

Evaluation Criteria
 - Adherence to the requirements. How well did you meet the requirements?
 - Code quality. Was your code well-structured? Did you use the appropriate levels of abstraction? Did you remove commented-out and unused code? Did you adhere to the PEP8?
 - Code performance. Did you use suitable algorithms and data structures to solve the problems?
 - Presentation quality. Coherence of the presentation of the project, and how well everything is explained.
 - General understanding of the topic.

# Build functions

## func3_lt package

	A package contains 3 functions:
		transpose2d
			"The function `transpose2d` takes a 2D matrix as input and returns its transpose."

		window1d
			" The function `window1d` takes an input array and creates overlapping windows of a specified size,
    		shift, and stride."

		convolution2d
			"The `convolution2d` function performs a 2D convolution operation on an input matrix using a given
    		kernel and stride."

## How to use
	After installing the package use following import:

		from func3_lt import transpose2d, window1d, convolution2d
