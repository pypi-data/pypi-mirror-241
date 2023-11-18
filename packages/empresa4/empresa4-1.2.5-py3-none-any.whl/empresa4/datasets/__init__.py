import pkg_resources
import pandas as pd

nombres_datasets = [
    "01_original",
    "01_producto_estrella",
    "01_productos_todos",
    "01_por_cliente",
    "01_120",
    "02_original",
    "02_producto_estrella",
    "02_productos_todos",
    "02_por_cliente",
    "02_precios_cuidados",
    "02_120",
    "maestro_productos",
    "02_productos_todos_anti_leak",
    "02_120_anti_leak",
    "02_stocks_productos_todos",
    "02_stocks_anti_leak",
    "02_productos_todos_anti_leak_con_FE_04",
    "02_productos_todos_anti_leak_con_FE_06"
]


def get_nombres_datasets():
    return nombres_datasets


def get_dataset(dataset_name):
    if dataset_name not in nombres_datasets:
        raise ValueError(
            f"Dataset not found. Usar uno de los siguientes: {nombres_datasets}"
        )

    df = None

    if dataset_name == "01_producto_estrella":
        filepath = pkg_resources.resource_filename(
            "empresa4", "datasets/tb_sellout_01_producto_estrella.csv"
        )

    elif dataset_name == "01_productos_todos":
        filepath = pkg_resources.resource_filename(
            "empresa4", "datasets/tb_sellout_01_productos_todos.csv"
        )

    elif dataset_name == "01_original":
        filepath = pkg_resources.resource_filename(
            "empresa4", "datasets/tb_sellout_01_original.csv"
        )

    elif dataset_name == "01_120":
        filepath = pkg_resources.resource_filename(
            "empresa4", "datasets/tb_sellout_01_120.csv"
        )

    elif dataset_name == "02_producto_estrella":
        filepath = pkg_resources.resource_filename(
            "empresa4", "datasets/tb_sellout_02_producto_estrella.csv"
        )

    elif dataset_name == "02_productos_todos":
        filepath = pkg_resources.resource_filename(
            "empresa4", "datasets/tb_sellout_02_productos_todos.csv"
        )

    elif dataset_name == "02_original":
        filepath = pkg_resources.resource_filename(
            "empresa4", "datasets/tb_sellout_02_original.csv"
        )

    elif dataset_name == "02_precios_cuidados":
        filepath = pkg_resources.resource_filename(
            "empresa4", "datasets/tb_sellout_02_precios_cuidados.csv"
        )

    elif dataset_name == "02_120":
        filepath = pkg_resources.resource_filename(
            "empresa4", "datasets/tb_sellout_02_120.csv"
        )

    elif dataset_name == "maestro_productos":
        filepath = pkg_resources.resource_filename(
            "empresa4", "datasets/maestro_productos.csv"
        )

    elif dataset_name == "02_productos_todos_anti_leak":
        filepath = pkg_resources.resource_filename(
            "empresa4", "datasets/tb_sellout_02_productos_todos_anti_leak.csv"
        )

    elif dataset_name == "02_120_anti_leak":
        filepath = pkg_resources.resource_filename(
            "empresa4", "datasets/tb_sellout_02_120_anti_leak.csv"
        )

    elif dataset_name == "02_stocks_productos_todos":
        filepath = pkg_resources.resource_filename(
            "empresa4", "datasets/tb_stocks_02_productos_todos.csv"
        )

    elif dataset_name == "02_stocks_anti_leak":
        filepath = pkg_resources.resource_filename(
            "empresa4", "datasets/tb_stocks_02_productos_todos_anti_leak.csv"
        )
    
    elif dataset_name == "02_productos_todos_anti_leak_con_FE_04":
        filepath = pkg_resources.resource_filename(
            "empresa4", "datasets/tb_sellout_02_productos_todos_con_FE_04.csv"
        )

    elif dataset_name == "02_productos_todos_anti_leak_con_FE_06":
        filepath = pkg_resources.resource_filename(
            "empresa4", "datasets/tb_sellout_02_productos_todos_con_FE_06.csv"
        )

    df = pd.read_csv(filepath)
    return df
