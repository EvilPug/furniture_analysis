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
            title=f'{category_name}: распределение цены',
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
            title=f'{category_name}: ТОП-10 артикулов по средней цене',
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
            title=f'{category_name}: количество уникальных ID по статусам',
            category_orders={"status": ["в пути", "под заказ", "доступно"]}
        )

        fig.update_layout(title={
            'font_size': 22,
            'xanchor': 'center',
            'x': 0.5
        }, legend_traceorder="reversed")

        fig.update_traces(hoverinfo='label+percent', textinfo='value+percent')

        charts.append(fig.to_html())

        return charts
