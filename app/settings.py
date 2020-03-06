import yaml, os

MONGO_HOST      = "mongo"
MONGO_PORT      =  27017
MONGO_DBNAME    = "jammer"

HATEOAS = False

# Eve schema is supposed to be read and written
# by humans too. YAML, period.
with open('app/eve_schema.yml') as f:
    DOMAIN = yaml.safe_load(f)

# While picking at the API running in dev box,
# the need to provide etag is just a nuisance.
if os.environ.get('devenv'):
    IF_MATCH = False
