-- Table: public.testerdb

-- DROP TABLE public.testerdb;

CREATE TABLE public.testerdb
(
    datetime text COLLATE pg_catalog."default",
    avgwinddir text COLLATE pg_catalog."default",
    avgwindspd text COLLATE pg_catalog."default",
    windobs text COLLATE pg_catalog."default",
    avgseas text COLLATE pg_catalog."default",
    waveobs text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE public.testerdb
    OWNER to "Emerson";
-- Index: data_timestamp_value_unique

-- DROP INDEX public.data_timestamp_value_unique;

CREATE UNIQUE INDEX data_timestamp_value_unique
    ON public.testerdb USING btree
    (datetime COLLATE pg_catalog."default" ASC NULLS LAST, datetime COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;