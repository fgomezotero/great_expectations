---
sidebar_label: 'Manage Data Assets'
title: 'Manage Data Assets'
description: Create and manage Data Assets in GX Cloud.
toc_min_heading_level: 2
toc_max_heading_level: 2
---

A Data Asset is a collection of records that you create when you connect to your Data Source. When you connect to your Data Source, you define a minimum of one Data Asset. You use these Data Assets to create the Batch Requests that select the data that is provided to your Expectations.

To learn more about Data Assets, see [Data Asset](../../terms/data_asset.md).

## Prerequisites

- You have a [GX Cloud Beta account](https://greatexpectations.io/cloud).

- You have [set up your environment](../set_up_gx_cloud.md), you have set the `GX_CLOUD_SNOWFLAKE_PASSWORD` environment variable, and the GX Agent is running. 

- You have a [Snowflake account](https://docs.snowflake.com/en/user-guide-admin) with USAGE privileges on the table, database, and schema you are validating, and you know your password.


## Create a Data Asset

Create a Data Asset to define the data you want GX Cloud to access. Currently, the GX Cloud user interface is configured for Snowflake. To connect to Data Assets on another Data Source, see [Connect to source data](https://deploy-preview-8760.docs.greatexpectations.io/docs/guides/connecting_to_your_data/connect_to_data_lp) in the GX OSS documentation. 

1. In GX Cloud, click **Data Assets** > **New Asset**.

2. Complete the following mandatory fields:

    - **Datasource name**: Enter a meaningful name for the Data Asset.

    - **Username**: Enter your Snowflake username.

    - **Password variable**: Enter `GX_CLOUD_SNOWFLAKE_PASSWORD`.

    - **Account or locator**: Enter your Snowflake account or locator information. The locator value must include the geographical region. For example, `us-east-1`. To locate these values see [Account Identifiers](https://docs.snowflake.com/en/user-guide/admin-account-identifier).

3. Optional. Complete the following fields:

    - **Database**: Enter the name of the Snowflake database where the data you want to validate is stored.
 
    - **Schema**: Enter the name of the schema for the Snowflake database where the data you want to validate is stored.

    - **Warehouse**: Enter the name of the Snowflake database warehouse.

    - **Role**: Enter your Snowflake role.

    - **Authenticator**: Enter the Snowflake database authenticator that you want to use to verify your Snowflake connection. 

4. Optional. Clear **Create temp table** if you don't want to create a temporary database table. Temporary database tables store data temporarily and can improve performance by making queries run faster.

5. Optional. Clear **Test connection** if you don't want to test the Data Asset connection. Testing the connection to the Data Asset is a preventative measure that makes sure the connection configuration is correct. This verification can help you avoid errors and can reduce troubleshooting downtime.

6. Select **Table Asset** or **Query Asset** and complete the following fields:

    - **Asset name**: Enter a name for the Data Asset. Data Asset names must be unique. If you use the same name for multiple Data Assets, each Data Asset must be associated with a unique Data Source.

    - **Table name**: When **Table Asset** is selected, enter a name for the table you're creating in the Data Asset.

    - **Query**: When **Query Asset** is selected, enter the query that you want to run on the table. 

7. Optional. Select **Add table/query** to add additional tables or queries and repeat step 6.

8. Click **Finish**.

9. Create an Expectation. See [Create an Expectation](/cloud/expectations/manage_expectations.md#create-an-expectation).

## View Data Asset metrics

Data Asset metrics provide you with insight into the data you can use for your data validations. 

1. In GX Cloud, click **Data Assets** and then select a Data Asset in the **Data Assets** list.

2. Click the **Overview** tab.

3. Select one of the following options: 

    - If you have not previously generated Data Asset metrics, click **Fetch Metrics**. 

    - If you previously generated Data Asset metrics, click **Refresh** to refresh the metrics.

### Available Data Asset metrics

The following table lists the available Data Asset metrics.

| Column                                   | Description                                               | 
|------------------------------------------|-----------------------------------------------------------|
| **Row Count**                            | The number of rows within a Data Asset.                   | 
| **Column**                               | A column within your Data Asset.                          | 
| **Type**                                 | The data storage type in the Data Asset column.           | 
| **Min**                                  | For numeric columns the lowest value in the column.       | 
| **Max**                                  | For numeric columns, the highest value in the column.     | 
| **Mean**                                 | For numeric columns, the average value with the column.<br/> This is determined by dividing the sum of all values in the Data Asset by the number of values.  |
| **Median**                                 | For numeric columns, the value in the middle of a data set.<br/> 50% of the data within the Data Asset has a value smaller or equal to the median, and 50% of the data within the Data Asset has a value that is higher or equal to the median.  |
| **Null %**                                | The percentage of missing values in a column.             |


## Edit a Data Asset

1. In Jupyter Notebook, run the following code to import the `great_expectations` module and the existing Data Context:

    ```python title="Jupyter Notebook"
    import great_expectations as gx
    context = gx.get_context()
    ```

2. Run the following code to retrieve the Data Source:

    ```python title="Jupyter Notebook"
    datasource = context.get_datasource("<data_source_name>")
    ```

3. Edit the Data Asset settings. For example, run the following code to change the name of the Data Source:

    ```python title="Jupyter Notebook"
    datasource.name = "<new_data_source_name>"
    ```

    To review the Data Asset parameters that you can add or edit, see the [GX API documentation](https://deploy-preview-8760.docs.greatexpectations.io/docs/reference/api_reference).

 4. Run the following code to save your changes:

    ```python title="Jupyter Notebook"
    context.sources.update_snowflake(datasource)
    ```

## Delete a Data Asset

1. In GX Cloud, click **Settings** > **Datasources**.

2. Click **Delete** for the Data Source and the associated Data Assets you want to delete.

3. Click **Delete**.

