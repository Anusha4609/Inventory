from googleapiclient.discovery import build
import json


def get_books_data(query):
    """Retriving data from google books API"""

    service = build('books','v1',developerKey='AIzaSyANbvD4tJaRiHd2gwAoo_YPXeH5FJzhhRA')
    request = service.volumes().list(q=query)
    response = request.execute()
    book_list = [response['items'][item]
    for item in range(len(response['items']))]

    return book_list

def get_books_data_ById(query):
    """Retriving data from google books API"""

    service = build('books','v1',developerKey='AIzaSyANbvD4tJaRiHd2gwAoo_YPXeH5FJzhhRA')
    string = 'id=' + query
    request = service.volumes().get(volumeId=query)
    response = request.execute()

    return response
