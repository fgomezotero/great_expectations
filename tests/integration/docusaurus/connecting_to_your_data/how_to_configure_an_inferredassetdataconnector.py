# <snippet name="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py imports yaml">
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py imports python">
import great_expectations as gx
from great_expectations.core.batch import BatchRequest

# </snippet>
from great_expectations.core.yaml_handler import YAMLHandler

yaml = YAMLHandler()
# </snippet>

context = gx.get_context()

# YAML
datasource_yaml = r"""
name: taxi_datasource
class_name: Datasource
module_name: great_expectations.datasource
execution_engine:
  module_name: great_expectations.execution_engine
  class_name: PandasExecutionEngine
data_connectors:
  default_inferred_data_connector_name:
    class_name: InferredAssetFilesystemDataConnector
    base_directory: <MY DIRECTORY>/
    default_regex:
      group_names:
        - data_asset_name
      pattern: (.*)\.csv
"""

# Please note this override is only to provide good UX for docs and tests.
# In normal usage you'd set your path directly in the yaml above.
datasource_yaml = datasource_yaml.replace(
    "<MY DIRECTORY>/", "../data/single_directory_one_data_asset/"
)

test_yaml = context.test_yaml_config(
    datasource_yaml,
)

# Python
datasource_config = {
    "name": "taxi_datasource",
    "class_name": "Datasource",
    "module_name": "great_expectations.datasource",
    "execution_engine": {
        "module_name": "great_expectations.execution_engine",
        "class_name": "PandasExecutionEngine",
    },
    "data_connectors": {
        "default_inferred_data_connector_name": {
            "class_name": "InferredAssetFilesystemDataConnector",
            "base_directory": "<MY DIRECTORY>/",
            "default_regex": {
                "group_names": ["data_asset_name"],
                "pattern": r"(.*)\.csv",
            },
        },
    },
}

# Please note this override is only to provide good UX for docs and tests.
# In normal usage you'd set your path directly in the code above.
datasource_config["data_connectors"]["default_inferred_data_connector_name"][
    "base_directory"
] = "../data/single_directory_one_data_asset/"

test_python = context.test_yaml_config(
    yaml.dump(datasource_config),
)

context.add_datasource(**datasource_config)

assert [ds["name"] for ds in context.list_datasources()] == ["taxi_datasource"]
assert "yellow_tripdata_2019-01" in set(
    context.get_available_data_asset_names()["taxi_datasource"][
        "default_inferred_data_connector_name"
    ]
)

# YAML
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_yaml each file own data asset">
datasource_yaml = r"""
name: taxi_datasource
class_name: Datasource
module_name: great_expectations.datasource
execution_engine:
  module_name: great_expectations.execution_engine
  class_name: PandasExecutionEngine
data_connectors:
  default_inferred_data_connector_name:
    class_name: InferredAssetFilesystemDataConnector
    base_directory: <MY DIRECTORY>/
    default_regex:
      group_names:
        - data_asset_name
        - year
        - month
      pattern: (.*)_(\d{4})-(\d{2})\.csv
"""
# </snippet>

# Please note this override is only to provide good UX for docs and tests.
# In normal usage you'd set your path directly in the yaml above.
datasource_yaml = datasource_yaml.replace(
    "<MY DIRECTORY>/", "../data/single_directory_one_data_asset/"
)

test_yaml = context.test_yaml_config(
    datasource_yaml,
)

# Python
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_config each file own data asset">
datasource_config = {
    "name": "taxi_datasource",
    "class_name": "Datasource",
    "module_name": "great_expectations.datasource",
    "execution_engine": {
        "module_name": "great_expectations.execution_engine",
        "class_name": "PandasExecutionEngine",
    },
    "data_connectors": {
        "default_inferred_data_connector_name": {
            "class_name": "InferredAssetFilesystemDataConnector",
            "base_directory": "<MY DIRECTORY>/",
            "default_regex": {
                "group_names": ["data_asset_name", "year", "month"],
                "pattern": r"(.*)_(\d{4})-(\d{2})\.csv",
            },
        },
    },
}
# </snippet>

# Please note this override is only to provide good UX for docs and tests.
# In normal usage you'd set your path directly in the code above.
datasource_config["data_connectors"]["default_inferred_data_connector_name"][
    "base_directory"
] = "../data/single_directory_one_data_asset/"

test_python = context.test_yaml_config(
    yaml.dump(datasource_config),
)

context.add_datasource(**datasource_config)

assert [ds["name"] for ds in context.list_datasources()] == ["taxi_datasource"]
assert "yellow_tripdata" in set(
    context.get_available_data_asset_names()["taxi_datasource"][
        "default_inferred_data_connector_name"
    ]
)

