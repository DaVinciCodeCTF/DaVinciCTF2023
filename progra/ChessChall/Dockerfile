FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3 python3-pip socat
RUN useradd carlsen -m
RUN pip install --upgrade pip
RUN pip install stockfish
RUN pip install matplotlib

COPY . /ChessChall/
WORKDIR /ChessChall/
RUN chown -R carlsen:carlsen .
RUN chmod +x stockfish_15_linux_x64/stockfish_15_linux_x64/stockfish_15_x64

USER carlsen

CMD ["sh", "-c", "socat TCP-LISTEN:6464,reuseaddr,fork EXEC:'python3 ChessProj.py',stderr,pty,echo=0", ""]