import time
import sched

from app.common.transaction_status import TransactionStatus
from app.utils.datetime_util import diff_time_in_minutes
from app.service import transaction_service

scheduler_interval_time = 10
scheduler = sched.scheduler(time.time, time.sleep)
expired_time_in_minute = 5


def update_expired_transaction():
    print("Cron job update expired transaction started at", int(time.time() * 1000))
    trans = transaction_service.get_all_not_completed_transaction()
    if trans is None or len(trans) == 0:
        return

    for tran in trans:
        if diff_time_in_minutes(tran.get("createdTime"), time.time() * 1000) >= expired_time_in_minute:
            print("=> Update status to EXPIRED of transaction ", tran.get("transactionId"))
            transaction_service.update_transaction_status(tran.get("transactionId"), TransactionStatus.EXPIRED.value)


def scheduled_task():
    update_expired_transaction()
    scheduler.enter(scheduler_interval_time, 1, scheduled_task)


scheduler.enter(0, 1, scheduled_task)


def start_scheduled_task():
    scheduler.run()
