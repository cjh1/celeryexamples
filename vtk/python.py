from celery import Celery
import sys

celery = Celery()
celery.config_from_object('celeryconfig')

@celery.task
def run():
    msg = "Running VTK Python"
    print >> sys.stderr, msg
    return msg
