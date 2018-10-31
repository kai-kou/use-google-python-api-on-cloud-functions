# use-google-python-api-on-cloud-functions

Google Cloud Fucntionsでgoogle-api-python-clientを利用してfile_cache is unavailableエラーになったときの対応方法  

## Usage

```sh
# Get Source
> git clone https://github.com/kai-kou/use-google-python-api-on-cloud-functions.git
> cd use-google-python-api-on-cloud-functions

# Deploy Functions
> gcloud beta functions deploy check_discovery_error \
    --trigger-http \
    --runtime=python37

# Call Function
> gcloud beta functions call check_discovery_error

# Read Logs
> gcloud beta functions logs read check_discovery_error
```
