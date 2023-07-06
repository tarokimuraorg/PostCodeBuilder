from dataclasses import dataclass

@dataclass(frozen=True)
class JPAddressPage:
    post_code : str = ''
    address : str = ''
    furigana : str = ''
