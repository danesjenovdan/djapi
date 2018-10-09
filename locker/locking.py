from datetime import timedelta
from django.utils import timezone

def checkIfExpired(lock):
  if lock.opened:
    if (lock.activated_at + timedelta(seconds=20)) > timezone.localtime():
      return False
    else:
      lock.expired = True
      lock.save()

  return lock.expired