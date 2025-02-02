from flask import Blueprint, render_template

portfolio_menu_routes = Blueprint('portfolio_menu', __name__)


@portfolio_menu_routes.route("/portfolio/cakes")
def cakes():
    """Данная функция обрабатывает запрос URL, после рендеринга HTML-шаблона,
       возвращает пользователю страницу Архитектура, на основе HTML-шаблона"""
    return render_template("cakes.html")


@portfolio_menu_routes.route("/portfolio/cupcakes")
def cupcakes():
    """Данная функция обрабатывает запрос URL, после рендеринга HTML-шаблона,
       возвращает пользователю страницу Благоустройство, на основе HTML-шаблона"""
    return render_template("cupcakes.html")


@portfolio_menu_routes.route("/portfolio/donuts")
def donuts():
    """Данная функция обрабатывает запрос URL, после рендеринга HTML-шаблона,
       возвращает пользователю страницу Коммерческие интерьеры, на основе HTML-шаблона"""
    return render_template("donuts.html")


@portfolio_menu_routes.route("/portfolio/national_sweets")
def national_sweets():
    """Данная функция обрабатывает запрос URL, после рендеринга HTML-шаблона,
       возвращает пользователю страницу Коммерческие интерьеры, на основе HTML-шаблона"""
    return render_template("national_sweets.html")
