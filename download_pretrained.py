from huggingface_hub import snapshot_download

snapshot_download(repo_id="google-t5/t5-large", local_dir="./pretrained_models/t5-large")
snapshot_download(repo_id="distilbert/distilbert-base-cased", local_dir="./pretrained_models/distilbert-base-cased")
