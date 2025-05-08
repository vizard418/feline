## feline (LLM on the command line: a client for intelligent conversations.)
---

### Install

- Clone the repository:
  `git clone https://github.com/vizard418/feline.git ~.local/share/`
- Get your API key on the Google Studio platform
  [aistudio](https://aistudio.google.com/app/apikey)
- Make your virtual enviroment with python on feline folder

  ```bash
  cd ~.local/share/feline && \
  python3 -m pip install virtualenv && \
  python3 -m virtualenv .venv
  ```
- Activate enviroment and install dependences:

  ```bash
  source .venv/bin/activate && \
  python -m pip install -r requirements.txt && \
  deactivate
  ```
---

- Edit the .bashrc file with the environment variables.
  `vim ~/.bashrc`
- Add lines:

```bash
# feline (LLM Command-Line)
export GEMINI_API_KEY="XXXXXXXXXXXXXX"
export FELINE_DIR="$HOME/.local/share/feline"
alias feline="$FELINE_DIR/wrapper.sh"
```

- Save and Refresh file:
`source ~/.bashrc`

---

### Run feline. Examples:

- Text comprehension:
`feline "How does AI work

- Switch model for complex tasks
`feline "Explains the relationship between climate change and human migration, highlighting both direct and indirect causes, and offers concrete examples from vulnerable regions." --deeper`

- Image recognition
`feline "How many animals do you see in the image?" --image [path/to/image1.png]`
