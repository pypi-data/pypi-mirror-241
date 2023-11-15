FROM python:3

RUN adduser --disabled-password --gecos '' runner

WORKDIR /usr/dataset_sh_server

RUN mkdir -p /dataset-sh-storage/data && chown -R runner:runner /dataset-sh-storage

RUN mkdir -p /tmp
RUN touch /tmp/upload.dataset && chown runner:runner /tmp/upload.dataset


RUN pip install dataset_sh_server==0.0.4
RUN pip install gunicorn

USER runner

WORKDIR /dataset-sh-storage

ENV DATASET_APP_STORAGE_LOCATION=/dataset-sh-storage/data
ENV DATASET_SH_SERVER_CONFIG_FILE=/dataset-sh-storage/dataset-sh-server-config.json

CMD ["gunicorn"  , "-b", "0.0.0.0:8989", "dataset_sh_server.app:create_app()"]
