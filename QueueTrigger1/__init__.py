import logging
import io
import pycurl
import azure.functions as func


def main(msg: func.QueueMessage) -> None:
    buffer = io.BytesIO()
    curl = pycurl.Curl()
