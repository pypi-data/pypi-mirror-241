import json

from mediaApiClient import *

contentApi = ClientStreamControllerV2("https://mediapi.dev.mediatech.dev", "5XxN5QOlRf5tel0GOgxU1nBz5iFjmlzq6T7l9uFhcLqQw6hQLjUlCfQdF9QvXF7mpyV2hSHn6dBwr3IUPy64xc2eWtWzbhGJlvk4cS99Y0eU3f97Q2o9qLwBvtpX3jCjQYSXxVXsZqO0FrO7SIk5SaHJSm3W8IS1ZvSYYFctgoy8q4ktmq7cRPTuuZcPznVSyMY47F1SVDIcbjKbF5KnKiesAs7aXXU1ieEsP2ubtr2mR8n9b5ShdF70pC8YfZl")

response = contentApi.get_stream_for_content("2101f069c8bf48c94b98c058dc0427f1", "testAccount0111", "all", True)

print(response)
