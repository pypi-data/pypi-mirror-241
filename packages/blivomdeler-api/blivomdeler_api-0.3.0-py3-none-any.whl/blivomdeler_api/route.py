from .exceptions import InvalidResponseException
from requests import get


class RouteMap:
    def __init__(self, route_number: int, pdf_url: str) -> None:
        self.__route_number = route_number
        self.__pdf_url = pdf_url
        response = get(self.__pdf_url)
        if response.status_code != 200:
            raise InvalidResponseException("invalid response from api")
        self.__pdf_data = response.content

    @property
    def route_number(self) -> int:
        return self.__route_number

    @property
    def pdf_data(self) -> bytes:
        return self.__pdf_data

    @property
    def pdf_url(self) -> str:
        return self.__pdf_url
