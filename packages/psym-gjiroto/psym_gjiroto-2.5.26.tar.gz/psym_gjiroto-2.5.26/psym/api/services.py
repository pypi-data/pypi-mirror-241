#!/usr/bin/env python3
# Copyright (c) 2004-present Facebook All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from psym.client import SymphonyClient
from psym.common.data_class import Service
from psym.common.constant import PAGINATION_STEP
from typing import Iterator
from ..graphql.query.services import Services


def get_services(client: SymphonyClient) -> Iterator[Service]:
    """ this funtion Get all Services
    :return: alarmStatus object
    :rtype: Iterator[ :class:`~psym.common.data_class.Service` ]
    **Example**
    .. code-block:: python
        services = client.get_get_services()
        for services_ in services:
            print(services_.name)
    """
    Services_ = Services.execute(client, first=PAGINATION_STEP)
    edges = Services_.edges if Services_ else []
    while Services_ is not None and Services_.pageInfo.hasNextPage:
        Services_ = Services.execute(
            client, after=Services_.pageInfo.endCursor, first=PAGINATION_STEP
        )
        if Services_ is not None:
            edges.extend(Services_.edges)
    for edge in edges:
        node = edge.node
        if node is not None:
            yield Service(
                id=node.id,
                name=node.name,
                external_id=node.externalId,
                status=node.status,
                service_type_name=node.serviceType.name,
                customer=None,
                properties=node.properties,
            )