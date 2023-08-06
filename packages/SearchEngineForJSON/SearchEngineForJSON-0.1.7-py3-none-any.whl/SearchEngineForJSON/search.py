

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
				addName = str(nameItem[0]) if isinstance(nameItem[0], int) else nameItem[0]
				nameReturns.append([name+"."+addName, nameItem[1]])
			return nameReturns

		if isinstance(documents, dict):
			typeItems = [[key, value] for key, value in documents.items() if type(value) is typeName]
			seekItems = [[key, value] for key, value in documents.items() if (isinstance(value, dict) or isinstance(value, list))]
		elif isinstance(documents, list):
			typeItems = [[key, value] for key, value in enumerate(documents) if type(value) is typeName]
			seekItems = [[key, value] for key, value in enumerate(documents) if (isinstance(value, dict) or isinstance(value, list))]
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

	@staticmethod
	def hello():
		print("hello world")