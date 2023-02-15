FROM python:3.10-slim as base

WORKDIR /backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

FROM base AS python-deps


# install dependencies
RUN pip3 install --upgrade pipenv pip


COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --dev  --deploy --ignore-pipfile


#TODO build this from alpine and not slim like some kind of madman
FROM python:3.10-slim AS runtime
EXPOSE 8000
WORKDIR /backend
# Copy virtual env from python-deps stage
COPY --from=python-deps /backend/.venv /backend/.venv
ENV PATH="/.venv/bin:$PATH"
# install dependencies

# copy project
COPY . .
#the standard 127.0.0.1 listen address for the devserver would break with docker.

RUN chmod a+x docker/entrypoint.sh
RUN ./.venv/bin/python3 manage.py collectstatic --noinput

ENTRYPOINT ["docker/entrypoint.sh"]
CMD ./.venv/bin/gunicorn  -b 0.0.0.0:8000 roll-call.wsgi