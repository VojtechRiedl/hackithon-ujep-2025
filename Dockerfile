FROM python:3.13-slim-bookworm as requirements-stage
WORKDIR /tmp
RUN pip install uv
COPY ./pyproject.toml ./uv.lock* /tmp/
RUN uv lock
RUN uv export --no-hashes --no-header --no-annotate --no-dev --format requirements.txt > requirements-dev.txt

FROM python:3.13-slim-bookworm

ENV TZ=Europe/Prague
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /code
COPY --from=requirements-stage /tmp/requirements-dev.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENV PYTHONUNBUFFERED=1

COPY ./pyproject.toml /code/
COPY ./app /code/app

CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
