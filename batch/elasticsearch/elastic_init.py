from elasticsearch import Elasticsearch
from os import getenv

es = Elasticsearch(["http://{}:{}".format(getenv("ELASTICSEARCH_HOST"),getenv("ELASTICSEARCH_PORT"))])

metrics_jems_json = {
    "mappings": {
        "properties": {
            "dateHour": {
                "type": "date"
            },
            "gpsSpeed": {
                "type": "float"
            },
            "gpsSatCount": {
                "type": "float"
            },
            "Gear": {
                "type": "float"
            },
            "Brake_pedal": {
                "type": "float"
            },
            "Accel_pedal": {
                "type": "float"
            },
            "Machine_Speed_Mesured": {
                "type": "float"
            },
            "AST_Direction": {
                "type": "float"
            },
            "Ast_HPMB1_Pressure_bar": {
                "type": "float"
            },
            "Ast_HPMA_Pressure_bar": {
                "type": "float"
            },
            "Pressure_HighPressureReturn": {
                "type": "float"
            },
            "Pressure_HighPressure": {
                "type": "float"
            },
            "Oil_Temperature": {
                "type": "float"
            },
            "Ast_FrontAxleSpeed_Rpm": {
                "type": "float"
            },
            "Pump_Speed": {
                "type": "float"
            }
        }  
    }
}

res = es.indices.create(index=getenv("ELASTICSEARCH_INDEX"), body=metrics_jems_json)