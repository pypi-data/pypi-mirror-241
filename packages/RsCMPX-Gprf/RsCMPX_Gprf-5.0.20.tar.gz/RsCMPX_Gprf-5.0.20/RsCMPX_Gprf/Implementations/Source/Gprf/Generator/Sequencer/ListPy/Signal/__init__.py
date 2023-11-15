from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.Utilities import trim_str_response
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SignalCls:
	"""Signal commands group definition. 7 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signal", core, parent)

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Range import RangeCls
			self._range = RangeCls(self._core, self._cmd_group)
		return self._range

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	@property
	def index(self):
		"""index commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_index'):
			from .Index import IndexCls
			self._index = IndexCls(self._core, self._cmd_group)
		return self._index

	def set(self, index: int, signal: str) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.signal.set(index = 1, signal = 'abc') \n
		Defines or queries the signal type for the sequencer list entry with the selected <Index>. A complete list of all
		supported strings can be queried using method RsCMPX_Gprf.Source.Gprf.Generator.Sequencer.ListPy.Signal.Catalog.value. \n
			:param index: No help available
			:param signal: Signal type
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('signal', signal, DataType.String))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal {param}'.rstrip())

	def get(self, index: int) -> str:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal \n
		Snippet: value: str = driver.source.gprf.generator.sequencer.listPy.signal.get(index = 1) \n
		Defines or queries the signal type for the sequencer list entry with the selected <Index>. A complete list of all
		supported strings can be queried using method RsCMPX_Gprf.Source.Gprf.Generator.Sequencer.ListPy.Signal.Catalog.value. \n
			:param index: No help available
			:return: signal: Signal type"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal? {param}')
		return trim_str_response(response)

	def get_all(self) -> List[str]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL \n
		Snippet: value: List[str] = driver.source.gprf.generator.sequencer.listPy.signal.get_all() \n
		Defines the signal types for all sequencer list entries. A complete list of all supported strings can be queried using
		method RsCMPX_Gprf.Source.Gprf.Generator.Sequencer.ListPy.Signal.Catalog.value. \n
			:return: signal: Comma-separated list of strings, one string per list entry
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL?')
		return Conversions.str_to_str_list(response)

	def set_all(self, signal: List[str]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.signal.set_all(signal = ['abc1', 'abc2', 'abc3']) \n
		Defines the signal types for all sequencer list entries. A complete list of all supported strings can be queried using
		method RsCMPX_Gprf.Source.Gprf.Generator.Sequencer.ListPy.Signal.Catalog.value. \n
			:param signal: Comma-separated list of strings, one string per list entry
		"""
		param = Conversions.list_to_csv_quoted_str(signal)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:SIGNal:ALL {param}')

	def clone(self) -> 'SignalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SignalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
