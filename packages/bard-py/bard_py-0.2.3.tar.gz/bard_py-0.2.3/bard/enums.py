from enum import Enum


class ConversationStyle(Enum):
    """
    Bard conversation styles. Supported options are:
    - `creative` for original and imaginative chat
    - `balanced` for informative and friendly chat
    - `precise` for concise and straightforward chat
    """

    CASUAL = 2
    PROFESSIONAL = 5
