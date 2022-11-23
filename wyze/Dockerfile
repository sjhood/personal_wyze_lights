FROM python:3.10-slim-buster

COPY . .

RUN pip3 install -r requirements.txt
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    make 

ENTRYPOINT ["sh"]
CMD ["entrypoint_script.sh"]