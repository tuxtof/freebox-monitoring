FROM grafana/grafana

ADD freebox-grafana.json /usr/share/grafana/dashboard/
RUN apt-get update && apt-get install -y curl && mkdir -p /data/grafana


ENV GF_DASHBOARDS_JSON_ENABLED true
ENV GF_DASHBOARDS_JSON_PATH dashboard/
ENV GF_USERS_ALLOW_SIGN_UP false
ENV GF_AUTH_ANONYMOUS_ENABLED true
ENV GF_PATHS_DATA /data/grafana

RUN /run.sh & sleep 60; curl 'http://admin:admin@127.0.0.1:3000/api/datasources' -X POST -H 'Content-Type: application/json;charset=UTF-8' --data-binary '{"name":"freebox","type":"influxdb","url":"http://influxdb:8086","access":"proxy","isDefault":true,"database":"freebox"}' ; pkill grafana-server
