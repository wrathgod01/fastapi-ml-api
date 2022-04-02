from assets.item_model import ItemDetails
import pandas as pd

def transform_data(data: ItemDetails):
    json_data = pd.read_json('datasets/data.json')
    transformed_data = list()

    ## item_identifier
    index_of_item_identifier = ((json_data['train']['item_identifier']).strip('][').replace("'", "").split(', ')).index(data['item_identifier'])
    transformed_data.append(int((json_data['encoded_train']['item_identifier']).strip('][').replace("'", "").split(', ')[index_of_item_identifier]))

    # item_weight
    transformed_data.append(data['item_weight'])

    # # item_fat_content
    index_of_item_fat_content = ((json_data['train']['item_fat_content']).strip('][').replace("'", "").split(', ')).index(data['item_fat_content'])
    transformed_data.append(int((json_data['encoded_train']['item_fat_content']).strip('][').replace("'", "").split(', ')[index_of_item_fat_content]))

    # # item_visibility
    transformed_data.append(data['item_visibility'])

    # # item_type
    index_of_item_type = ((json_data['train']['item_type']).strip('][').replace("'", "").split(', ')).index(data['item_type'])
    transformed_data.append(int((json_data['encoded_train']['item_type']).strip('][').replace("'", "").split(', ')[index_of_item_type]))
    
    # # item_mrp
    transformed_data.append(data['item_mrp'])

    # # outlet_identifier
    index_of_outlet_identifier = ((json_data['train']['outlet_identifier']).strip('][').replace("'", "").split(', ')).index(data['outlet_identifier'])
    transformed_data.append(int((json_data['encoded_train']['outlet_identifier']).strip('][').replace("'", "").split(', ')[index_of_outlet_identifier]))
    
    # # outlet_establishment_year
    transformed_data.append(data['outlet_establishment_year'])

    # # outlet_size
    index_of_outlet_size = ((json_data['train']['outlet_size']).strip('][').replace("'", "").split(', ')).index(data['outlet_size'])
    transformed_data.append(int((json_data['encoded_train']['outlet_size']).strip('][').replace("'", "").split(', ')[index_of_outlet_size]))
    
    # # outlet_location_type
    index_of_outlet_location_type = ((json_data['train']['outlet_location_type']).strip('][').replace("'", "").split(', ')).index(data['outlet_location_type'])
    transformed_data.append(int((json_data['encoded_train']['outlet_location_type']).strip('][').replace("'", "").split(', ')[index_of_outlet_location_type]))
    
    # # outlet_type
    index_of_outlet_type = ((json_data['train']['outlet_type']).strip('][').replace("'", "").split(', ')).index(data['outlet_type'])
    transformed_data.append(int((json_data['encoded_train']['outlet_type']).strip('][').replace("'", "").split(', ')[index_of_outlet_type]))
    
    return [transformed_data]