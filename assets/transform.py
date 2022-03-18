from assets.item_model import ItemDetails
import pandas as pd

def transform_data(data: ItemDetails):
    encoded_csv = pd.read_csv('datasets/encoded_train.csv')
    og_csv = pd.read_csv('datasets/train.csv')
    transformed_data = list()

    # item_identifier
    index_of_item_identifier = og_csv.index[og_csv['Item_Identifier'] == data['item_identifier']].tolist()[0]
    transformed_data.append(encoded_csv['Item_Identifier'][index_of_item_identifier])

    # item_weight
    transformed_data.append(data['item_weight'])

    # item_fat_content
    index_of_item_fat_content = og_csv.index[og_csv['Item_Fat_Content'] == data['item_fat_content']].tolist()[0]
    transformed_data.append(encoded_csv['Item_Fat_Content'][index_of_item_fat_content])

    # item_visibility
    transformed_data.append(data['item_visibility'])

    # item_type
    index_of_item_type = og_csv.index[og_csv['Item_Type'] == data['item_type']].tolist()[0]
    transformed_data.append(encoded_csv['Item_Type'][index_of_item_type])

    # item_mrp
    transformed_data.append(data['item_mrp'])

    # outlet_identifier
    index_of_outlet_identifier = og_csv.index[og_csv['Outlet_Identifier'] == data['outlet_identifier']].tolist()[0]
    transformed_data.append(encoded_csv['Outlet_Identifier'][index_of_outlet_identifier])

    # outlet_establishment_year
    transformed_data.append(data['outlet_establishment_year'])

    # outlet_size
    index_of_outlet_size = og_csv.index[og_csv['Outlet_Size'] == data['outlet_size']].tolist()[0]
    transformed_data.append(encoded_csv['Outlet_Size'][index_of_outlet_size])

    # outlet_location_type
    index_of_outlet_location_type = og_csv.index[og_csv['Outlet_Location_Type'] == data['outlet_location_type']].tolist()[0]
    transformed_data.append(encoded_csv['Outlet_Location_Type'][index_of_outlet_location_type])

    # outlet_type
    index_of_outlet_type = og_csv.index[og_csv['Outlet_Type'] == data['outlet_type']].tolist()[0]
    transformed_data.append(encoded_csv['Outlet_Type'][index_of_outlet_type]) 

    return [transformed_data]