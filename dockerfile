FROM python:3.10-alpine
# copy and install dependencies
COPY requirements.txt /requirements.txt
RUN pip install --user -r /requirements.txt

# install srai_telegrambot module
COPY srai_telegrambot /srai_telegrambot
COPY setup.py /setup.py
COPY setup.cfg /setup.cfg
COPY README.md /README.md
RUN pip install --user -e .

# contains config
COPY app /app
WORKDIR /app
CMD python main.py