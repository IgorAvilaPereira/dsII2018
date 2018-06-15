CREATE DATABASE blog;

CREATE TABLE public.noticia (
    id serial primary key,
    titulo text,
    texto text
);

INSERT INTO public.noticia VALUES (1, 'la casita de papelito', 'terceira temporada.como?');
INSERT INTO public.noticia VALUES (10, 'asdas', 'asdsads');
INSERT INTO public.noticia VALUES (11, 'grey anatomy', 'derek morre');
INSERT INTO public.noticia VALUES (12, 'ghost', 'eh um fantasma');
INSERT INTO public.noticia VALUES (13, 'lost', NULL);