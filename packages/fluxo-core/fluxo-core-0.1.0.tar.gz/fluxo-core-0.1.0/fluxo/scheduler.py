import asyncio
import schedule


def scheduler(coroutines):
    def exe_task(task):
        asyncio.run(task())

    for task, fluxo_info in coroutines:
        if fluxo_info.interval.get('minutes'):
            schedule.every(fluxo_info.interval.get('minutes')).minutes.at(
                fluxo_info.interval.get('at')).do(exe_task, task)
        elif fluxo_info.interval.get('hours'):
            schedule.every(fluxo_info.interval.get('hours')).hours.at(
                fluxo_info.interval.get('at')).do(exe_task, task)
        elif fluxo_info.interval.get('days'):
            schedule.every(fluxo_info.interval.get('days')).days.at(
                fluxo_info.interval.get('at')).do(exe_task, task)

    while True:
        schedule.run_pending()
