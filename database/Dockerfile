FROM postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB todo
COPY todo.sql /docker-entrypoint-initdb.d/
EXPOSE 5432