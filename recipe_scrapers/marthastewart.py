# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class MarthaStewart(AbstractScraper):
    @classmethod
    def host(cls):
        return "marthastewart.com"
