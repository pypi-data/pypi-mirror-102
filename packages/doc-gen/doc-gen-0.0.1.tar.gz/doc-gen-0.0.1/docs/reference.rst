.. module:: doc

=========
Reference
=========

This is the reference page of Doc-Gen

------------
External API
------------

.. autofunction:: doc.doc

.. autofunction:: doc.main

.. autofunction:: doc.poll

----------
UI Helpers
----------

.. autofunction:: doc.confirm

.. autoclass:: doc.ConfirmationLexer

.. autofunction:: doc.ask_docstring

.. autofunction:: doc.ask_confirmation

----------------
Status Modifiers
----------------

The function in this section all deal with external files. The
reason I need this is to convey information between seperate function
calls. There are to stateful files that are used: ``docstrings.json`` and
``doc_config``. ``docstrings.json`` contains a json file with docstrings
while ``doc_config`` contains a pickled representation of either ``True`` or
``False``

doc_config Modifiers
========================

.. autofunction:: doc.set_status

.. autofunction:: doc.get_status

.. autofunction:: doc.init_status

.. autofunction:: doc.del_status

docstring.json Modifiers
========================

.. autofunction:: doc.make_store

.. autofunction:: doc._get_store

.. autofunction:: doc.add_store

.. autofunction:: doc.get_store

----
Misc
----

.. autofunction:: doc.hash_fn
