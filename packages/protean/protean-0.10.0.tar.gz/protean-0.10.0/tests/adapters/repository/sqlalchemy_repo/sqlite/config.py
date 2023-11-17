# cSpell: disable

from protean.utils import Database, IdentityStrategy, IdentityType

####################
# CORE             #
####################

DEBUG = True
TESTING = True
ENV = "development"

# A secret key for this particular Protean installation. Used in secret-key
# hashing algorithms.
SECRET_KEY = "nU5JSWCP#4c#Annek2mx9V&g5uWUJfh@"

IDENTITY_STRATEGY = IdentityStrategy.UUID.value
IDENTITY_TYPE = IdentityType.STRING.value

# Define the databases
DATABASES = {
    "default": {
        "PROVIDER": "protean.adapters.repository.sqlalchemy.SAProvider",
        "DATABASE": Database.SQLITE.value,
        "DATABASE_URI": "sqlite:///test.db",
    },
    "memory": {"PROVIDER": "protean.adapters.MemoryProvider"},
}
