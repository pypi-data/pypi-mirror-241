import re

from famegui.models import Contract


def get_product_name_from_contract(formatted_tree_view_contract_text: str):
    """Extract the product name from a formatted treeview contract item text"""

    pattern = r"\((.*?)\)"
    match = re.search(pattern, formatted_tree_view_contract_text)
    # Return the match if found, otherwise return None
    if match:
        return match.group(1)
    else:
        return None


def contract_fields_to_natural_types(contract_data_dict: dict, contract: Contract) -> dict:
    """Convert the contract fields to python types"""
    """ This is necessary to convert strings to ints"""
    for field_name, field_value in contract_data_dict.items():
        if contract.get_field_type(field_name) == Contract.FIELD_TYPE_INT:
            contract_data_dict[field_name] = int(field_value)
    return contract_data_dict


def get_id_from_item_desc(text: str):
    """Used to extract the id from a agent item description in the tree view"""
    pattern = r"#(\d+)"
    match = re.search(pattern, text)

    if match:
        result = match.group(1)
        return result
    else:
        return ""
