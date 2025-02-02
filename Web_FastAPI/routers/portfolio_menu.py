from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

router = APIRouter()

env = Environment(loader=FileSystemLoader('templates'))


@router.get("/portfolio/cakes")
def read_cakes(request: Request):
    """Данная функция обрабатывает GET запрос поступающий на URL, получает HTML-шаблон, рендерит его
       с переданным контекстом, возвращает в виде HTML-ответа. Отображает страницу Архитектура."""
    template = env.get_template('cakes.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)


@router.get("/portfolio/cupcakes")
def read_cupcakes(request: Request):
    """Данная функция обрабатывает GET запрос поступающий на URL, получает HTML-шаблон, рендерит его
       с переданным контекстом, возвращает в виде HTML-ответа. Отображает страницу Благоустройство."""
    template = env.get_template('cupcakes.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)


@router.get("/portfolio/donuts")
def read_donuts(request: Request):
    """Данная функция обрабатывает GET запрос поступающий на URL, получает HTML-шаблон, рендерит его
       с переданным контекстом, возвращает в виде HTML-ответа. Отображает страницу Коммерческие интерьеры."""
    template = env.get_template('donuts.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)


@router.get("/portfolio/national_sweets")
def read_national_sweets(request: Request):
    """Данная функция обрабатывает GET запрос поступающий на URL, получает HTML-шаблон, рендерит его
       с переданным контекстом, возвращает в виде HTML-ответа. Отображает страницу Жилые интерьеры."""
    template = env.get_template('national_sweets.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)
