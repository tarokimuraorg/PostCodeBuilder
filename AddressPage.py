from dataclasses import dataclass

@dataclass(frozen=True)
class AddressPage:
    post_code : str = ''
    address : str = ''
    furigana : str = ''
