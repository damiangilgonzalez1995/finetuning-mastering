# finetuning-mastering


# finetuning-mastering


    -e COMET_PROJECT_NAME="finetuning" `
    -s COMET_API_KEY="1Ch9VlrNm0x2X3RQjAke1nshz" `
    -s HF_TOKEN="<HF_TOKEN>"
CLI INSTRUCTION
hf jobs uv run main.py `
    --flavor a10g-small `
    --timeout 3h `
    -e COMET_PROJECT_NAME="finetuning-sessions-lab2" `
    -s COMET_API_KEY="1Ch9VlrNm0x2X3RQjAke1nshz" `
    -s HF_TOKEN="<HF_TOKEN>"

hf jobs uv run --flavor a10g-small `
  -e COMET_PROJECT_NAME="finetuning-sessions-full-finetuning-no-thinking" `
  -s COMET_API_KEY="1Ch9VlrNm0x2X3RQjAke1nshz" `
  -s HF_TOKEN="<HF_TOKEN>" `
  --timeout 3h main.py -- `
  --hub_model_id Qwen3-0.6B-Full-Finetuning-No-Thinking `
  --dataset_column messages_no_thinking `
  --max_steps 200 # Remove this if you want to run it for one epoch (but it will take a long time)