import pandas as pd
from typing import Union
from pathlib import Path
import chardet


def detect_encoding(file_path: Path, num_bytes: int = 10000) -> str:
    """Detecta o encoding de um arquivo usando chardet."""
    with open(file_path, 'rb') as f:
        raw_data = f.read(num_bytes)
    result = chardet.detect(raw_data)
    return result['encoding'] or 'utf-8'  # fallback


def extract_data(file_path: Union[str, Path], sep: str = ';') -> pd.DataFrame:
    """
    Extrai dados de arquivos CSV, Excel ou JSON com auto-detecção de encoding.

    :param file_path: Caminho para o arquivo.
    :param sep: Separador para CSVs, padrão ';'.
    :return: DataFrame.
    """
    file_path = Path(file_path)

    try:
        if file_path.suffix == '.csv':
            detected_encoding = detect_encoding(file_path)
            print(f"🔍 Encoding detectado: {detected_encoding}")
            df = pd.read_csv(file_path, sep=sep, encoding=detected_encoding)

        elif file_path.suffix in ['.xls', '.xlsx']:
            df = pd.read_excel(file_path)

        elif file_path.suffix == '.json':
            df = pd.read_json(file_path)

        else:
            raise ValueError(f"Formato de arquivo {file_path.suffix} não suportado!")

        return df

    except UnicodeDecodeError as e:
        raise ValueError(f"Erro de codificação ao ler {file_path}. Detalhe: {e}")

    except Exception as e:
        raise ValueError(f"Erro ao extrair dados de {file_path}: {e}")
