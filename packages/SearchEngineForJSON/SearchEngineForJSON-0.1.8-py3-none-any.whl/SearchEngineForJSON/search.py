
""" SearchEngine for JSON
	
	Todo:
		* Practice
		* refactoring list and dict structure: done
		* Crating Errorhandling for ReclusionError
"""

class Search(object):
	""" SearchEngine for json

		Json形式のデータを検索するためのモジュール(小技)

		Attributes:
			None
	"""
	@classmethod
	def typeSearch(cls, documents, typeName, name=None):
		""" SearchEngine for json by mold
			
			json形式のデータを型を基にvalueで検索
			指定の型のデータを取得可能

			Args:
				documents(dict(json)): 探索したいjson形式のデータ
				typeName(型オブジェクト): 検索したい値の型を指定
				name(string): 呼び出し時不要, 指定必要なし

			returns:
				list: 値までの絶対パス(仮称)と値
		"""
		def nameUpdate(nameItems):
			nameReturns = []
			for nameItem in nameItems:
				if type(nameItem[0]) == str:
					if "->" in nameItem[0]:
						addName = nameItem[0].replace("->", "(>)")
					else:
						addName = nameItem[0]
				else:
					typeReName = type(nameItem[0]).__name__
					addName = typeReName + "({})".format(str(nameItem[0]))

				nameReturns.append([name+"->"+addName, nameItem[1]])
			return nameReturns

		if isinstance(documents, dict):
			typeItems = [[key, value] for key, value in documents.items() if type(value) is typeName]
			seekItems = [[key, value] for key, value in documents.items() if (isinstance(value, dict) or isinstance(value, list))]
		elif isinstance(documents, list):
			typeItems = [[list.__name__ + "({})".format(str(key)), value] for key, value in enumerate(documents) if type(value) is typeName]
			seekItems = [[list.__name__ + "({})".format(str(key)), value] for key, value in enumerate(documents) if (isinstance(value, dict) or isinstance(value, list))]
		else:
			pass

		typeAnswears = nameUpdate(typeItems) if name else typeItems
		seekAnswears = nameUpdate(seekItems) if name else seekItems

		if not seekAnswears:
			return typeAnswears
		else:
			for seekAnswear in seekAnswears:
				typeAnswears.extend(cls.typeSearch(documents=seekAnswear[1], typeName=typeName, name=seekAnswear[0]))
			return typeAnswears

	@classmethod
	def getAll(cls, documents, name=None):
		def nameUpdate(nameItems):
			nameReturns = []
			for nameItem in nameItems:
				if type(nameItem[0]) == str:
					if "->" in nameItem[0]:
						addName = nameItem[0].replace("->", "(>)")
					else:
						addName = nameItem[0]
				else:
					typeReName = type(nameItem[0]).__name__
					addName = typeReName + "({})".format(str(nameItem[0]))

				nameReturns.append([name+"->"+addName, nameItem[1]])
			return nameReturns

		if isinstance(documents, dict):
			branchItems = [[key, value] for key, value in documents.items() if (type(value) is not list) and (type(value) is not dict)]
			seekItems = [[key, value] for key, value in documents.items() if (isinstance(value, dict) or isinstance(value, list))]
		elif isinstance(documents, list):
			branchItems = [[list.__name__ + "({})".format(str(key)), value] for key, value in enumerate(documents) if (type(value) is not list) and (type(value) is not dict)]
			seekItems = [[list.__name__ + "({})".format(str(key)), value] for key, value in enumerate(documents) if (isinstance(value, dict) or isinstance(value, list))]
		else:
			pass

		branchAnswears = nameUpdate(branchItems) if name else branchItems
		seekAnswears = nameUpdate(seekItems) if name else seekItems

		if not seekAnswears:
			return branchAnswears
		else:
			for seekAnswear in seekAnswears:
				branchAnswears.extend(cls.getAll(documents=seekAnswear[1], name=seekAnswear[0]))
			return branchAnswears


	@classmethod
	def valueSearch(cls, documents, valueName, name=None):
		def nameUpdate(nameItems):
			nameReturns = []
			for nameItem in nameItems:
				if type(nameItem[0]) == str:
					if "->" in nameItem[0]:
						addName = nameItem[0].replace("->", "(>)")
					else:
						addName = nameItem[0]
				else:
					typeReName = type(nameItem[0]).__name__
					addName = typeReName + "({})".format(str(nameItem[0]))

				nameReturns.append([name+"->"+addName, nameItem[1]])
			return nameReturns

		if isinstance(documents, dict):
			valueItems = [[key, value] for key, value in documents.items() if value == valueName]
			seekItems = [[key, value] for key, value in documents.items() if (isinstance(value, dict) or isinstance(value, list))]
		elif isinstance(documents, list):
			valueItems = [[list.__name__ + "({})".format(str(key)), value] for key, value in enumerate(documents) if value == valueName]
			seekItems = [[list.__name__ + "({})".format(str(key)), value] for key, value in enumerate(documents) if (isinstance(value, dict) or isinstance(value, list))]
		else:
			pass

		valueAnswears = nameUpdate(valueItems) if name else valueItems
		seekAnswears = nameUpdate(seekItems) if name else seekItems

		if not seekAnswears:
			return valueAnswears
		else:
			for seekAnswear in seekAnswears:
				valueAnswears.extend(cls.valueSearch(documents=seekAnswear[1], valueName=valueName, name=seekAnswear[0]))
			return valueAnswears

	@classmethod
	def subStringSearch(cls, documents, subStringName, name=None):
		def nameUpdate(nameItems):
			nameReturns = []
			for nameItem in nameItems:
				if type(nameItem[0]) == str:
					if "->" in nameItem[0]:
						addName = nameItem[0].replace("->", "(>)")
					else:
						addName = nameItem[0]
				else:
					typeReName = type(nameItem[0]).__name__
					addName = typeReName + "({})".format(str(nameItem[0]))

				nameReturns.append([name+"->"+addName, nameItem[1]])
			return nameReturns

		if isinstance(documents, dict):
			valueItems = [[key, value] for key, value in documents.items() if type(value) == str if subStringName in value]
			seekItems = [[key, value] for key, value in documents.items() if (isinstance(value, dict) or isinstance(value, list))]
		elif isinstance(documents, list):
			valueItems = [[list.__name__ + "({})".format(str(key)), value] for key, value in enumerate(documents) if type(value) == str if subStringName in value]
			seekItems = [[list.__name__ + "({})".format(str(key)), value] for key, value in enumerate(documents) if (isinstance(value, dict) or isinstance(value, list))]
		else:
			pass

		valueAnswears = nameUpdate(valueItems) if name else valueItems
		seekAnswears = nameUpdate(seekItems) if name else seekItems

		if not seekAnswears:
			return valueAnswears
		else:
			for seekAnswear in seekAnswears:
				valueAnswears.extend(cls.subStringSearch(documents=seekAnswear[1], subStringName=subStringName, name=seekAnswear[0]))
			return valueAnswears

	@classmethod
	def startStringSearch(cls, documents, startStringName, name=None):
		def nameUpdate(nameItems):
			nameReturns = []
			for nameItem in nameItems:
				if type(nameItem[0]) == str:
					if "->" in nameItem[0]:
						addName = nameItem[0].replace("->", "(>)")
					else:
						addName = nameItem[0]
				else:
					typeReName = type(nameItem[0]).__name__
					addName = typeReName + "({})".format(str(nameItem[0]))

				nameReturns.append([name+"->"+addName, nameItem[1]])
			return nameReturns

		if isinstance(documents, dict):
			valueItems = [[key, value] for key, value in documents.items() if type(value) == str if value.startswith(startStringName)]
			seekItems = [[key, value] for key, value in documents.items() if (isinstance(value, dict) or isinstance(value, list))]
		elif isinstance(documents, list):
			valueItems = [[list.__name__ + "({})".format(str(key)), value] for key, value in enumerate(documents) if type(value) == str if value.startswith(startStringName)]
			seekItems = [[list.__name__ + "({})".format(str(key)), value] for key, value in enumerate(documents) if (isinstance(value, dict) or isinstance(value, list))]
		else:
			pass

		valueAnswears = nameUpdate(valueItems) if name else valueItems
		seekAnswears = nameUpdate(seekItems) if name else seekItems

		if not seekAnswears:
			return valueAnswears
		else:
			for seekAnswear in seekAnswears:
				valueAnswears.extend(cls.startStringSearch(documents=seekAnswear[1], startStringName=startStringName, name=seekAnswear[0]))
			return valueAnswears

	@classmethod
	def endStringSearch(cls, documents, endStringName, name=None):
		def nameUpdate(nameItems):
			nameReturns = []
			for nameItem in nameItems:
				if type(nameItem[0]) == str:
					if "->" in nameItem[0]:
						addName = nameItem[0].replace("->", "(>)")
					else:
						addName = nameItem[0]
				else:
					typeReName = type(nameItem[0]).__name__
					addName = typeReName + "({})".format(str(nameItem[0]))

				nameReturns.append([name+"->"+addName, nameItem[1]])
			return nameReturns

		if isinstance(documents, dict):
			valueItems = [[key, value] for key, value in documents.items() if type(value) == str if value.endswith(endStringName)]
			seekItems = [[key, value] for key, value in documents.items() if (isinstance(value, dict) or isinstance(value, list))]
		elif isinstance(documents, list):
			valueItems = [[list.__name__ + "({})".format(str(key)), value] for key, value in enumerate(documents) if type(value) == str if value.endswith(endStringName)]
			seekItems = [[list.__name__ + "({})".format(str(key)), value] for key, value in enumerate(documents) if (isinstance(value, dict) or isinstance(value, list))]
		else:
			pass

		valueAnswears = nameUpdate(valueItems) if name else valueItems
		seekAnswears = nameUpdate(seekItems) if name else seekItems

		if not seekAnswears:
			return valueAnswears
		else:
			for seekAnswear in seekAnswears:
				valueAnswears.extend(cls.endStringSearch(documents=seekAnswear[1], endStringName=endStringName, name=seekAnswear[0]))
			return valueAnswears


	@staticmethod
	def hello():
		print("hello")

	@staticmethod
	def world():
		print("world")


