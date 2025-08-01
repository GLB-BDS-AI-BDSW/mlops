FROM python:3.9

WORKDIR /app

COPY manifests/pipelineMNIST.yaml .
COPY scripts/kbf-run.py . 
RUN pip install kfp==2.3.0


CMD ["python","kbf-run.py"]


