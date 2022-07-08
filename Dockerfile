FROM legendxdxx/royalbot:latest

RUN git clone https://github.com/legendxdxx/OP-ROYALBOT.3.0.git /root/hellbot

WORKDIR /root/royalbot

RUN pip3 install -U -r requirements.txt

ENV PATH="/home/royalbot/bin:$PATH"

CMD ["python3", "-m", "royalbot"]
