from __future__ import annotations

from ast import literal_eval
from configparser import ConfigParser
from itertools import islice
from pathlib import Path

import magic
import pdfplumber

from plagdef.model.models import Document


class DocumentFileRepository:
    def __init__(self, dir_path: Path, lang: str, recursive=False, at_least_two=True):
        self.lang = lang
        self._dir_path = dir_path
        self._recursive = recursive
        if not dir_path.is_dir():
            raise NotADirectoryError(f'The given path {dir_path} does not point to an existing directory!')
        if at_least_two and (not any(dir_path.iterdir()) or not next(islice(dir_path.iterdir(), 1, None), None)):
            raise NoDocumentFilePairFoundError(f'The directory {dir_path} must contain at least two documents.')

    def list(self) -> [Document]:
        if self._recursive:
            doc_files = [file_path for file_path in self._dir_path.rglob('*') if file_path.is_file()]
        else:
            doc_files = [file_path for file_path in self._dir_path.iterdir() if file_path.is_file()]
        documents = []
        for file in doc_files:
            if file.suffix == '.pdf':
                with pdfplumber.open(file) as pdf:
                    text = ' '.join(filter(None, (page.extract_text() for page in pdf.pages)))
            else:
                try:
                    detect_enc = magic.Magic(mime_encoding=True)
                    enc = detect_enc.from_buffer(open(str(file), 'rb').read())
                    text = file.read_text(encoding=enc)
                except (UnicodeDecodeError, LookupError):
                    raise UnsupportedFileFormatError(f'The file {file.name} has an unsupported encoding'
                                                     f' and cannot be read.')
            documents.append(Document(file.stem, str(text)))
        return documents


class DocumentPairReportFileRepository:
    def __init__(self, out_path: Path):
        if not out_path.is_dir():
            raise NotADirectoryError(f'The given path {out_path} does not point to an existing directory!')
        self._out_path = out_path

    def add(self, doc_pair_report):
        file_name = Path(f'{doc_pair_report.doc1.name}-{doc_pair_report.doc2.name}.{doc_pair_report.format}')
        file_path = self._out_path / file_name
        with file_path.open('w', encoding='utf-8') as f:
            f.write(doc_pair_report.content)


class ConfigFileRepository:
    def __init__(self, config_path: Path):
        if not config_path.is_file():
            raise FileNotFoundError(f'The given path {config_path} does not point to an existing file!')
        if not config_path.suffix == '.ini':
            raise UnsupportedFileFormatError(f'The config file format must be INI.')
        self.config_path = config_path

    def get(self) -> dict:
        parser = ConfigParser()
        parser.read(self.config_path)
        config = {}
        for section in parser.sections():
            typed_config = [(key, literal_eval(val)) for key, val in parser.items(section)]
            config.update(dict(typed_config))
        return config


class NoDocumentFilePairFoundError(Exception):
    pass


class UnsupportedFileFormatError(Exception):
    pass
