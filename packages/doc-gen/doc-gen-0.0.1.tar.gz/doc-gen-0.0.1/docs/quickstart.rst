.. _quickstart-label:

==========
Quickstart
==========

Doc-Gen is a simple tool to help you move your documentation
out of your code files. It is very simple to use.

Doc-Gen contains both a module and an executable; both of them are titled
``doc``.

.. note::

   There is no part of this module called ``doc-gen`` except for
   the module itself.

Here's a quick example of how to use Doc-Gen:

.. code:: python

   # source.py
   from doc import doc

   @doc
   def my_func(x, y):
        return 2*x + y

.. code:: text

   $ doc source.py
   Enter the docstring for my_func (Press Escape then Enter to submit):
   1| Write the documentation here. This prompt has *syntax highlighting*
   2| for reStructuredText
   3|
   4| .. note::
   5|    You can't see the syntax highlighting in this snippet. You actually
   6|    have to run the command above.
   7| 
   8| Once you've finished writing the docstring, press Escape then Enter to
   9| submit (or Meta-Enter).
   $

After you've run that, you can see the results of the docstring in the shell:

.. code:: python

   >>> import source
   >>> source.my_func.__doc__
   "Docstring here"

Documentation tools can read the docstring from that attribute.

.. note::

   Documentation tools like Sphinx only update the documentation if the source files
   change. Using this tool, the source files won't change; that's the whole point. To make
   tools update their documentation, you have to force them to rebuild the docs; with sphinx,
   you can use the ``E`` flag.

.. warning::

   All of the docstrings are stored in a file called ``docstrings.json``. If this file is deleted,
   there is no way to recover your docstrings (unless you undo the delete).
