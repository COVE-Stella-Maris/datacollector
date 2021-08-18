-- Table: public.datascraper2

-- DROP TABLE public.datascraper2;

CREATE TABLE public.datascraper2
(
    datetime text COLLATE pg_catalog."default",
    heightmetric integer,
    heightimperial integer
)

TABLESPACE pg_default;

ALTER TABLE public.testerdb
    OWNER to "Emerson";
-- Index: data_timestamp_value_unique

-- DROP INDEX public.data_timestamp_value_unique;