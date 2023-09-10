## Customization Steps

- DO NOT migrate yet
- add additional dependencies as needed
  - Re-export requirements.txt as needed
- Rename `project/.env.sample` to `.env` and update as needed
  - To generate secret key use `python3 -c "import secrets; print(secrets.token_urlsafe())"`
- Run makemigrations and migrate commands when ready.