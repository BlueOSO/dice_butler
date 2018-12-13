FROM python:3.6
add . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python3.6", "dice_butler.py"]
