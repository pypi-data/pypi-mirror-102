# hive-udf

Hive UDF (user-defined functions) in Python.

Reference: [blog post](https://zpz.github.io/blog/hive-udf/).

This package provides a single function `make_udf` to work with Hive UDF
in Python. Please see source code for documentation.

Several example UDF modules are provided and can be used in tests.
Because real tests need a Hive setup, they are not included here.
User may test this package in their own Hive envivonrment, using
the few example UDFs.
The blog post offers some idea about testing as well.

This package is ready for production use.