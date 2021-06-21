# RVGenerator

This random variate generation Python library has only two dependencies: `NumPy` and `Matplotlib`. If the user does not already have them installed, they may do so easily with the following commands:

`pip install numpy`

`pip install matplotlib`

Once the two dependencies are installed, users are ready to get started using the random variate generation library.

The random variate generation routines are written as methods within a class called `RVGenerator`, which located in a module called `RandomVariateGen.py`. To import the `RVGenerator` (along with all of the random variate generation routines) simply import it as follows:

`from RandomVariateGen import RVGenerator`

Once the `RVGenerator` class is imported into the user's script or Jupyter Notebook, they may begin using its methods to generate various random variates.

Since `RVGenerator` is a class, it must be instantiated. Creating an instance of `RVGenerator` takes just two arguments, the number of desired random variates to be creating and an optional random seed.

Please see `RVGenerator_walkthrough.ipynb` for a complete walk-through and examples of all of the methods in this library. 
