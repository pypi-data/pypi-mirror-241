import wandb
from log_parameter import log
# import wandb.sdk.wandb_metric
# import wandb.apis.reports as wandb.apis.reports
from datetime import date, datetime
import time

def log_last_values(param, project_name, entity_name):
    api = wandb.Api()
    my_runs = api.runs(path=f"{entity_name}/{project_name}")
    # last_vals = []
    # for run in my_runs:
    #     history = run.scan_history(keys=[f"{param}"])
    #     run_vals = [row[f"{param}"] for row in history]
    #     if len(run_vals) != 0:
    #         last_vals.append(run_vals[-1])
    
    last_vals = []
    last_vals_date = []
    for run in my_runs:
        history = run.scan_history(keys=[f"{param}"])
        run_vals = [row[f"{param}"] for row in history]
        if len(run_vals) != 0:
            last_vals.append(run_vals[-1])
            last_vals_date.append(run.config["date"])

    last_vals.reverse()
    last_vals_date.reverse()

    curr_date = date.today()

    wandb.init(
        # Set the project where this run will be logged
        project=project_name, 
        # We pass a run name (otherwise it’ll be randomly assigned, like sunshine-lollypop-10)
        name=f"Last Value Log for {curr_date}", 
        # Track hyperparameters and run metadata
        config={
        "learning_rate": 0.02,
        "architecture": "CNN",
        "dataset": "CIFAR-100",
        "epochs": 10,
        "steps" : 1000,
        "date" : str(curr_date),
        })

    # wandb.run.define_metric("last-values", step_metric="date_metric")
    # for val in last_vals:
    #     wandb.log({"last-values": val, "date_metric":int(date.today())})

    for val in last_vals:
        wandb.log({"Last Values": val})

    # data = [[x, y] for (x, y) in zip(last_vals_date, last_vals)]
    # table = wandb.Table(data=data, columns = ["Date", "Last Values"])
    # wandb.log(
    # {"Last Value Graph" : wandb.plot.scatter(table, "Date", "Last Values",
    #        title=f"Last Value Graph for {param}")})

    wandb.finish()
    return last_vals

def generate_report(param, project_name, entity_name):

    api = wandb.Api()
    my_runs = api.runs(path=f"{entity_name}/{project_name}")
    run_vals = []
    for run in my_runs:
        history = run.scan_history(keys=[f"{param}"])
        run_vals.append([row[f"{param}"] for row in history])
    if len(run_vals) == 0:
        return -1
    
    curr_date = date.today()

    log_last_values(param, project_name, entity_name)

    report = wandb.apis.reports.Report(
        project=project_name,
        title=f'{curr_date}' + "\'s report",
        description="Here are the runs up to this date.",
        blocks=[
            wandb.apis.reports.H1(f"All runs for project {project_name} with parameter: {param}"),
            wandb.apis.reports.PanelGrid(
                panels=[
                    wandb.apis.reports.LinePlot(
                        title="Recent Graphs for:" + f"{param}",
                        y=f"{param}",
                        title_x="steps",
                        title_y=f"{param}",
                        ignore_outliers=True,
                        smoothing_factor=0.5,
                        smoothing_type="gaussian",
                        smoothing_show_original=True,
                        max_runs_to_show=10,
                        font_size="large",
                        legend_position="west",
                    ),
                    wandb.apis.reports.RunComparer(),
                    
                ],

                # runsets=[wandb.apis.reports.Runset(project=project_name, entity=entity_name)]
                runsets=[
                    wandb.apis.reports.Runset(project=project_name, entity=entity_name, query=f"{param}", name=f"Runs with {param}"),
                ],
            ),


            wandb.apis.reports.H1(f"Last values for project {project_name} with parameter: {param}"),
            wandb.apis.reports.PanelGrid(
                panels=[
                    wandb.apis.reports.LinePlot(
                        title="Last Value Graph:",
                        y="Last Values",
                        title_x="Date",
                        title_y="Last Values",
                        range_y=[0, 2],
                        ignore_outliers=True,
                        max_runs_to_show=1,
                        font_size="large",
                        legend_position="west",
                    ),
                    
                ],
                runsets=([[
                    wandb.apis.reports.Runset(project=project_name, entity=entity_name, name=f"Last Values of Runs"),
                ][-1]]),
            ),



            wandb.apis.reports.H1(f"All runs for project: {project_name}"),
            wandb.apis.reports.PanelGrid(
                panels=[
                    # wandb.apis.reports.LinePlot(
                    #     title="Recent Graphs for:" + f"{my_param}",
                    #     y=f"{my_param}",
                    #     title_x="steps",
                    #     title_y="{my_param}",
                    #     ignore_outliers=True,
                    #     smoothing_factor=0.5,
                    #     smoothing_type="gaussian",
                    #     smoothing_show_original=True,
                    #     max_runs_to_show=10,
                    #     plot_type="stacked-area",
                    #     font_size="large",
                    #     legend_position="west",
                    # )
                ],

                # runsets=[wandb.apis.reports.Runset(project=project_name, entity=entity_name)]
                runsets=[
                    wandb.apis.reports.Runset(project=project_name, entity=entity_name, name="Complete Run Set")
                ],
            )
        ]   
    ).save()                       
                    
    wandb.apis.reports.Report.from_url(report.url) 

    return 0