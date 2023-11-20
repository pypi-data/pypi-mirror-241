===========
wonderparse
===========

Overview
--------

The wonderparse project allows for easy cooperation between a main-function/an object that hold the central functions on the one side and argparse on the other.

Installation
------------

To install wonderparse, you can use `pip`. Open your terminal and run:

.. code-block:: bash

    pip install wonderparse

Usage
-----

The code from the expit project

.. code-block:: python

    import math as _math

    import wonderparse as _wp


    def function(x:float):
        try:
            p = _math.exp(-x)
        except OverflowError:
            p = float('+inf')
        return 1 / (1 + p)

    def main(args=None):
        _wp.easymode.simple_run(
            args=args,
            program_object=function,
            prog='expit',
        )

Working example:

.. code-block:: python

    main([".4"])
    ### 0.598687660112452

Example with missing parameter.

.. code-block:: python

    main([])
    ### usage: expit [-h] x
    ### expit: error: the following arguments are required: x
    ### An exception has occurred, use %tb to see the full traceback.

Example with faulty typing.

.. code-block:: python

    main(["spam"])
    ### usage: expit [-h] x
    ### expit: error: argument x: invalid float value: 'spam'
    ### An exception has occurred, use %tb to see the full traceback.

The wonderparse project allows for parsing made easy.

License
-------

This project is licensed under the MIT License.

Links
-----

* `Download <https://pypi.org/project/wonderparse/#files>`_
* `Source <https://github.com/johannes-programming/wonderparse>`_

Credits
-------
- Author: Johannes
- Email: johannes-programming@posteo.org

Thank you for using wonderparse!
