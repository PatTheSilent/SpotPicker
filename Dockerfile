FROM python:3.9.0-slim-buster

WORKDIR /workdir

COPY setup.py README.md ./
COPY SpotPicker SpotPicker/
COPY scripts scripts/

RUN python setup.py sdist bdist_wheel

FROM python:3.9.0-slim-buster
WORKDIR /workdir/
COPY --from=0 /workdir/dist/* ./

RUN pip install SpotPicker-0.0.1*

CMD 'spot-picker'