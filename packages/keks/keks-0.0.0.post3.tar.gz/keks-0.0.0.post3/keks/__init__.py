"""
"""
from typing import NamedTuple, Literal


class VersionInfo(NamedTuple):
    major: int = 0
    minor: int = 0
    micro: int = 0
    releaselevel: Literal['alpha', 'beta', 'candidate', 'final'] = 'final'
    serial: int = 0
    post: int = 0
    dev: int = 0

    def to_string(self):
        dev = self.dev
        post = self.post
        level = self.releaselevel

        base = f'{self.major}.{self.minor}.{self.micro}'
        suffix = ''

        if post:
            suffix = f'.post{post}'

        if dev:
            suffix = f'{suffix}.dev{dev}'

        if level == 'final':
            return f'{base}{suffix}'

        if level == 'candidate':
            label = 'rc'
        else:
            label = level[0]

        return f'{base}{label}{self.serial}{suffix}'


version_info = VersionInfo(post=3)


__title__ = 'keks'
__author__ = 'katzensindniedlich'
__version__ = version_info.to_string()
__license__ = 'MIT'
__copyright__ = 'Copyright 2023-present katzensindniedlich'



del NamedTuple, Literal, VersionInfo