# nummethod-tester

This is a single-class Python library that helps testing numerical methods (e.g. methods for solving systems of linear algebraic equations or methods of obtaining eigenvalues). Since all testing workflow is similar for different numerical methods (preparing tests, running algorithm on number of tests, checking quality and speed), the library was prepared to provide a general skeleton for these tasks. User needs to specify only the code of the method and tests input/output procedures (not fully).
Library supports auto-generation of tests, reporting results; another functionality such as plotting can be added.

### How to use

User should fill in the gaps in several functions in files:
* **mytester.py**
* **calculate.py**
* **main.py** (not necessarily)

Files are provided with comments on the meaning of the functions.

**calculate (SLAE).py** is provided as a more specific version of **calculate.py** written for SLAE solving methods.

You can either execute **main.py** or import MyTester class from **mytester.py** to run the testing process.
