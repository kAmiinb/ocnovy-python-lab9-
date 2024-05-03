import json
from pydantic import BaseModel
from typing import List, Optional

class Pair(BaseModel):
    pair: str
    base_currency: str
    quote_currency: str
    volume: Optional[float]
    last_price: Optional[float]
    high: Optional[float]
    low: Optional[float]

class GetPairsResponse(BaseModel):
    pairs: List[Pair]

#зчитування json
with open('pairs.json', 'r') as file:
    json_data = json.load(file)
#вивід json
response = GetPairsResponse.parse_obj(json_data)

for pair in response.pairs:
    print(pair.pair, pair.last_price)
