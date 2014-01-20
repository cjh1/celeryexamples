from celery import Celery

celery = Celery()
celery.config_from_object('celeryconfig')

print celery.send_task('vtk.r.run', []).get()
print celery.send_task('vtk.python.run', []).get()

