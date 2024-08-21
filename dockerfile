FROM python:3.10-alpine
# install bash
RUN apk update && apk add --no-cache bash curl

# Copy and install dependencies
RUN pip install poetry==1.8.3

# Configure Poetry to not create virtual environments
#RUN poetry config virtualenvs.create false

# Copy the pyproject.toml file and install dependencies
COPY pyproject.toml /pyproject.toml

# Install only dependancies
RUN poetry install --no-root

# Poetry wont install without it but also wont fail
COPY README.md /README.md

# Copy the code
COPY srai_telegrambot /srai_telegrambot

# install srai_telegrambot module
RUN poetry install

# copy the app
COPY app /app

# run the app
CMD ["poetry", "run", "python", "app/main.py"]
