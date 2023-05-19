FROM nginx:1.17.1-alpine

VOLUME ["/var/log/nginx", "/etc/nginx/conf.d"]

COPY ./nginx/config-default.conf /etc/nginx/nginx.conf

EXPOSE 80
EXPOSE 443