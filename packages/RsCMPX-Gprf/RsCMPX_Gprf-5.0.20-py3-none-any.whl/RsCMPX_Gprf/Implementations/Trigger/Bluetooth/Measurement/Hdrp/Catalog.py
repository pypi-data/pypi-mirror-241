from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CatalogCls:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get_source(self) -> str:
		"""SCPI: TRIGger:BLUetooth:MEASurement<Instance>:HDRP:CATalog:SOURce \n
		Snippet: value: str = driver.trigger.bluetooth.measurement.hdrp.catalog.get_source() \n
		No command help available \n
			:return: trigger: No help available
		"""
		response = self._core.io.query_str('TRIGger:BLUetooth:MEASurement<Instance>:HDRP:CATalog:SOURce?')
		return trim_str_response(response)

	def set_source(self, trigger: str) -> None:
		"""SCPI: TRIGger:BLUetooth:MEASurement<Instance>:HDRP:CATalog:SOURce \n
		Snippet: driver.trigger.bluetooth.measurement.hdrp.catalog.set_source(trigger = 'abc') \n
		No command help available \n
			:param trigger: No help available
		"""
		param = Conversions.value_to_quoted_str(trigger)
		self._core.io.write(f'TRIGger:BLUetooth:MEASurement<Instance>:HDRP:CATalog:SOURce {param}')
