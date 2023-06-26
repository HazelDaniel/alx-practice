#getting base image
FROM ubuntu

RUN apt-get update

CMD ["printf", "created my first docker image\n"]
