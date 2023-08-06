
SimpleTAP
=========

``simpletap`` is a test runner that integrates with the unittest framework to
produce `TAP (Test Anything Protocol) <https://en.wikipedia.org/wiki/Test_Anything_Protocol>`__ compatible output.

.. image:: https://github.com/unode/simpletap/actions/workflows/main.yml/badge.svg
    :target: https://github.com/unode/simpletap/actions/

Usage
-----

In your test scripts, instead of:

.. code:: python

    if __name__ == "__main__":
        unittest.main()

use:

.. code:: python

    if __name__ == "__main__":
        from simpletap import TAPTestRunner
        unittest.main(testRunner=TAPTestRunner(buffer=True))


A small test case like:

.. code:: python

    import unittest

    class IntegerArithmeticTestCase(unittest.TestCase):
        def testAdd(self):  # test method names begin 'test*'
            "test adding values"
            self.assertEqual((1 + 2), 3)
            self.assertEqual(0 + 1, 1)

        def testMultiply(self):
            "test multiplying values"
            self.assertEqual((0 * 10), 0)
            self.assertEqual((5 * 8), 40)

        def testFail(self):
            "a failing test"
            self.assertEqual(0, 1)

        @unittest.expectedFailure
        def testExpectFail(self):
            "we saw this coming"
            self.assertEqual(0, 1)

        @unittest.expectedFailure
        def testUnexpectFail(self):
            "someone fixed it already"
            self.assertEqual(0, 0)

        @unittest.skipIf(True, "Skipping this one")
        def testSkip(self):
            "pending a fix"
            self.assertEqual(0, 1)

        def testError(self):
            "oops something went wrong"
            no_such_variable + 1  # Oops!

    if __name__ == "__main__":
        from simpletap import TAPTestRunner
        unittest.main(testRunner=TAPTestRunner(buffer=True))

When saved in a file called ``test.py`` and executed would produce:

.. code:: TAP

    1..7
    ok 1 - test.py: test adding values
    not ok 2 - test.py: oops something went wrong
    # ERROR: NameError on file test.py line 38 in testError: 'no_such_variable + 1  # Oops!':
    #        name 'no_such_variable' is not defined
    ok 3 - test.py: we saw this coming # TODO
    # EXPECTED_FAILURE: AssertionError on file test.py line 24 in testExpectFail: 'self.assertEqual(0, 1)':
    #                   0 != 1
    not ok 4 - test.py: a failing test
    # FAIL: AssertionError on file test.py line 19 in testFail: 'self.assertEqual(0, 1)':
    #       0 != 1
    ok 5 - test.py: test multiplying values
    ok 6 - test.py: pending a fix # skip
    # SKIP:
    #       Skipping this one
    not ok 7 - test.py: someone fixed it already # FIXED
    # UNEXPECTED_SUCCESS:
    #                     testUnexpectFail (__main__.IntegerArithmeticTestCase)

You can also launch ``simpletap`` directly from the command line in much the same way you do with unittest:

.. code::

    python -m simpletap test.IntegerArithmeticTestCase

Testing
-------

The test suite is configured to run via `tox <http://tox.readthedocs.io/>`__.


Projects
--------

``simpletap`` is currently being used by:

- `taskwarrior <https://github.com/taskwarrior/task/>`__
- `firefox_decrypt <https://github.com/unode/firefox_decrypt/>`__


Changelog
---------

2.0.0
^^^^^

- `skip` keyword is no longer used. Now fully compliant with `TAP <https://en.wikipedia.org/wiki/Test_Anything_Protocol>`__ using `ok`/`not ok`
- `SKIP` now results in `ok`
- `EXPECTED_FAILURE` now results in `ok`
- `UNEXPECTED_SUCCESS` is now explicitly handled and results in `not ok`
