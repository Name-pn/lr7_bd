import models
from flask import jsonify
from serialize import *

def where_filters(query, model: models.BaseModel, **filters):
    _filters = [
        getattr(model, key) == value
        for key, value in filters.items() if value is not None
    ]
    if _filters:
        return query.where(*_filters)
    return query

def execute_get_all(model, serializer, **filters):
    query = model.select()

    query = where_filters(query, model, **filters)
    print(query)
    return jsonify([serializer(model) for model in query])

def execute_get_one(pk, model, serializer):
    return serializer(model.select().where(model.id == int(pk)).get())

def get_block_detail(pk: int):
    return execute_get_one(pk, models.Block, serialize_block)

def get_blocks(**filters):
    return execute_get_all(models.Block, serialize_block, **filters)

def create_block(json: dict):
    return serialize_block(models.Block.create(**json))

def get_country_detail(pk: int):
    return execute_get_one(pk, models.Country, serialize_block)

def get_country(**filters):
    return execute_get_all(models.Country, serialize_block, **filters)

def create_country(json: dict):
    return serialize_block(models.Country.create(**json))

def get_conflict_detail(pk: int):
    return execute_get_one(pk, models.Conflict, serialize_block)

def get_conflict(**filters):
    return execute_get_all(models.Conflict, serialize_block, **filters)

def create_conflict(json: dict):
    return serialize_block(models.Conflict.create(**json))

def get_document_detail(pk: int):
    return execute_get_one(pk, models.BlockDocument, serialize_block)

def get_document(**filters):
    return execute_get_all(models.BlockDocument, serialize_block, **filters)

def create_document(json: dict):
    return serialize_block(models.BlockDocument.create(**json))

def get_climate_detail(pk: int):
    return execute_get_one(pk, models.Climate, serialize_block)

def get_climate(**filters):
    return execute_get_all(models.Climate, serialize_block, **filters)

def create_climate(json: dict):
    return serialize_block(models.Climate.create(**json))

def get_industry_detail(pk: int):
    return execute_get_one(pk, models.Climate, serialize_block)

def get_industry(**filters):
    return execute_get_all(models.Climate, serialize_block, **filters)

def create_industry(json: dict):
    return serialize_block(models.Climate.create(**json))

#def get_region_detail(pk: int):
#    return execute_get_one(pk, models.Region, serialize_block)

def get_region(**filters):
    return execute_get_all(models.Region, serialize_block, **filters)

def create_region(json: dict):
    return serialize_block(models.Region.create(**json))