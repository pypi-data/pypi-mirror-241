from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DefaultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "size"

    def get_paginated_response(
        self,
        data: list,
    ):
        response_data = OrderedDict(
            [
                ("total_count", self.page.paginator.count),
                ("total_pages", self.page.paginator.num_pages),
                ("current_page", self.page.number),
                ("next", self.get_next_link()),
                ("previous", self.get_previous_link()),
                ("results", data),
            ]
        )
        response = Response(response_data)
        return response
