FROM python:3.10-slim

ENV PIP_ROOT_USER_ACTION=ignore

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    git clone --recursive --depth 1 https://github.com/StephenRicher/number_test && \
    cd number_test/ && python3 -m pip install . && \
    apt-get autoremove -y && apt-get clean

CMD ["/bin/bash"]
