"""
This guide demonstrates how to use Great Expectations in a quick-start
notebook environment with Pandas. It is useful to explore and understand how Great Expectations
works, using your own data.

Note:
- Do not follow this workflow when you are building a durable workflow because it uses
ephemeral assets.
- Do not use this workflow for embedding in a pipeline or CI system, because it uses an
iterative process for trying and refining expectations.
"""


# <snippet name="tests/integration/docusaurus/tutorials/quickstart/v1_pandas_quickstart.py import_gx">
import great_expectations as gx
import great_expectations.expectations as gxe

# </snippet>

# Set up
# <snippet name="tests/integration/docusaurus/tutorials/quickstart/v1_pandas_quickstart.py get_context">
context = gx.get_context()
# </snippet>

# <snippet name="tests/integration/docusaurus/tutorials/quickstart/v1_pandas_quickstart.py connect_to_data">
batch = context.sources.pandas_default.read_csv(
    "https://raw.githubusercontent.com/great-expectations/great_expectations/develop/tests/test_sets/quickstart/yellow_tripdata_sample_2022-01.csv"
)
# </snippet>

# <snippet name="tests/integration/docusaurus/tutorials/quickstart/v1_pandas_quickstart.py create_expectation">
expectation = gxe.ExpectColumnValuesToBeBetween(
    column="passenger_count",
    min_value=0,
    max_value=6,
    notes="Per the TLC data dictionary, this is a driver-submitted value (historically between 0 to 6)",
)
result = batch.validate(expectation)
result.describe()
# </snippet>
assert result.success is False

# <snippet name="tests/integration/docusaurus/tutorials/quickstart/v1_pandas_quickstart.py update_expectation">
# Review the results of the expectation! Change parameters as needed.
expectation.mostly = 0.95
result = batch.validate(expectation)

suite = context.add_expectation_suite("quickstart")
suite.add_expectation(expectation)
suite.add_expectation(gxe.ExpectColumnValuesToNotBeNull(column="trip_distance"))
# </snippet>
assert result.success is True
assert result.expectation_config.kwargs["mostly"] == 0.95

suite_result = batch.validate(suite)
assert suite_result.success

suite_result.describe()