# YAML
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_yaml add an InferredAssetDataConnector to a Datasource configuration">
datasource_yaml = r"""
name: taxi_datasource
class_name: Datasource
module_name: great_expectations.datasource
execution_engine:
  module_name: great_expectations.execution_engine
  class_name: PandasExecutionEngine
data_connectors:
  default_inferred_data_connector_name:
    class_name: InferredAssetS3DataConnector
    bucket: <MY S3 BUCKET>/
    prefix: <MY S3 BUCKET PREFIX>/
    default_regex:
      group_names:
        - prefix
        - data_asset_name
        - year
        - month
      pattern: (.*)/(.*)_sample_(\d{4})-(\d{2})\.csv
"""
# </snippet>

# Please note this override is only to provide good UX for docs and tests.
# In normal usage you'd set your path directly in the yaml above.
datasource_yaml = datasource_yaml.replace(
    "<MY S3 BUCKET>/", "superconductive-docs-test"
)
datasource_yaml = datasource_yaml.replace(
    "<MY S3 BUCKET PREFIX>/", "data/taxi_yellow_tripdata_samples/"
)

test_yaml = context.test_yaml_config(
    datasource_yaml,
)

# Python
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_config add an InferredAssetDataConnector to a Datasource configuration">
datasource_config = {
    "name": "taxi_datasource",
    "class_name": "Datasource",
    "module_name": "great_expectations.datasource",
    "execution_engine": {
        "module_name": "great_expectations.execution_engine",
        "class_name": "PandasExecutionEngine",
    },
    "data_connectors": {
        "default_inferred_data_connector_name": {
            "class_name": "InferredAssetS3DataConnector",
            "bucket": "<MY S3 BUCKET>/",
            "prefix": "<MY S3 BUCKET PREFIX>/",
            "default_regex": {
                "group_names": ["prefix", "data_asset_name", "year", "month"],
                "pattern": r"(.*)/(.*)_sample_(\d{4})-(\d{2})\.csv",
            },
        },
    },
}
# </snippet>

# Please note this override is only to provide good UX for docs and tests.
# In normal usage you'd set your path directly in the code above.
datasource_config["data_connectors"]["default_inferred_data_connector_name"][
    "bucket"
] = "superconductive-docs-test"
datasource_config["data_connectors"]["default_inferred_data_connector_name"][
    "prefix"
] = "data/taxi_yellow_tripdata_samples/"

test_python = context.test_yaml_config(
    yaml.dump(datasource_config),
)

context.add_datasource(**datasource_config)

assert [ds["name"] for ds in context.list_datasources()] == ["taxi_datasource"]
assert "yellow_tripdata" in set(
    context.get_available_data_asset_names()["taxi_datasource"][
        "default_inferred_data_connector_name"
    ]
)

# YAML
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_yaml basic configuration with more than one Data Asset">
datasource_yaml = r"""
name: taxi_datasource
class_name: Datasource
module_name: great_expectations.datasource
execution_engine:
  module_name: great_expectations.execution_engine
  class_name: PandasExecutionEngine
data_connectors:
  default_inferred_data_connector_name:
    class_name: InferredAssetFilesystemDataConnector
    base_directory: <MY DIRECTORY>/
    default_regex:
      group_names:
        - data_asset_name
        - year
        - month
      pattern: (.*)_(\d{4})-(\d{2})\.csv
"""
# </snippet>

# Please note this override is only to provide good UX for docs and tests.
# In normal usage you'd set your path directly in the yaml above.
datasource_yaml = datasource_yaml.replace(
    "<MY DIRECTORY>/", "../data/single_directory_one_data_asset/"
)

test_yaml = context.test_yaml_config(
    datasource_yaml,
)

# Python
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_config basic configuration with more than one Data Asset">
datasource_config = {
    "name": "taxi_datasource",
    "class_name": "Datasource",
    "module_name": "great_expectations.datasource",
    "execution_engine": {
        "module_name": "great_expectations.execution_engine",
        "class_name": "PandasExecutionEngine",
    },
    "data_connectors": {
        "default_inferred_data_connector_name": {
            "class_name": "InferredAssetFilesystemDataConnector",
            "base_directory": "<MY DIRECTORY>/",
            "default_regex": {
                "group_names": ["data_asset_name", "year", "month"],
                "pattern": r"(.*)_(\d{4})-(\d{2})\.csv",
            },
        },
    },
}
# </snippet>

# Please note this override is only to provide good UX for docs and tests.
# In normal usage you'd set your path directly in the code above.
datasource_config["data_connectors"]["default_inferred_data_connector_name"][
    "base_directory"
] = "../data/single_directory_one_data_asset/"

