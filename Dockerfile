FROM python:3.10

# Copy project
WORKDIR /app
COPY static/ static/
COPY Makefile Makefile
COPY pip.lock pip.lock
COPY server.py server.py

# Install dependencies from lock file
RUN make prod

# Expose server
EXPOSE 8080

ENTRYPOINT [ "make" ]
CMD [ "runprod" ]