import datetime
import math

from dateutil.parser import parse
from pandas import pandas as pd

from vocabs.models import SkosCollection, SkosConcept, SkosTechnicalCollection


def pop_char_field(temp_item, row, cur_attr, max_length=249, fd=None):
    """adds value to CharField on the current temp_item
    :param temp_item: a model class object
    :param row: A pandas DataFrame row with column names matching the items field names
    :param cur_attr: field name of the temp_item object
    :param max_length: The max_length of the current CharField of the object
    :return: The temp_item
    """
    lookup_val = fd.get(cur_attr, cur_attr)
    try:
        my_val = f"{str((row[lookup_val]))[:max_length]}"
    except TypeError:
        return temp_item
    setattr(temp_item, cur_attr, f"{my_val}")
    return temp_item


def pop_text_field(temp_item, row, cur_attr, fd=None):
    """ adds value to TextField on the current temp_item
        :param temp_item: a model class object
        :param row: A pandas DataFrame row with column names matching\
            the items field names
        :param cur_attr: field name of the temp_item object
        :return: The temp_item
    """
    try:
        lookup_val = fd.get(cur_attr, cur_attr)
        my_val = f"{(row[lookup_val])}"
        setattr(temp_item, cur_attr, my_val)
    except TypeError:
        pass
    return temp_item


def pop_int_field(temp_item, row, cur_attr, fd=None):
    """ adds value to TextField on the current temp_item
        :param temp_item: a model class object
        :param row: A pandas DataFrame row with column names matching\
            the items field names
        :param cur_attr: field name of the temp_item object
        :return: The temp_item
    """
    try:
        lookup_val = fd.get(cur_attr, cur_attr)
        my_val = int(row[lookup_val])
        setattr(temp_item, cur_attr, my_val)
    except ValueError:
        pass
    return temp_item


def pop_float_field(temp_item, row, cur_attr, fd=None):
    """ adds value to FloatField on the current temp_item
        :param temp_item: a model class object
        :param row: A pandas DataFrame row with column names matching\
            the items field names
        :param cur_attr: field name of the temp_item object
        :return: The temp_item
    """
    try:
        lookup_val = fd.get(cur_attr, cur_attr)
        my_val = float(row[lookup_val])

    except ValueError:
        return temp_item
    if math.isnan(my_val):
        return temp_item
    else:
        setattr(temp_item, cur_attr, my_val)
    return temp_item


def pop_fk_field(current_class, temp_item, row, cur_attr, fd=None, source_name=False):
    """ adds value to ForeignKey Field on the current temp_item
        :param current_class: a model class
        :param temp_item: a model class object
        :param row: A pandas DataFrame row with column names matching\
            the items field names
        :param cur_attr: field name of the temp_item object
        :param cur_field: the index number of the current collection
        :return: The temp_item
    """
    lookup_val = fd.get(cur_attr, cur_attr)
    rel_model_field = current_class._meta.get_field(cur_attr)
    rel_model = rel_model_field.related_model
    rel_model_npk_field = rel_model.get_natural_primary_key()

    if isinstance(row[lookup_val], str) and not row[lookup_val] == "x":
        my_val = row[lookup_val]
        get_create_dict = {rel_model_npk_field: my_val}
        rel_obj, _ = rel_model.objects.get_or_create(**get_create_dict)
        setattr(temp_item, cur_attr, rel_obj)
    else:
        return temp_item
    if isinstance(rel_obj, SkosConcept):
        tech_class_pref_label = f"{temp_item._meta.model_name}__{cur_attr}"
        tech_col, _ = SkosTechnicalCollection.objects.get_or_create(
            pref_label=tech_class_pref_label
        )
        rel_obj.tech_collection.add(tech_col)
    return temp_item


