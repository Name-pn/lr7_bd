from models import *

def serialize_block(block: Block):
    return {
        'idBlock': block.idBlock,
        'army': block.army,
        'name': block.name,
        'dateFinal': block.dateFinal,
        'numberParticipants': block.numberParticipants,
    }

def serialize_document(model):
    return {
        'dateCreated': model.dateCreated,
        'nameDocument': model.nameDocument,
        'startingNum': model.startingNum,
        'numberParticipants': model.numberParticipants,
        'idBlock': {
            'idBlock': model.idBlock.idBlock,
            'army': model.idBlock.army,
            'name': model.idBlock.name,
            'dateFinal': model.idBlock.dateFinal,
            'numberParticipants': model.idBlock.numberParticipants,
        }
}

def serialize_conflict(model):
    return {
        'name': model.name,
        'numParticipants': model.numParticipants,
        'idConflict': model.idConflict,
    }


def serialize_country(model):
    return {
        'history', model.history,
        'name', model.name,
        'GDP', model.GDP,
        'idCountry', model.idCountry,
    }

def serialize_climate(model):
    return {
        'climateZone': model.climateZone,
        'idClimate': model.idClimate,
    }

def serialize_industry(model):
    return {
        'level': model.level,
        'idProm': model.idProm,
    }

def serialize_region(model):
    return {
        'square': model.square,
        'name': model.name,
        'idCountry': {
            'idCountry': model.idCountry.idCountry,
            'history': model.idCountry.history,
            'name': model.idCountry.name,
            'GDP': model.idCountry.GDP,
        },
        'idProm': {
            'level': model.idProm.level,
            'idProm': model.idProm.idProm,
        },
        'idClimate': {
            'climateZone': model.idClimate.climateZone,
            'idClimate': model.idClimate.idClimate,
        },
    }

def serialize_CCLinker(model):
    return {
        'idCountry': {
            'history', model.idCountry.history,
            'name', model.idCountry.name,
            'GDP', model.idCountry.GDP,
            'idCountry', model.idCountry.idCountry,
        },
        'idConflict': {
            'name': model.idConflict.name,
            'numParticipants': model.idConflict.numParticipants,
            'idConflict': model.idConflict.idConflict,
        },
    }

def serialize_BCLinker(model):
    return {
        'idCountry': {
            'history', model.idCountry.history,
            'name', model.idCountry.name,
            'GDP', model.idCountry.GDP,
            'idCountry', model.idCountry.idCountry,
        },
        'idBlock': {
            'idBlock': model.idBlock.idBlock,
            'army': model.idBlock.army,
            'name': model.idBlock.name,
            'dateFinal': model.idBlock.dateFinal,
            'numberParticipants': model.idBlock.numberParticipants,
        },
    }