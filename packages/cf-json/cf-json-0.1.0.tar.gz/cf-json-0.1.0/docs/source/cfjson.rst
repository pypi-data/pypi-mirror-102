cf-json
#######

.. py:currentmodule:: cfjson


**Expanded JSON serialization**


####

Summary
-------

``cf-json`` provides a batteries included approach to extending the standard :mod:`json` module.


It achieves this by making use of a custom :class:`json.JSONEncoder` subclass :class:`cfjson.MyEncoder` to
expand the range of types that can be serialized. While keeping sticking to the :mod:`json` interface.


Installation
------------

Install the package from `PyPI`_:

.. tabs::

    .. group-tab:: Linux

        .. code-block:: console

            $ python -m pip install cf-json
            [...]
            Successfully installed cf-json

    .. group-tab:: Windows

        .. code-block:: doscon

            C:\> py -m pip install cf-json
            [...]
            Successfully installed cf-json


Quick Start
-----------

`cf-json` is a drop in replacement for the standard :mod:`json` module.

.. code-block:: python

    >>> from cfjson import dumps, loads
    >>> data = {1: 'a', 2: Path('./my_file.py'), 3: datetime.datetime.utcnow()}
    >>> data
    {1: 'a', 2: WindowsPath('my_file.py'), 3: datetime.datetime(2021, 4, 7, 2, 45, 57, 696066)}
    >>> json_blob = dumps(data)
    >>> json_blob
    '{"1": "a", "2": {"__json_type__": "WindowsPath", "path": "my_file.py"}, "3": {"__json_type__": "datetime", "datetime": "2021-04-07T02:45:57.696066"}}'
    >>> loads(json_blob)
    {'1': 'a', '2': WindowsPath('my_file.py'), '3': datetime.datetime(2021, 4, 7, 2, 45, 57, 696066)}


Supported Types
---------------

.. automodule:: cfjson.serde
    :member-order: bysource

    .. automodule:: cfjson.serde.datetime_serde
        :member-order: bysource

    .. automodule:: cfjson.serde.decimal_serde
        :member-order: bysource

    .. automodule:: cfjson.serde.pathlib_serde
        :member-order: bysource


.. _encoderdecoder:

Custom Types
------------

It's straight forward to extend cf-json to support you own types.


Functional Approach
^^^^^^^^^^^^^^^^^^^

Use :meth:`cfjson.JsonTypeRegister.register` to register both your encoder and decoder against your type name.

.. code-block:: python

    import cfjson
    cfjson.JsonTypeRegister.register('MyClass', encoder_func, decoder_func)

Where the encoder function takes a single argument, an instance of your class and returns a `JSON` safe object, like a ``dict``
that will be output by the built-in ``json`` encoder.

.. code-block:: python

    def encoder_func(obj):
        """Encode the object into a json safe dict."""
        return {
            '__json_type__': 'MyClass',
            'my_class': obj.as_string()
        }

The `__json_type__` entry needs to match the type name your registered against. This is used by cfjson to lookup the correct
decoder during deserialization. The rest of the data in the output structure is up to you, just remember your decoder will
need to be able to parse it back into an object again.


.. code-block:: python

    def decoder_func(dct):
        """Decode json dict into class objects."""
        cls_name = dct['__json_type__']
        if cls_name == 'MyClass':
            return MyClass(dct['my_class'])
        raise TypeError()


The decoder also takes a single argument, a `dict` from the `JSON` file being parsed.

Your decoder first has to decide if if the `dict` contains any data you know how to deserialize. If not, raise and
exception an let one of the other decoders process it.

If it is your data, transform the data or instantiate your class, or what ever else you need to do and return the result.


Full Example
^^^^^^^^^^^^

.. literalinclude:: ../../src/cfjson/serde/datetime_serde.py
    :start-at: def datetime_decode(dct):


For more examples look at the source code of the scripts in the `cfjson.serde` module.



Object Approach
^^^^^^^^^^^^^^^

You can also choose implement your encoder and decoder as methods on your class.

If you use the `__json_encode__` method name there is no need to register it.

.. code-block:: python

    class MyClass(object):

        ...

        def __json_encode__(self):
            """Encode the object into a json safe dict."""
            return {
                '__json_type__': 'MyClass',
                'my_class': self.as_string()
            }


The decoder still needs to be registered.

.. code-block:: python

    class MyClass(object):

        ...

        @staticmethod
        def from_json(dct):
            """Decode json dict into class objects."""
            cls_name = dct['__json_type__']
            if cls_name == 'MyClass':
                return MyClass(dct['my_class'])
            raise TypeError()

    cfjson.JsonTypeRegister.register_decoder('MyClass', decoder_func)



Registration Class
------------------



.. automodule:: cfjson.coder
    :members:
    :member-order: bysource

.. py:currentmodule:: ""

JSON Interface
--------------

The json interface is unchanged with the exception of the `cls` parameter being reserved for internal usage.

.. automodule:: cfjson
    :members:
    :inherited-members:
    :member-order: bysource

.. _`PYPI`: https://pypi.org/project/cf-json/