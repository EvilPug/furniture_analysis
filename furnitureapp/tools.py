import pandas as pd
import plotly.express as px

from furnitureapp.models import FurnitureModel


def plot_category(category_name: str) -> list:
    rows = FurnitureModel.objects.all()

    if len(rows) > 0:
        df = pd.DataFrame(list(rows.values()), columns=list(
            rows[0].__dict__.keys())[1:])

        df[df['category_name'] == category_name]
        charts = []
        fig = px.histogram(
            df,
            x='orig_price',
            color="status",
            title='Распределение цены без скидки для разных статусов мебели',
            labels={"orig_price": "Цена без скидки",
                    "status": "Статус"},
            category_orders={"status": ["в пути", "под заказ", "доступно"]}
        )

        fig.update_layout(title={
            'font_size': 22,
            'xanchor': 'center',
            'x': 0.5
        }, yaxis_title='Количество', legend_traceorder="reversed")

        charts.append(fig.to_html())

        top_10 = df.groupby('ven_code').mean().round().astype(int)[
                            'orig_price'].sort_values()[:10]

        fig = px.bar(
            top_10,
            title='ТОП-10 артикулов по средней цене без скидки',
            labels={"ven_code": "Артикул",
                    "value": "Средняя цена без скидки",
                    "variable": "Переменные"}
        )

        fig.update_layout(title={
            'font_size': 22,
            'xanchor': 'center',
            'x': 0.5
        })

        charts.append(fig.to_html())

        fig = px.pie(
            df,
            values=df.value_counts().values,
            names='status',
            title='Количество уникальных ID по статусам мебели',
            category_orders={"status": ["в пути", "под заказ", "доступно"]}
        )

        fig.update_layout(title={
            'font_size': 22,
            'xanchor': 'center',
            'x': 0.5
        }, legend_traceorder="reversed")

        charts.append(fig.to_html())

        return charts
