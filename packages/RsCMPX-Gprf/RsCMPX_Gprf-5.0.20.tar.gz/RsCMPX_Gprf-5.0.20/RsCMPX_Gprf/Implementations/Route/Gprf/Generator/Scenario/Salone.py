from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SaloneCls:
	"""Salone commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("salone", core, parent)

	def set(self, tx_connector: enums.TxConnector, rf_converter: enums.TxConverter) -> None:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SCENario:SALone \n
		Snippet: driver.route.gprf.generator.scenario.salone.set(tx_connector = enums.TxConnector.I12O, rf_converter = enums.TxConverter.ITX1) \n
		No command help available \n
			:param tx_connector: No help available
			:param rf_converter: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('tx_connector', tx_connector, DataType.Enum, enums.TxConnector), ArgSingle('rf_converter', rf_converter, DataType.Enum, enums.TxConverter))
		self._core.io.write(f'ROUTe:GPRF:GENerator<Instance>:SCENario:SALone {param}'.rstrip())

	# noinspection PyTypeChecker
	class SaloneStruct(StructBase):
		"""Response structure. Fields: \n
			- Tx_Connector: enums.TxConnector: No parameter help available
			- Rf_Converter: enums.TxConverter: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tx_Connector: enums.TxConnector = None
			self.Rf_Converter: enums.TxConverter = None

	def get(self) -> SaloneStruct:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SCENario:SALone \n
		Snippet: value: SaloneStruct = driver.route.gprf.generator.scenario.salone.get() \n
		No command help available \n
			:return: structure: for return value, see the help for SaloneStruct structure arguments."""
		return self._core.io.query_struct(f'ROUTe:GPRF:GENerator<Instance>:SCENario:SALone?', self.__class__.SaloneStruct())
