from .elf import Elf


class Druid(Elf):

    def __init__(
            self,
            musical_instrument: str,
            favourite_spell: str,
            nickname: str
    ) -> None:
        super().__init__(favourite_spell)
        self._favourite_spell = favourite_spell
        self.nickname = nickname
        self._musical_instrument = musical_instrument

    def player_info(self) -> str:
        return f"Druid {self.nickname}." \
               f" {self.nickname} has a favourite spell:" \
               f" {self._favourite_spell}"

    def get_rating(self) -> int:
        return len(self._favourite_spell)