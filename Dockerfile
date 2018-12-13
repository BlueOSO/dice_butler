FROM alpine:3.4
add . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python3.6", "dice_butler.py"]