test_python = context.test_yaml_config(
    yaml.dump(datasource_config),
)

context.add_datasource(**datasource_config)

assert [ds["name"] for ds in context.list_datasources()] == ["taxi_datasource"]
assert "yellow_tripdata" in set(
    context.get_available_data_asset_names()["taxi_datasource"][
        "default_inferred_data_connector_name"
    ]
)

# <snippet name="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py get_validator">
batch_request = BatchRequest(
    datasource_name="taxi_datasource",
    data_connector_name="default_inferred_data_connector_name",
    data_asset_name="yellow_tripdata",
)

validator = context.get_validator(
    batch_request=batch_request,
    create_expectation_suite_with_name="<MY EXPECTATION SUITE NAME>",
)
# </snippet>

# NOTE: The following code is only for testing and can be ignored by users.
assert isinstance(validator, gx.validator.validator.Validator)

# <snippet name="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py batch_request 2019-02">
batch_request = BatchRequest(
    datasource_name="taxi_datasource",
    data_connector_name="default_inferred_data_connector_name",
    data_asset_name="yellow_tripdata",
    data_connector_query={"batch_filter_parameters": {"year": "2019", "month": "02"}},
)

validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name="<MY EXPECTATION SUITE NAME>",
)
# </snippet>

# NOTE: The following code is only for testing and can be ignored by users.
assert isinstance(validator, gx.validator.validator.Validator)
assert validator.active_batch_definition.batch_identifiers == {
    "year": "2019",
    "month": "02",
}

# YAML
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_yaml nested directory structure with the data_asset_name on the inside">
datasource_yaml = r"""
name: taxi_datasource
class_name: Datasource
module_name: great_expectations.datasource
execution_engine:
  module_name: great_expectations.execution_engine
  class_name: PandasExecutionEngine
data_connectors:
  default_inferred_data_connector_name:
    class_name: InferredAssetFilesystemDataConnector
    base_directory: <MY DIRECTORY>/
    glob_directive: "*/*/*.csv"
    default_regex:
      group_names:
        - year
        - month
        - data_asset_name
      pattern: (\d{4})/(\d{2})/(.*)\.csv
"""
# </snippet>

# Please note this override is only to provide good UX for docs and tests.
# In normal usage you'd set your path directly in the yaml above.
datasource_yaml = datasource_yaml.replace(
    "<MY DIRECTORY>/", "../data/nested_directories_time/"
)

test_yaml = context.test_yaml_config(
    datasource_yaml,
)

# Python
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_config nested directory structure with the data_asset_name on the inside">
datasource_config = {
    "name": "taxi_datasource",
    "class_name": "Datasource",
    "module_name": "great_expectations.datasource",
    "execution_engine": {
        "module_name": "great_expectations.execution_engine",
        "class_name": "PandasExecutionEngine",
    },
    "data_connectors": {
        "default_inferred_data_connector_name": {
            "class_name": "InferredAssetFilesystemDataConnector",
            "base_directory": "<MY DIRECTORY>/",
            "glob_directive": "*/*/*.csv",
            "default_regex": {
                "group_names": ["year", "month", "data_asset_name"],
                "pattern": r"(\d{4})/(\d{2})/(.*)\.csv",
            },
        },
    },
}
# </snippet>

# Please note this override is only to provide good UX for docs and tests.
# In normal usage you'd set your path directly in the code above.
datasource_config["data_connectors"]["default_inferred_data_connector_name"][
    "base_directory"
] = "../data/nested_directories_time/"

test_python = context.test_yaml_config(
    yaml.dump(datasource_config),
)

context.add_datasource(**datasource_config)

assert [ds["name"] for ds in context.list_datasources()] == ["taxi_datasource"]
assert "yellow_tripdata" in set(
    context.get_available_data_asset_names()["taxi_datasource"][
        "default_inferred_data_connector_name"
    ]
)
assert "green_tripdata" in set(
    context.get_available_data_asset_names()["taxi_datasource"][
        "default_inferred_data_connector_name"
    ]
)

# YAML
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_yaml nested directory structure with the data_asset_name on the outside">
datasource_yaml = r"""
name: taxi_datasource
class_name: Datasource
module_name: great_expectations.datasource
execution_engine:
  module_name: great_expectations.execution_engine
  class_name: PandasExecutionEngine
data_connectors:
  default_inferred_data_connector_name:
    class_name: InferredAssetFilesystemDataConnector
    base_directory: <MY DIRECTORY>/
    glob_directive: "*/*.csv"
    default_regex:
      group_names:
        - data_asset_name
        - file_name_root
        - year
        - month
      pattern: (.*)/(.*)(\d{4})-(\d{2})\.csv
"""
# </snippet>

