"""
This file contains the logic required to set up htcondor jobs
for heron inference and training.
"""
import htcondor
import yaml


def create_sub_description(settings):
    """
    Create a condor submission description.
    """
    name = settings["name"]
    filepath = f"{settings['name']}.yml"
    with open(filepath, "w") as settings_file:
        yaml.dump(settings_file, settings)

    description = {
        "executable": "heron",
        "arguments": f"inference --settings {filepath}",
        "output": f"{name}.out",
        "error": f"{name}.err",
        "log": f"{name}.log",
        "batch_name": f"heron/{name}",
    }

    job = htcondor.Submit(description)
    return job


# def submit_description():
#     schedulers = htcondor.Collector().locate(
#         htcondor.DaemonTypes.Schedd, config.get("condor", "scheduler")
#     )

#     schedd = htcondor.Schedd(schedulers)
#     with schedd.transaction() as txn:
#         cluster_id = job.queue(txn)
#     return cluster_id
