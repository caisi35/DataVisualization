FROM python:3.5

RUN mkdir /covid_19_dv

WORKDIR /covid_19_dv

COPY requirements.txt /covid_19_dv/requirements.txt

ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive

RUN ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

COPY . /covid_19_dv

CMD ["uwsgi", "uwsgi.ini"]