# Please note this override is only to provide good UX for docs and tests.
# In normal usage you'd set your path directly in the yaml above.
datasource_yaml = datasource_yaml.replace(
    "<MY DIRECTORY>/", "../data/nested_directories_data_asset/"
)

test_yaml = context.test_yaml_config(
    datasource_yaml,
)

# Python
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_config nested directory structure with the data_asset_name on the outside">
datasource_config = {
    "name": "taxi_datasource",
    "class_name": "Datasource",
    "module_name": "great_expectations.datasource",
    "execution_engine": {
        "module_name": "great_expectations.execution_engine",
        "class_name": "PandasExecutionEngine",
    },
    "data_connectors": {
        "default_inferred_data_connector_name": {
            "class_name": "InferredAssetFilesystemDataConnector",
            "base_directory": "<MY DIRECTORY>/",
            "glob_directive": "*/*.csv",
            "default_regex": {
                "group_names": [
                    "data_asset_name",
                    "file_name_root",
                    "year",
                    "month",
                ],
                "pattern": r"(.*)/(.*)(\d{4})-(\d{2})\.csv",
            },
        },
    },
}
# </snippet>

# Please note this override is only to provide good UX for docs and tests.
# In normal usage you'd set your path directly in the code above.
datasource_config["data_connectors"]["default_inferred_data_connector_name"][
    "base_directory"
] = "../data/nested_directories_data_asset/"

test_python = context.test_yaml_config(
    yaml.dump(datasource_config),
)

context.add_datasource(**datasource_config)

assert [ds["name"] for ds in context.list_datasources()] == ["taxi_datasource"]
assert "yellow_tripdata" in set(
    context.get_available_data_asset_names()["taxi_datasource"][
        "default_inferred_data_connector_name"
    ]
)
assert "green_tripdata" in set(
    context.get_available_data_asset_names()["taxi_datasource"][
        "default_inferred_data_connector_name"
    ]
)

# YAML
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_yaml redundant information in the naming convention">
datasource_yaml = r"""
name: taxi_datasource
class_name: Datasource
module_name: great_expectations.datasource
execution_engine:
  module_name: great_expectations.execution_engine
  class_name: PandasExecutionEngine
data_connectors:
  default_inferred_data_connector_name:
    class_name: InferredAssetFilesystemDataConnector
    base_directory: <MY DIRECTORY>/
    glob_directive: "*/*.csv"
    default_regex:
      group_names:
        - data_asset_name
        - year
        - month
      pattern: (.*)/.*(\d{4})-(\d{2})\.csv
"""
# </snippet>

# Please note this override is only to provide good UX for docs and tests.
# In normal usage you'd set your path directly in the yaml above.
datasource_yaml = datasource_yaml.replace(
    "<MY DIRECTORY>/", "../data/nested_directories_data_asset/"
)

test_yaml = context.test_yaml_config(
    datasource_yaml,
)

# Python
# <snippet name="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py python datasource_config redundant information in the naming convention">
datasource_config = {
    "name": "taxi_datasource",
    "class_name": "Datasource",
    "module_name": "great_expectations.datasource",
    "execution_engine": {
        "module_name": "great_expectations.execution_engine",
        "class_name": "PandasExecutionEngine",
    },
    "data_connectors": {
        "default_inferred_data_connector_name": {
            "class_name": "InferredAssetFilesystemDataConnector",
            "base_directory": "<MY DIRECTORY>/",
            "glob_directive": "*/*.csv",
            "default_regex": {
                "group_names": [
                    "data_asset_name",
                    "year",
                    "month",
                ],
                "pattern": r"(.*)/.*(\d{4})-(\d{2})\.csv",
            },
        },
    },
}
# </snippet>

# Please note this override is only to provide good UX for docs and tests.
# In normal usage you'd set your path directly in the code above.
datasource_config["data_connectors"]["default_inferred_data_connector_name"][
    "base_directory"
] = "../data/nested_directories_data_asset/"

test_python = context.test_yaml_config(
    yaml.dump(datasource_config),
)

context.add_datasource(**datasource_config)

assert [ds["name"] for ds in context.list_datasources()] == ["taxi_datasource"]
assert "yellow_tripdata" in set(
    context.get_available_data_asset_names()["taxi_datasource"][
        "default_inferred_data_connector_name"
    ]
)
assert "green_tripdata" in set(
    context.get_available_data_asset_names()["taxi_datasource"][
        "default_inferred_data_connector_name"
    ]
)
