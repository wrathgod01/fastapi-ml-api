from pydantic import BaseModel 

class ItemDetails(BaseModel):
    item_identifier: str
    item_weight: float
    item_fat_content: str
    item_visibility: float
    item_type: str
    item_mrp: float
    outlet_identifier: str
    outlet_establishment_year: int
    outlet_size: str
    outlet_location_type: str
    outlet_type: str

