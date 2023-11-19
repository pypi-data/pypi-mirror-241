# mon 
A customizable chat bot.

## Install
```bash
pip install -U mmon
```

Set environment variable in your `~/.bashrc`, `~/.zshrc`, etc.
```bash
export OPENAI_API_KEY=sk~XXXXXXXX
```
Or, to use Azure OpenAI endpoint, set following environment variable:
```bash
export OPENAI_API_KEY=XXXXXXXXXX
export OPENAI_API_BASE=https://XXXXXX.openai.azure.com/
export OPENAI_API_TYPE=azure
export OPENAI_API_VERSION=2023-07-01-preview
# Use a deploymetn of gpt-3.5-turbo or gpt-4 with version 0613 or later
export MON_DEPLOYMENT=gpt-35-turbo-16k
```

## Usage
```bash
python -m mon
# or
mon
```
