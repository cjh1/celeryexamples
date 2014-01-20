BROKER_URL = "mongodb://localhost/celery"
CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": "localhost",
    "database": "celery"
}
CELERY_ROUTES = {'vtk.r.run': {'queue': 'r-queue'},
                 'vtk.python.run': {'queue': 'python-queue'}}
