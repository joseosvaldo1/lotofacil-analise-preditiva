from pathlib import Path

from pandas import read_csv


ARQUIVO = Path(__file__).resolve().parents[1] / 'combinacoes' / 'combinacoes.csv'


def obter_possibilidades(arq=ARQUIVO):
	"""
	Cria uma lista com todas as combinações possíveis da lotofácil
		
	:param arq: Arquivo CSV com as combinações
	
	:return: Uma lista com todas as combinações 
	"""

	df = read_csv(arq, sep=';', encoding='utf-8')
	
	df.drop(columns=['seq'], inplace=True)
	possibilidades = df.values

	return possibilidades.tolist()
