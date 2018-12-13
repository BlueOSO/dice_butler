FROM python:3
add . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "dice_butler.py"]
