from app.core.config import settings

TORTOISE_CONFIG = {
    "connections":{
        "default" : settings.DATABASE_URL
    },
    "apps" : {
        "models":{
            "models":[            
                "app.models.user",
                "app.models.room",
                "app.models.room_cost",
                "app.models.reservation",
                "aerich.models"
                ],
        "default_connection":"default"
        },
    },
    "use_tz":False,
    "timezone":"UTC"
}