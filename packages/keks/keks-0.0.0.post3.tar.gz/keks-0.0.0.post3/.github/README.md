[pip]: https://pip.pypa.io/en/stable/
[pypi]: https://pypi.org/project/keks
[python]: https://www.python.org/downloads/
[website]: https://schokokeks.pages.dev

[python-shield]: https://img.shields.io/badge/Python_3.11+-3776ab?style=for-the-badge&logo=python&logoColor=white


## Anforderungen

[![Python][python-shield]][python]

> [!IMPORTANT]  
> Stellen Sie sicher, dass Sie Python zum **PATH** hinzugefügt haben.

## Installation

Das Paket kann nun mit pip installiert werden! 
```shell
pip install -U keks
```

> [!NOTE]  
> Wenn Sie pip nicht mit Python installiert haben oder pip nicht erkannt wird,  
> führen Sie für pip zuvor noch `python -m ensurepip -U` aus.

## Verwendung

Danach können Sie keks im Terminal ausführen.
```shellOder nutzen Sie das Paket in Ihren eigenem Projekt
keks --help
```

Oder benutzen Sie das Paket in Ihrem eigenen Projekt.
```python [project.py]
import keks

print('Ich nutze keks', keks.__version__)
```