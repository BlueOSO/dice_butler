FROM alpine:3.4
add . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "dice_butler.py"]
