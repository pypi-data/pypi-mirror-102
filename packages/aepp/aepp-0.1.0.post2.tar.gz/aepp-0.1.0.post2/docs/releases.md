# Releases information

__This page will be completed once version 0.1.0 is achieved.__

## version 0.1.0

* official release of the aepp module as beta python module with support.\
  The module include:
  * Automatic token generation and maintenance
  * Documentation on use-cases for the modules (with a star)
  * Support to most endpoints described on the [AEP API documentation](https://www.adobe.io/apis/experienceplatform/home/api-reference.html) (as January 2021).
    * Schema *
    * Query Service *
    * Identity *
    * Privacy Service
    * Sandboxes *
    * Segmentation *
    * Sensei
    * Flow Service *
    * Dule
    * Customer Profile *
    * Catalog *
    * Data Access *
    * Mapping Service *
    * Datasets *
    * Ingestion *
  
Patches:
* fix `save` option in `getSchemaSample`
* add `save` option to `getSchemaPaths`
* change `getBatches` method parameters to add "dataframe" and "raw" ouputs options
* upgrading the docstring for `postQuery` method
* changing `exportJobs` to `getExportJobs`
* removing some duplicate attributes in `QueryService` class

Return to [README](../README.md)