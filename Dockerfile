FROM python:3.12
RUN pip install poetry
COPY . /src
WORKDIR /src
RUN poetry install
ENTRYPOINT ["poetry","run", "python", "polkaalert/main.py"]
