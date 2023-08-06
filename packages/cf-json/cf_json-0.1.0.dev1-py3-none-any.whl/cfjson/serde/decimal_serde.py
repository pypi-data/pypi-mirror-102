"""
decimal
^^^^^^^

:class:`decimal.Decimal` is serialized as a string.

>>> import decimal
>>> data = decimal.Decimal('9.2')
>>> serialized = str(data)
>>> serialized
'9.2'
>>> data = decimal.Decimal(serialized)
Decimal('9.2')
"""

from ..coder import JsonTypeRegister


def decimal_decode(dct):
	"""Decode json dict into class objects."""
	from decimal import Decimal
	cls_name = dct['__json_type__']
	if cls_name == 'Decimal':
		return Decimal(dct['decimal'])
	raise TypeError()


def decimal_encode(obj):
	"""Encode the object into a json safe dict."""
	return {
		'__json_type__': 'Decimal',
		'decimal': str(obj)
	}


JsonTypeRegister.register('Decimal', decimal_encode, decimal_decode)