def pop_m2m_field(
    current_class, temp_item, row, cur_attr, sep="|", fd=None, source_name=None
):
    """ adds value to ManyToMany Field on the current temp_item
        :param current_class: a model class
        :param temp_item: a model class object
        :param row: A pandas DataFrame row with column names matching\
            the items field names
        :param cur_attr: field name of the temp_item object
        :param col_counter: the index number of the current collection
        :return: The temp_item
    """
    lookup_val = fd.get(cur_attr, cur_attr)
    fk = current_class._meta.get_field(cur_attr)
    rel_model_name = fk.related_model._meta.model_name
    if rel_model_name == "skosconcept":
        legacy_id = f"{source_name}__{row[lookup_val]}".strip().lower()
        return temp_item
    else:
        try:
            legacy_id = f"{float(row[lookup_val])}".strip().lower()
        except ValueError:
            legacy_id = f"{(row[lookup_val])}".strip().lower()
    if rel_model_name == "skosconcept":
        col, _ = SkosCollection.objects.get_or_create(
            name=f"{cur_attr}",
        )
        rel_things = []
        for x in row[lookup_val].split(sep):
            temp_rel_obj, _ = fk.related_model.objects.get_or_create(
                legacy_id=legacy_id,
            )
            temp_rel_obj.pref_label = f"{row[lookup_val]}".strip().lower()
            temp_rel_obj.collection.add(col)
            rel_things.append(temp_rel_obj)
        m2m_attr = getattr(temp_item, cur_attr)
        m2m_attr.set(rel_things)
    else:
        rel_things = []
        for x in row[lookup_val].split(sep):
            try:
                my_value = f"{float(x)}"
            except ValueError:
                my_value = f"{x}"[:249]
            temp_rel_obj, _ = fk.related_model.objects.get_or_create(
                legacy_id=my_value.strip().lower()
            )
            rel_things.append(temp_rel_obj)
        m2m_attr = getattr(temp_item, cur_attr)
        m2m_attr.set(rel_things)
    return temp_item


def pop_date_field(temp_item, row, cur_attr, fd=None):
    """ adds value to DateField on the current temp_item
        :param temp_item: a model class object
        :param row: A pandas DataFrame row with column names matching\
            the items field names
        :param cur_attr: field name of the temp_item object
        :return: The temp_itemplaces
    """
    lookup_val = fd.get(cur_attr, cur_attr)
    if isinstance(row[lookup_val], float):
        value = None
    if isinstance(row[lookup_val], int):
        value = parse(f"{row[lookup_val]}-01-01")
    elif isinstance(row[lookup_val], datetime.date):
        value = row[cur_attr]
    elif isinstance(row[lookup_val], str):
        try:
            value = parse(row[lookup_val])
        except Exception:
            # print(f"{row[lookup_val]} for field: {cur_attr} could not be\
            # parsed, due to Error: {e}")
            value = None
    elif pd.isnull(row[lookup_val]):
        value = None
    if value is not None:
        setattr(temp_item, cur_attr, value)
    return temp_item


def pop_date_range_field(temp_item, row, cur_attr, sep="|", fd=None):
    """ adds value to DateRangeField on the current temp_item
        :param temp_item: a model class object
        :param row: A pandas DataFrame row with column names matching\
            the items field names
        :param cur_attr: field name of the temp_item object
        :param sep: The separator used between start and end date
        :return: The temp_item
    """
    lookup_val = fd.get(cur_attr, cur_attr)
    if pd.isnull(row[lookup_val]):
        return temp_item
    elif isinstance(row[lookup_val], str) and sep in row[lookup_val]:
        if len(row[lookup_val].split(sep)) == 2:
            start_date, end_date = row[lookup_val].split("/")
            try:
                parse(start_date)
                valid_end = parse(end_date)
            except Exception as e:
                print(f"could not parse {start_date} or {end_date} due to: {e}")
                valid_end = None
            if valid_end is not None:
                setattr(temp_item, cur_attr, (start_date, end_date))
                return temp_item
        return temp_item
    else:
        return temp_item
