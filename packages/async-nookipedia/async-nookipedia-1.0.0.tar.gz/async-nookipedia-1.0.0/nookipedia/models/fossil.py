from pydantic import BaseModel


class Fossil(BaseModel):
    name: str
    image: str
    scientific_name: str
    sections: str
    period: str
    length: str
    price: str
    link: str
