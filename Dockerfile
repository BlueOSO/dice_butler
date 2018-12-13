FROM python:3-alpine
ADD requirements.txt /code
ADD dice_butler.py /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "code/dice_butler.py"]
