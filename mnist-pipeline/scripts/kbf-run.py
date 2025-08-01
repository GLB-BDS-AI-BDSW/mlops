from kfp.client import Client


with open("/var/run/secrets/kfp/token", "r") as f:
    token = f.read().strip()

client = Client(
    host="https://kns-job-1.jxe.10.132.0.56.nip.io/pipeline",
    verify_ssl=False,
    namespace="zakaria",
    existing_token=token
)

# yolo_experiment = client.create_experiment(name="YOLO Experiment")

run = client.create_run_from_pipeline_package(
    pipeline_file="pipelineMNIST.yaml",
    arguments={}
    )






