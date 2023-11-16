from setuptools import setup, find_packages

setup(
    name="dconnector",
    version="0.1.0",
    author="Ddhruv Arora",
    author_email="<ddhruvarora2@gmail.com>",
    description="The dconnector Python package provides a streamlined interface for connecting to MongoDB databases using the MongoDBConnection class in Streamlit Projects. This class encapsulates common MongoDB operations, such as querying, inserting, updating, and deleting documents, and provides a convenient way to interact with MongoDB collections using pandas DataFrames.",
    long_description="""

The dconnector Python package facilitates MongoDB database interactions through the MongoDBConnection class. This class extends streamlit.connections.ExperimentalBaseConnection and integrates with the pymongo library to offer a comprehensive set of functionalities for working with MongoDB collections. Users can establish connections by specifying the MongoDB connection string, database name, and collection name, either through explicit parameters or by relying on stored secrets.

The provided methods cover a wide range of MongoDB operations, including querying documents based on filters, retrieving all documents, finding a single document, and executing custom queries. The package supports caching mechanisms to enhance performance, allowing users to set time-to-live values for cached results.

In addition to query operations, the MongoDBConnection class supports document insertion, either for a single document or multiple documents in a batch. Users can also update and delete documents based on specified queries. The class further provides methods for counting documents, retrieving distinct values for a given field, and paginating through the collection.

To ensure flexibility, the class exposes several optional keyword arguments for each operation, allowing users to customize their MongoDB queries. The pandas library is leveraged to convert query results into easily manipulable DataFrames, simplifying data analysis and manipulation tasks.

This package aims to streamline MongoDB interactions within Python applications, offering an abstraction layer that balances ease of use with robust functionality.""",
    packages=find_packages(),
    install_requires=["streamlit", "pymongo", "pandas"],
    python_requires=">=3.6",
    provides=["dconnector"],
)
