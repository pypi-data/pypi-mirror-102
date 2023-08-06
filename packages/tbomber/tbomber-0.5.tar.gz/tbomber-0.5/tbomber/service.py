import random
import re
from abc import ABC, abstractmethod
from string import ascii_letters, digits
from typing import Optional

from httpx import AsyncClient, Response


class Service(ABC):
    @abstractmethod
    async def run(self, client, phone) -> Response:
        raise NotImplementedError()


def format_phone(phone: str, mask: str, mask_char: Optional[str] = "*") -> str:
    if not (match := re.match(r"\+?[78]?(\d{10})", phone)):
        raise ValueError(f"Invalid phone number {phone}")
    phone = match[1]
    if len(phone) != mask.count(mask_char):
        raise ValueError(f"Invalid mask {mask}")

    formatted = ""
    iter_phone = iter(phone)
    for char in mask:
        if char != mask_char:
            formatted += char
            continue
        formatted += next(iter_phone)
    return formatted


def rand_username() -> str:
    return str(random.sample(ascii_letters, 8) + random.sample(digits, 4))


def rand_password():
    return str(random.sample(ascii_letters + digits, 12))


def rand_russian_name():
    letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    return str(random.sample(letters, 7)).capitalize()


def rand_email():
    email = random.choice(["gmail.com", "mail.ru", "yandex.ru"])
    return f"{rand_username()}@{email}"
