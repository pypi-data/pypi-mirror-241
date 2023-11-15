# dataset.sh server

## Using Docker

`dataset.sh` server is available as a docker container `datasetsh/server`, by default it use the following
configuration:

* data storage folder: `/dataset-sh-storage/data`
* server config path: `/dataset-sh-storage/dataset-sh-server-config.json`

You can mount a local folder as a persistent storage for this container.

#### create an empty config file

```shell
docker run -v $(pwd):/dataset-sh-storage  datasetsh/server  dataset-sh-server-cli init
# -v $(pwd):/dataset-sh-storage                   -> mount current folder as storage folder
```

#### import

```shell
docker run -v $(pwd):/dataset-sh-storage -v /path/to/dataset/file:/tmp/upload.dataset datasetsh/server dataset.sh import username/dataset-name -f /tmp/upload.dataset
# -v $(pwd):/dataset-sh-storage                   -> mount current folder as storage folder
# -v /path/to/dataset/file:/tmp/upload.dataset    -> mount the file to import
# dataset.sh import username/dataset-name -f /tmp/upload.dataset
```

#### Start server

```shell
docker run -p 8989:8989 \ # map container:8989 to host:8989 -v $(pwd):/dataset-sh-storage datasetsh/server 
```

## Without Docker

You can also use it without docker.

```shell
pip install dataset_sh_server
```

#### Create an empty config file

```shell
dataset-sh-server-cli init
```

#### Start server

```shell
gunicorn -b 127.0.0.1:8989 "dataset_sh_server.app:create_app()"
# bind to 0.0.0.0 for external access
```

```shell
dataset.sh -b ./ import username/dataset_name -f /path/to/dataset/file 
```

### Management scripts

If you are using docker, you can use the following management script for you own convenience.

```shell
#!/bin/bash
set -e

must_exist() {
    local var_name="$1"
    local var_value="$2"

    if [ -z "$var_value" ]; then
        echo "Error: '$var_name' is not defined or empty"
        exit 1
    fi
    return
}

print_and_execute() {
  local cmd="$@"
  echo Executing CMD:
  echo $'\t' $cmd
  $cmd
}

start_server () {
  local port=${1:-8989}
  local storage_base_path=${2:-$(pwd)}
  must_exist storage_base_path $storage_base_path
  must_exist port $port
  local cmd="docker run -p ${port}:8989 -v ${storage_base_path}:/dataset-sh-storage datasetsh/server"
  print_and_execute $cmd
}

init_config () {
  local storage_base_path=${1:-$(pwd)}
  must_exist storage_base_path $storage_base_path
  local cmd="docker run -v ${storage_base_path}:/dataset-sh-storage  datasetsh/server  python -m dataset_sh_server.cli init"
  print_and_execute $cmd
}

import_dataset () {
  local dataset_name=$1
  local dataset_path=$2
  local storage_base_path=${3:-$(pwd)}

  must_exist dataset_name $dataset_name
  must_exist dataset_path $dataset_path
  must_exist storage_base_path $storage_base_path

  local cmd="docker run -v ${storage_base_path}:/dataset-sh-storage -v ${dataset_path}:/tmp/upload.dataset datasetsh/server dataset.sh import ${dataset_name} -f /tmp/upload.dataset"
  print_and_execute $cmd
}

"$@"
```

