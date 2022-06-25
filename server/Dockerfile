FROM odoo:15.0
LABEL maintainer="Oakland  Tech <m.abdalla@odooerp.ae>"
ARG ACCESS_TOKEN
ENV ACCESS_TOKEN ${ACCESS_TOKEN}


USER root

COPY image-scripts/entrypoint.sh /
RUN chmod +x /entrypoint.sh
RUN mkdir -p /mount/data
#RUN chown  odoo:odoo -R /mount/data
RUN chmod  777  /mount/data
RUN apt-get update -y && apt-get  install git -y && git clone https://oaklanderp:"${connection_string}"@github.com/odoo/enterprise --depth 1 --branch 15.0 /mnt/addons_dependencies

#COPY server/addons_dependencies /mnt/addons_dependencies








RUN pip3 install redis

#COPY addons_ci /mnt/addons_ci
COPY image-configs/dev.conf /etc/odoo/odoo.conf
#RUN chmod 777 /etc/odoo/odoo.conf
#RUN chown odoo:odoo -R /etc/odoo/


COPY custom_addons /mnt/custom_addons
#COPY ./addons_extra /mnt/addons_extra
EXPOSE 8069 8071 8072

#USER odoo

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]
