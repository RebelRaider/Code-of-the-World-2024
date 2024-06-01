up:
	poetry run uvicorn app:app --reload --port 8000

.PHONY: migrate-rev
migrate-rev:
	poetry run alembic revision --autogenerate -m $(name)

.PHONY: migrate-up
migrate-up:
	poetry run alembic upgrade $(rev)

.PHONY: local
local:
	docker compose up postgres

.PHONY: test
test:
	poetry run pytest

.PHONY: download_models
	cd ml/models && wget https://huggingface.co/IlyaGusev/saiga_llama3_8b_gguf/resolve/main/model-q8_0.gguf