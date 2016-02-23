FROM python:3
MAINTAINER Your Name <your@email.com> 

RUN pip install Flask && mkdir -p /tmp/hello
EXPOSE 80
CMD ["/hello.py"]
ENTRYPOINT ["python3"]
COPY hello.py /hello.py

