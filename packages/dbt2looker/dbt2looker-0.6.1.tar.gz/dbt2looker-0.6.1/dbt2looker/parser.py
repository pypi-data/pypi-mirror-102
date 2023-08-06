from typing import Dict, Optional

from . import models


def validate_manifest(raw_manifest: dict):
    return True


def validate_catalog(raw_catalog: dict):
    return True


def parse_dbt_project_config(raw_config: dict):
    return models.DbtProjectConfig(**raw_config)


def parse_catalog_nodes(raw_catalog: dict):
    catalog = models.DbtCatalog(**raw_catalog)
    return catalog.nodes


def parse_adapter_type(raw_manifest: dict):
    manifest = models.DbtManifest(**raw_manifest)
    return manifest.metadata.adapter_type


def parse_models(raw_manifest: dict, tag=None):
    manifest = models.DbtManifest(**raw_manifest)
    all_models = [
        node
        for node in manifest.nodes.values()
        if node.resource_type == 'model'
    ]
    filtered_models = (
        all_models if tag is None else [
            model for model in all_models
            if tag in model.tags
        ]
    )
    return filtered_models


def parse_typed_models(raw_manifest: dict, raw_catalog: dict, tag: Optional[str] = None):
    catalog_nodes = parse_catalog_nodes(raw_catalog)
    dbt_models = parse_models(raw_manifest, tag=tag)

    # Update dbt models with data types from catalog
    dbt_typed_models = [
        model.copy(update={'columns': {
            column.name: column.copy(update={
                'data_type': get_column_type_from_catalog(catalog_nodes, model.unique_id, column.name)
            })
            for column in model.columns.values()
        }})
        for model in dbt_models
    ]
    return dbt_typed_models


def get_column_type_from_catalog(catalog_nodes: Dict[str, models.DbtCatalogNode], model_id: str, column_name: str):
    node = catalog_nodes.get(model_id)
    column = None if node is None else node.columns.get(column_name)
    return None if column is None else column.type
