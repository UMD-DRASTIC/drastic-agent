"""
Contains a background task that will collect metrics about the
agent and make them available via the / route as a JSON object.
"""
__copyright__ = "Copyright (C) 2016 University of Maryland"
__license__ = "GNU AFFERO GENERAL PUBLIC LICENSE, Version 3"


from gevent import spawn, sleep

METRICS = {"storage": {}}


def metrics_processor(drivers):
    print "Spawning metrics process"
    spawn(metrics_background, drivers)


def metrics_background(drivers):
    while True:
        calculate_metrics(drivers)
        sleep(30)


def calculate_metrics(driver_list):
    from drivers import load
    global METRICS

    for driver_name in driver_list:
        driver = load(driver_name)
        METRICS["storage"][driver_name] = {}
        free = driver.free_space()
        used = driver.used_space()
        total = used + free
        if free == 0:
            percent = 100.0
        elif used == 0:
            percent = 0.0
        else:
            pct = (float(used) / float(total)) * 100.0
            percent = float("{0:.2f}".format(pct))

        METRICS["storage"][driver_name]["free"] = free
        METRICS["storage"][driver_name]["used"] = used
        METRICS["storage"][driver_name]["total"] = total
        METRICS["storage"][driver_name]["percent_used"] = percent

        count, size, max_size, min_size = driver.resource_info()
        METRICS["storage"][driver_name]["resource_count"] = count
        METRICS["storage"][driver_name]["avg_size"] = size
        METRICS["storage"][driver_name]["max_size"] = max_size
        METRICS["storage"][driver_name]["min_size"] = min_size
