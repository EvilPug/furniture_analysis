from django.shortcuts import render
from parserapp.scraputils import get_whole_category, convert_category_name

from furnitureapp.models import FurnitureModel
from furnitureapp.tools import plot_category


def index(request):
    rows = FurnitureModel.objects.all()
    loaded = set([row.category_name for row in rows])
    context = {'loaded': loaded}

    return render(request, 'index.html', context)


def scrap_furniture(request):

    if request.POST:

        rows = FurnitureModel.objects.all()
        loaded = set([row.category_name for row in rows])

        category = request.POST['category']
        category_name = convert_category_name(category)

        if len(category) == 7 and category_name not in loaded:

            furniture_list = get_whole_category(category)

            rows = FurnitureModel.objects.all()
            furniture_exist_list = [row.id for row in rows]
            for furniture in furniture_list:
                if furniture['id'] not in furniture_exist_list:
                    s = FurnitureModel(
                       id=furniture['id'],
                       ven_code=furniture['ven_code'],
                       category_name=furniture['category_name'],
                       name=furniture['name'],
                       furniture_color=furniture['furniture_color'],
                       furniture_type=furniture['furniture_type'],
                       furniture_sort=furniture['furniture_sort'],
                       status=furniture['status'],
                       orig_price=furniture['orig_price'],
                       disc_price=furniture['disc_price'])
                    s.save()

            charts = plot_category(category_name)
            message = f'Успешно загружена категория «{category_name}»'
            context = {'loaded': loaded, 'message': message, 'charts': charts}

            return render(request, 'index.html', context)
        else:

            charts = plot_category(category_name)
            message = f'Категория «{category_name}» уже есть в базе данных. \
                        Рисуем!'
            context = {'loaded': loaded, 'message': message, 'charts': charts}

            return render(request, 'index.html', context)
