# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class DonnaHay(AbstractScraper):
    @classmethod
    def host(cls):
        return "donnahay.com.au"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        div = self.soup.find("div", class_="col-sm-6 method")
        if not div:
            return
        instructions = div.find_all("li")
        for instruction in instructions:
            [tag.extract() for tag in instruction.find_all("b") if "Serves" in tag.get_text()] # Removes any bold text with 'Serves' in it
            instruction.string = instruction.get_text(separator=" ", strip=True)  # Removes all &nbsp; characters
        return instructions

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
