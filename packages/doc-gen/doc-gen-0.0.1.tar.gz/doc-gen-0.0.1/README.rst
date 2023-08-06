=======
Doc-Gen
=======

First, what Doc-Gen is not: it does not build documentation nor does it serve any
role in what you do after you write the documentation. In fact, it does what its
name says: it helps you write documentation.

When I code, I often find it hard to write docstrings; these bits of inline documentation
make navigating around the file a hassle. To move all docstrings out of file yet still
have them remain recognizable to other libraries, that is the purpose of this library.

-----------------------
How to use this library
-----------------------

This library has a shell script, ``doc``, and a decorator, ``doc``. Pretty easy to remember.
To use this library, you have to decorate the functions which you want with ``doc``, like so:

.. code:: python

   # source.py

   @doc
   def function(x, y):
        return 2 * x + y

Then, in the terminal, you should type ``doc source.py``, and you should see a prompt asking you
for a docstring for ``function``.

.. note::

   This library uses prompt_toolkit for many of its prompt-related actions. One thing to note is that
   when asking for a docstring, the prompt expects multiline input (in reST; it syntax highlights!), so
   to actually submit the docstring, you have to press Escape, then Enter.

After that, drop into the shell and check out the docstring of ``function``:

.. code:: python

   >>> import source
   >>> source.function.__doc__
   '<whatever you wrote>'

Sweet, isn't it?
